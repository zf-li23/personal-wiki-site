---
title: Computing on Servers and Clusters
description: "Using shared Linux servers and high-performance computing clusters for computational biology: the anatomy of a cluster and its file systems, software environments with modules, conda and containers, batch jobs with Slurm (resource requests, job arrays, dependencies, priorities and backfill), threaded, multi-process, MPI and GPU jobs, moving and verifying data with rsync and checksums, and workflow managers (Snakemake, Nextflow) that tie it all together."
---

A laptop is enough to develop an analysis but rarely to run it: aligning the reads of a few dozen RNA-seq samples, calling variants on whole genomes, assembling a genome or training a model needs more cores, memory and storage than a personal machine has, for hours or days. Such work runs on shared Linux machines, a lab server or a university's high-performance computing (HPC) cluster, accessed remotely with the tools of [4.11.10](/4.11.10). This chapter is the practical end point of the course. It uses **processes** and scheduling ([4.11.2](/4.11.2), [4.11.3](/4.11.3)), **threads** ([4.11.6](/4.11.6)), **file systems** and storage ([4.11.7](/4.11.7), [4.11.8](/4.11.8)) and **containers** ([4.11.9](/4.11.9)) to explain how a cluster is organized, how software is made available on it, how batch jobs are described and scheduled with Slurm, how to parallelize work, how to move data, and how workflow managers automate multi-step analyses. Details such as partition names, limits and storage paths differ from site to site; every cluster documents them, and that documentation takes precedence over the generic examples here.

## 11.1. The Anatomy of a Cluster

### 11.1.1. Nodes and Networks

**Definition 11.1.1 (Computing Cluster)** A **computing cluster** is a set of computers, its *nodes*, connected by a fast network and managed as one system: users log in to *login nodes*, which are shared by everyone and meant for editing, compiling, submitting and monitoring work; computations run on *compute nodes*, which are allocated to jobs by a *workload manager*; and all nodes mount the same shared file systems.

A typical cluster has a few login nodes, hundreds to thousands of compute nodes with two multicore CPUs (64–256 cores in total) and 256 GiB to several TiB of memory each, a smaller number of nodes with GPUs or very large memory, and storage servers. The nodes are connected by an Ethernet network for management and by a low-latency interconnect (InfiniBand, or high-speed Ethernet with RDMA) for parallel programs and storage. Login nodes are the one shared resource that everyone touches: running a heavy computation there slows down the whole user community and is usually killed automatically. Everything except light work belongs in a job (§11.3); for interactive work, request an interactive session on a compute node.

### 11.1.2. Storage

A cluster offers several **file systems** with different purposes, and choosing the right one for each kind of data is part of using it well:

| Area | Typical file system | Size and policy | Use for |
|---|---|---|---|
| home (`$HOME`) | NFS, backed up | small quota (tens of GB) | scripts, configuration, small source code |
| project or group | NFS or parallel FS, sometimes backed up | large quota (TB), shared by a group | raw data, final results, shared references |
| scratch | parallel FS (Lustre, IBM Storage Scale, BeeGFS) | very large, fast, not backed up; files unused for some weeks are purged | intermediate files of running analyses |
| node-local | SSD on the compute node (often `$TMPDIR`) | hundreds of GB, deleted at the end of the job | temporary files with many small or random accesses |
| archive | tape behind a disk cache | very large, slow to retrieve | long-term preservation of raw data |

A parallel file system stripes each large file over many storage servers, so that hundreds of nodes reading the same reference or writing different BAM files obtain an aggregate bandwidth of many gigabytes per second. It is optimized for large sequential I/O, not for metadata: every `open`, `stat` and `ls` goes to a small number of metadata servers ([4.11.7](/4.11.7#sec-7.2.4)). A pipeline that creates millions of small files, or a conda environment with hundreds of thousands of files read on every Python start, can overload the metadata servers and is slow for its user. For this reason clusters limit the number of files (an **inode** quota, shown by `quota`, `lfs quota` or a site command) as well as their size, and recommend packing small files into archives, keeping software environments in containers (one SIF file, [4.11.9](/4.11.9#sec-9.6)), and putting temporary files on node-local disks.

## 11.2. Software Environments

Users cannot install software system-wide on a cluster (there is no `sudo`, [4.11.10](/4.11.10#sec-10.4)), and different projects need different versions of the same tools. Four mechanisms coexist.

**Definition 11.2.1 (Environment Module)** An **environment module** is a script, interpreted by a tool such as Lmod or Environment Modules, that modifies the shell's environment variables (`PATH`, `LD_LIBRARY_PATH`, `MANPATH` and others) so that a particular version of a software package installed centrally becomes available; loading and unloading modules switches between versions without conflict.

```bash
module avail                 # list modules that can be loaded now
module spider samtools       # search all modules, including those behind a compiler or MPI module
module load samtools/1.21    # make a version available
module list                  # show what is loaded
module purge                 # unload everything (start job scripts from a clean state)
```

HPC centers build their module trees with **package managers** designed for this purpose, Spack and EasyBuild, which compile each package against chosen compilers and MPI libraries. The other three mechanisms are under the user's control:

| Mechanism | Strengths | Weaknesses on a cluster |
|---|---|---|
| modules | built for the hardware (optimized compilers, MPI, GPU libraries), maintained by staff | only what staff installed; versions differ between clusters |
| conda / mamba / pixi environments ([4.4.1](/4.4.1#sec-1.4)) | Bioconda covers almost all bioinformatics tools; user-installable; reproducible with a **lock file** | hundreds of thousands of small files (store them on project space, not scratch, and watch the inode quota) |
| containers with Apptainer ([4.11.9](/4.11.9#sec-9.6)) | one file per environment, identical on laptop and cluster, the whole user space fixed | MPI and GPU need care to match the host |
| own builds in `$HOME/.local` | full control | maintenance burden |

A common arrangement is modules for compilers, MPI and CUDA, conda environments or containers for bioinformatics tools, and a workflow manager that creates the environments or pulls the images for each step automatically (§11.6).

## 11.3. Batch Jobs with Slurm

### 11.3.1. Jobs and the Workload Manager

**Definition 11.3.1 (Batch Job)** A **batch job** is a unit of work submitted to a workload manager: a script together with a request for resources (number of nodes, tasks, CPU cores, memory, GPUs, maximum run time). The workload manager queues the job, starts it on compute nodes when the requested resources become free and its priority allows, confines it to those resources, and records its accounting data. A job may consist of several *job steps*, each a set of parallel *tasks* (processes).

**Definition 11.3.2 (Workload Manager)** A **workload manager** (batch system, job scheduler) is the software that allocates the compute nodes of a cluster to batch jobs: it maintains queues of pending jobs, decides by a scheduling policy which jobs start when and where, launches and monitors them, and enforces their resource limits.

Slurm is the workload manager of most of the world's largest supercomputers and of many university clusters; others include PBS Pro/OpenPBS, IBM Spectrum LSF and HTCondor (which specializes in many independent jobs). In Slurm, the nodes are grouped into partitions (queues with their own limits, such as maximum run time or GPU nodes), and *QOS* (quality-of-service) settings and *accounts* determine limits and priorities. A Slurm job is confined by **cgroups** ([4.11.9](/4.11.9#sec-9.4.3)): it sees only its allocated cores, and exceeding the requested memory gets it killed.

### 11.3.2. A Job Script

A job script is a **shell** script whose initial comments starting with `#SBATCH` are options for `sbatch`:

```bash
#!/bin/bash
#SBATCH --job-name=align_ctrl1
#SBATCH --partition=standard          # site-specific
#SBATCH --nodes=1
#SBATCH --ntasks=1                    # one process ...
#SBATCH --cpus-per-task=8             # ... with 8 cores for its threads
#SBATCH --mem=16G                     # memory per node
#SBATCH --time=02:00:00               # wall-time limit, HH:MM:SS
#SBATCH --output=logs/%x_%j.out       # %x = job name, %j = job ID
#SBATCH --error=logs/%x_%j.err

set -euo pipefail
module purge
module load minimap2/2.28 samtools/1.21

cd "$SLURM_SUBMIT_DIR"
echo "job $SLURM_JOB_ID on $(hostname) with $SLURM_CPUS_PER_TASK cores"

minimap2 -t "$SLURM_CPUS_PER_TASK" -a ref/genome.fa fastq/ctrl_1.fq.gz \
    | samtools sort -@ 2 -m 1G -o results/ctrl_1.sorted.bam
samtools index results/ctrl_1.sorted.bam
```

The `logs` directory must exist before submission, since Slurm does not create it. The essential commands:

| Command | Purpose |
|---|---|
| `sbatch job.sh` | submit a batch script; prints the job ID |
| `squeue --me` | own pending (`PD`) and running (`R`) jobs, with the reason a job waits (`Priority`, `Resources`, a limit) |
| `scancel 12345`, `scancel --me` | cancel jobs |
| `sinfo` | partitions and the state of their nodes |
| `srun --pty --cpus-per-task=4 --mem=8G --time=1:00:00 bash` | an interactive shell on a compute node (`salloc` allocates resources and then runs commands in them) |
| `sacct -j 12345 --format=JobID,State,Elapsed,TotalCPU,MaxRSS,ReqMem` | accounting for finished jobs: state, time, peak memory |
| `seff 12345` | efficiency summary: used versus requested CPU time and memory (a contributed tool installed on many clusters) |
| `scontrol show job 12345` | every detail of a job |

### 11.3.3. Requesting Resources

The requested resources are both a limit and a cost: the job may not use more, and while it runs the requested resources are reserved for it whether it uses them or not, and charged to the account's fair share. Requests should be measured, not guessed: run one sample, look at `sacct` or `seff`, and request the observed peak memory plus a margin of 20–50 % and the observed time plus a margin.

| Request | Symptom when too small | Cost when too large |
|---|---|---|
| `--time` | job killed with state `TIMEOUT` | the scheduler cannot backfill it (§11.3.5); it waits longer |
| `--mem`, `--mem-per-cpu` | job killed with state `OUT_OF_MEMORY` (the cgroup's OOM killer, exit status 137) | waits for a node with that much free memory; memory idle for others |
| `--cpus-per-task` | the program's threads share fewer cores and run slower | idle cores, low efficiency in `seff` |
| `--gres=gpu:1` or `--gpus=1` | no GPU visible to the program | GPUs are the scarcest resource; long waits |

A program uses only as many cores as it is told to: requesting 8 cores and running `minimap2` with its default of 3 **threads** wastes 5. Pass `$SLURM_CPUS_PER_TASK` to the program's thread option, and set `OMP_NUM_THREADS` (and the corresponding variables for **BLAS** libraries) to the same number for programs that use OpenMP threads.

### 11.3.4. Job Arrays and Dependencies

Most bioinformatics work consists of the same steps applied to many samples.

**Definition 11.3.3 (Job Array)** A **job array** is a set of batch jobs submitted together from one script, each identical except for its *array index*, which the script reads from the environment variable `SLURM_ARRAY_TASK_ID` to select its input. `--array=1-96%20` creates 96 array tasks of which at most 20 run at the same time.

```bash
#!/bin/bash
#SBATCH --job-name=align
#SBATCH --array=1-96%20
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x_%A_%a.out    # %A = array job ID, %a = array index

set -euo pipefail
# line N of samples.txt holds the name of sample N
sample=$(sed -n "${SLURM_ARRAY_TASK_ID}p" samples.txt)
minimap2 -t "$SLURM_CPUS_PER_TASK" -a ref/genome.fa "fastq/${sample}.fq.gz" \
    | samtools sort -@ 2 -o "results/${sample}.sorted.bam"
```

Steps that depend on each other are chained with dependencies: `sbatch --dependency=afterok:12345 merge.sh` starts `merge.sh` only after job 12345 (all tasks of an array) has completed successfully; `afterany` waits for any outcome, and `--parsable` makes `sbatch` print just the job ID for use in scripts (`jid=$(sbatch --parsable align.sh)`). Chaining more than a few steps this way quickly becomes unmanageable, which is what workflow managers solve (§11.6).

### 11.3.5. How Slurm Decides What Runs

The scheduler orders pending jobs by priority and starts the highest-priority job when its resources become free. Slurm's *multifactor* priority is a weighted sum of factors: the job's age in the queue, its size, its partition and QOS, and most importantly *fair share*.

**Definition 11.3.4 (Fair-Share Scheduling)** **Fair-share scheduling** assigns priorities to jobs so that, over time, each account (a user, a group, a project) receives a share of the cluster proportional to its allocation: the priority of an account's jobs decreases with its recent usage relative to its share, where past usage is weighted by an exponential decay with a half-life of typically one to two weeks.

This is the proportional-share idea of CPU scheduling ([4.11.3](/4.11.3)) applied to whole machines over weeks: a group that has used much of the cluster recently waits longer, and a group that has been idle starts quickly. Strict priority order would waste resources while a large high-priority job waits for enough nodes to become free, so Slurm also backfills.

**Definition 11.3.5 (Backfill Scheduling)** **Backfill scheduling** lets a lower-priority job start out of priority order if it fits in resources that are currently idle and, according to the time limits of the running and pending jobs, it will finish before the time at which the resources it uses are reserved for a higher-priority job; it therefore never delays the expected start of any higher-priority job.

**Example 11.3.1** A partition has 8 cores. Job A runs on 6 cores until hour 4. Waiting, in priority order, are B (8 cores, 2 h), C (2 cores, 3 h) and D (2 cores, 6 h). B cannot start before hour 4, when A ends, so it gets a reservation for hours 4–6. Two cores are idle until then. C fits in them and, by its time limit, ends at hour 3, before B's reservation, so the backfill scheduler starts it at once; D would run until hour 6 on cores that B needs at hour 4, so it must wait. The completion times change from B 6, C 9, D 12 to C 3, B 6, D 12: C finishes six hours earlier and nobody is delayed.

![Gantt charts of Example 11.3.1 on 8 cores. Top: jobs start strictly in priority order, and two cores stay idle for the first four hours. Bottom: with backfill, job C starts immediately in the idle cores and finishes before job B's reservation at hour 4 (dashed line).](./plots/backfill-schedule.py)

Backfilling depends on time limits: the scheduler knows only the requested `--time`, not the true run time. Accurate time limits therefore get jobs started sooner, and a job that requests the partition's maximum of several days by default is backfilled almost never.

## 11.4. Parallel Jobs

A job can use parallelism in several ways, which correspond to different resource requests:

| Kind | Mechanism | Slurm request | Examples |
|---|---|---|---|
| multithreaded, one node | threads sharing memory: pthreads, OpenMP, a tool's `-t`/`--threads` option | `--ntasks=1 --cpus-per-task=N` | aligners (BWA, minimap2, STAR), `samtools sort -@` |
| independent tasks | separate processes, no communication | job array, or one job running several processes | per-sample steps, parameter scans, bootstrap replicates |
| multi-process, many nodes | message passing with MPI: processes on different nodes communicate over the interconnect | `--ntasks=N` (and `--nodes`), launched with `srun` | molecular dynamics (GROMACS), large phylogenetics (RAxML-NG, IQ-TREE MPI builds), climate models |
| GPU | thousands of GPU threads on one or more GPUs | `--gpus=N` or `--gres=gpu:N`, plus CPU cores to feed them | deep learning, base calling of nanopore data, GPU molecular dynamics, AlphaFold-type structure prediction |

**Definition 11.4.1 (MPI)** The **Message Passing Interface** (MPI) is a standardized library interface for parallel programs that consist of many processes with separate address spaces, which cooperate by sending and receiving messages (point-to-point operations such as send and receive, and collective operations such as broadcast and reduction). Implementations include Open MPI and MPICH; an MPI program is started as many processes at once, on a cluster with `srun`.

Most bioinformatics tools are multithreaded programs for one node, and most analyses consist of many independent tasks; MPI matters mainly for simulation codes. Two rules of thumb follow from the previous chapters. A multithreaded tool does not scale indefinitely: by **Amdahl's law** ([4.4.7](/4.4.7#sec-7.4.4)) a tool whose serial part is 10 % cannot run more than 10 times faster on any number of cores, and I/O or memory bandwidth often limits it earlier, so measuring the speed-up at 4, 8 and 16 cores before requesting 64 is worthwhile. And many independent tasks are best expressed as a job array or by a workflow manager, as an **embarrassingly parallel** problem ([4.4.7](/4.4.7)): 96 jobs with 8 cores each usually finish sooner, because they fit into gaps in the schedule, than one job with 768 cores, and a failure affects only one sample.

## 11.5. Moving and Protecting Data

Sequencing data arrive by the terabyte, and moving them is a task of its own. At the full speed of a 1-Gbit/s connection, 1 TB takes $8 \times 10^{12}\,\mathrm{bit} / 10^{9}\,\mathrm{bit/s} = 8000\,\mathrm{s} \approx 2.2$ hours; at a realistic 100 Mbit/s over the internet, about a day. The tools, from small to large transfers:

| Tool | Use |
|---|---|
| `scp file cluster:dir/` | copy a few files over SSH |
| `rsync -avP src/ cluster:dst/` | synchronize directories over SSH: transfers only files that differ, resumes interrupted transfers |
| `wget`, `curl -O`, `aria2c` | download from web or FTP servers (public data, reference genomes) |
| SRA Toolkit (`prefetch`, `fasterq-dump`), ENA downloads | fetch public sequencing runs by accession |
| Globus | managed, parallel, restartable transfers between institutions' data transfer nodes; the standard for terabyte-scale movement |

`rsync` deserves to be learned well. `-a` (archive) preserves the **directory tree**, times and permissions; `-v` lists what is transferred; `-P` keeps partial files and shows progress; `-n` (`--dry-run`) shows what would happen; `--delete` removes files from the destination that are no longer in the source (dangerous: always dry-run first). A trailing slash on the source matters: `rsync -a data/ dst/` copies the contents of `data` into `dst`, while `rsync -a data dst/` creates `dst/data`. By default rsync decides whether a file differs by its size and mtime; `--checksum` compares contents. Large transfers should go through the cluster's data transfer nodes rather than the login nodes, and in `tmux` so that a dropped connection does not interrupt them ([4.11.10](/4.11.10#sec-10.7.2)).

A transfer is complete only when it is verified. Sequencing facilities and public archives publish checksums (MD5 or SHA-256) of their files:

```bash
md5sum *.fq.gz > checksums.md5        # on the source: record checksums
md5sum -c checksums.md5               # on the destination: verify, printing OK or FAILED per file
```

Raw data that cannot be regenerated deserve the most care: keep them read-only (`chmod -R a-w raw/`), never modify them in place (every analysis reads them and writes elsewhere), keep at least one copy outside the cluster's scratch file system (which is purged and not backed up), and archive them, with their checksums and metadata, to tape or a public repository at the end of a project. Compress text formats (gzip or, better for random access, BGZF), and prefer the compressed binary formats of the field (BAM or CRAM instead of SAM).

## 11.6. Workflow Managers

### 11.6.1. Why

An analysis of a sequencing experiment is a sequence of steps (quality control, trimming, alignment, sorting, counting, statistics), each applied to every sample, with dependencies between steps. Shell scripts and chains of `sbatch --dependency` express this poorly: they rerun everything after a failure, do not know which outputs are out of date after a parameter change, and hard-code the cluster's details.

**Definition 11.6.1 (Workflow Management System)** A **workflow management system** executes an analysis described as a set of steps with declared inputs and outputs. From these declarations it derives a **directed acyclic graph** of tasks, runs each task when its inputs are available, in parallel where the graph allows, on a local machine, a cluster or a cloud; reruns only the tasks whose outputs are missing or out of date; provides each task with its software environment; and records what was run.

The idea is that of `make` and other **build systems** ([4.2.2](/4.2.2#sec-2.6)) applied to data analysis, with cluster execution, software environments and provenance added. In bioinformatics two systems dominate: Snakemake, a Python-based language in which rules are defined by file-name patterns and the graph is inferred backward from the requested outputs, as in `make`; and Nextflow, a dataflow language in which processes are connected by channels and data flow forward through them. Others include the Common Workflow Language (CWL) and WDL, standard descriptions used by large consortia and cloud platforms.

### 11.6.2. Snakemake

A Snakemake workflow is a `Snakefile` of rules:

```python
SAMPLES = ["ctrl_1", "ctrl_2", "treat_1", "treat_2"]


rule all:
    input:
        expand("results/{sample}.sorted.bam.bai", sample=SAMPLES),


rule align:
    input:
        ref="ref/genome.fa",
        reads="fastq/{sample}.fq.gz",
    output:
        "results/{sample}.sorted.bam",
    threads: 8
    resources:
        mem_mb=16000,
        runtime=120,                    # minutes
    conda:
        "envs/align.yaml"
    log:
        "logs/align/{sample}.log",
    shell:
        "(minimap2 -t {threads} -a {input.ref} {input.reads}"
        " | samtools sort -@ 2 -o {output}) 2> {log}"


rule index:
    input:
        "results/{sample}.sorted.bam",
    output:
        "results/{sample}.sorted.bam.bai",
    shell:
        "samtools index {input}"
```

Snakemake starts from the target, the input of the first rule `all`: four `.bai` files. Each file name is matched against the output patterns of the rules; the wildcard `{sample}` takes the value that makes the pattern match (`ctrl_1`, …), which determines the rule's inputs, and so on backward until existing files are reached. The resulting graph has eight jobs. A job runs if its output is missing or older than its inputs (and, by default, also when the rule's code, parameters or software environment changed). Typical invocations:

```bash
snakemake -n                                   # dry run: list the jobs that would run
snakemake --cores 8 --sdm conda                # run locally on 8 cores, creating conda envs per rule
snakemake --executor slurm --jobs 50 --sdm apptainer \
    --default-resources slurm_partition=standard    # submit each job to Slurm, at most 50 at a time
snakemake --dag | dot -Tsvg > dag.svg          # draw the graph
```

With the Slurm executor plugin (Snakemake 8 and later), each job becomes a Slurm job whose resource requests come from the rule's `threads` and `resources`; the Snakemake process itself is light and runs in `tmux` on the login node or as a small long-running job. Site-specific options are collected in a *profile* (a YAML file), so that the workflow itself stays portable.

### 11.6.3. Nextflow

The same alignment in Nextflow, with the strict syntax that is the default since Nextflow 26.04:

```text
params.reads = "fastq/*.fq.gz"
params.ref   = "ref/genome.fa"

process ALIGN {
    tag "${sample}"
    cpus 8
    memory '16 GB'
    time '2h'
    conda 'bioconda::minimap2=2.28 bioconda::samtools=1.21'

    input:
    tuple val(sample), path(reads)
    path ref

    output:
    tuple val(sample), path("${sample}.sorted.bam")

    script:
    """
    minimap2 -t ${task.cpus} -a ${ref} ${reads} | samtools sort -o ${sample}.sorted.bam
    """
}

workflow {
    reads = channel.fromPath(params.reads).map { f -> tuple(f.simpleName, f) }
    ALIGN(reads, file(params.ref))
}
```

A process declares inputs and outputs; the workflow block connects processes with *channels*, queues of values (here pairs of a sample name and a file) that flow forward. Each task runs in its own work directory, and `-resume` reuses the results of tasks whose inputs and script are unchanged (a cache keyed by hashes). The execution platform is chosen in `nextflow.config`, typically through profiles:

```text
profiles {
    slurm {
        process.executor = 'slurm'
        process.queue    = 'standard'
    }
    apptainer {
        apptainer.enabled = true
    }
}
```

`nextflow run main.nf -profile slurm,apptainer -resume` then submits every task as a Slurm job inside a container. The nf-core community maintains peer-reviewed Nextflow pipelines for standard analyses, such as `nextflow run nf-core/rnaseq -profile apptainer --input samplesheet.csv --outdir results --genome GRCh38`, with configuration profiles for many institutional clusters; for a standard analysis, using such a pipeline is usually better than writing one.

| | Snakemake | Nextflow |
|---|---|---|
| Language | Python with rule syntax | Groovy-based DSL (strict syntax since 26.04) |
| Model | rules matched by file-name patterns; graph inferred backward from targets | processes connected by channels; data flow forward |
| Rerun decision | missing or outdated outputs (mtime, code, parameters, environment) | task hash of inputs and script (`-resume`) |
| Ecosystem | Snakemake workflow catalog, wrappers | nf-core pipelines and modules |
| Feels natural for | people who think in files and Python; exploratory, custom analyses | standardized, large-scale production pipelines and clouds |

## 11.7. Good Practice

- Develop small, scale late: test every step on a subset of the data (a few thousand reads, one chromosome) interactively or with a short job, then scale up with measured resource requests.
- Keep code, environments and data apart: code in a version-controlled repository (`git`), environments in lock files or images, raw data read-only in project space, intermediate files on scratch, results with the code that produced them.
- Make every result reproducible from scratch: a workflow, a pinned environment (conda lock file or container digest), the reference versions and the parameters together determine the output; record them, and the workflow manager's logs, with the results.
- Respect shared resources: no computation on login nodes, no thousands of tiny jobs (use arrays or a workflow manager with grouping), no millions of tiny files on parallel file systems, accurate resource requests, and clean up scratch.
- Expect failures: nodes fail, jobs hit time limits, transfers are interrupted. Steps that write their output under a temporary name and rename it at the end ([4.11.7](/4.11.7#sec-7.4.5)), workflow managers that rerun only what is missing, checksums and backups turn failures into delays rather than losses.

## Summary

- A cluster consists of shared login nodes, compute nodes allocated by a workload manager, a fast interconnect, and several file systems: backed-up home and project space, fast but purged parallel scratch, node-local disks and archives. Parallel file systems excel at large sequential I/O and suffer under many small files.
- Software comes from environment modules (Lmod, built with Spack or EasyBuild), conda/pixi environments and Apptainer containers.
- A batch job is a script with a resource request (`--cpus-per-task`, `--mem`, `--time`, `--gpus`), submitted with `sbatch`, monitored with `squeue` and `sacct`, confined by cgroups. Job arrays handle many samples; dependencies chain steps.
- Slurm orders jobs by multifactor priority dominated by fair share, and backfills lower-priority jobs into idle resources when their time limits guarantee that no higher-priority job is delayed; accurate time limits shorten waiting.
- Threads within a node, independent tasks, MPI across nodes and GPUs require different requests; Amdahl's law limits threaded speed-ups, and independent tasks scale best as arrays.
- Move data with `rsync` and Globus, verify them with checksums, keep raw data read-only and backed up outside scratch.
- Workflow managers (Snakemake, Nextflow) build a directed acyclic graph of tasks from declared inputs and outputs, run them in parallel on a cluster with per-step software environments, and rerun only what changed; nf-core provides standard pipelines.
