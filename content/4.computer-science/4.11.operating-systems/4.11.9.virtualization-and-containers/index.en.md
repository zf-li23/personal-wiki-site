---
title: Virtualization and Containers
description: "Running one operating system inside another and isolating applications within one kernel: virtual machines and hypervisors, the Popek–Goldberg condition, trap-and-emulate, binary translation, paravirtualization and hardware support, memory and I/O virtualization, WSL 2 as a worked example; Linux containers built from namespaces, cgroups and layered file systems; Docker, OCI images and Podman; Apptainer for clusters; and how to choose between them for reproducible scientific software."
---

The previous chapters described how an **operating system** virtualizes the CPU and memory for processes, so that each process believes it owns the machine. This chapter applies the same idea one level up. A *virtual machine* gives a whole operating system the illusion of owning the hardware, so that Linux can run on a Windows laptop or dozens of servers on one physical host; a *container* gives a group of processes the illusion of owning the operating system, with their own files, process tree and network, while sharing one kernel. Both are everyday tools in computational biology: WSL 2 is a virtual machine, a bioinformatics tool is often distributed as a Docker image, and on a cluster the same image runs through Apptainer. The chapter builds on **limited direct execution** and privilege levels ([4.11.1](/4.11.1), [4.11.2](/4.11.2)), on **address translation** ([4.11.4](/4.11.4)) and on the **file systems** of [4.11.7](/4.11.7); the practical use of containers on servers continues in [4.11.11](/4.11.11).

## 9.1. Virtual Machines

### 9.1.1. Definitions

**Definition 9.1.1 (Virtual Machine and Hypervisor)** A **virtual machine** (VM) is an efficient, isolated duplicate of a real machine, on which an unmodified operating system, the *guest*, can run. It is provided by a **hypervisor**, or virtual machine monitor (VMM), a layer of software that controls the real hardware and multiplexes it among virtual machines. A *type 1* (bare-metal) hypervisor runs directly on the hardware; a *type 2* (hosted) hypervisor runs as an application on a *host* operating system.

The definition, due to Popek and Goldberg (1974), contains three requirements: *equivalence* (a program behaves on the VM as on the real machine, apart from timing and resource availability), *resource control* (the hypervisor is in complete control of the hardware; a guest cannot access resources not allocated to it), and *efficiency* (the great majority of instructions run directly on the CPU, without the hypervisor's intervention). The last requirement distinguishes virtualization from emulation: QEMU can emulate an ARM processor on an x86 machine by interpreting each instruction, but this is tens of times slower.

| | Type 1 | Type 2 |
|---|---|---|
| Runs on | the hardware | a host OS |
| Examples | Xen, VMware ESXi, Microsoft Hyper-V; KVM (a Linux kernel module that turns Linux itself into a hypervisor) | VirtualBox, VMware Workstation, Parallels, QEMU without KVM |
| Typical use | servers, clouds | desktops |

The boundary is blurred in practice. With Hyper-V enabled, Windows itself runs as a privileged guest (the "root partition") on top of the hypervisor, and WSL 2 is another guest beside it (§9.3); with KVM, a Linux host is both an ordinary operating system and a type 1 hypervisor. The motivations are the same as in the 1960s, when IBM invented virtual machines for its mainframes: *consolidation* (many lightly loaded servers on one machine), *isolation* (a crash or a compromise in one VM does not affect the others), encapsulation (a VM is a set of files that can be copied, snapshotted and migrated, even while running), and running software that needs a different OS.

### 9.1.2. When Can a CPU Be Virtualized?

The natural way to run a guest kernel efficiently is limited direct execution once more: run the guest kernel in **user mode**, let its ordinary instructions execute directly, and let every **privileged instruction** trap to the hypervisor, which emulates its effect on the virtual machine's state. This is *trap-and-emulate*. It works only if every instruction that could reveal or change the real machine's state traps.

**Definition 9.1.2 (Sensitive and Privileged Instructions)** A **privileged instruction** is one that traps when executed in user mode and executes normally in kernel mode. A **sensitive instruction** is one that reads or changes the configuration of the machine's resources (control-sensitive: for example, changing the page-table base register or the interrupt-enable flag) or whose behavior depends on that configuration (behavior-sensitive: for example, reading the current privilege level).

**Theorem 9.1.1 (Popek–Goldberg Theorem)** For a conventional computer with user and kernel modes and relocatable memory, a virtual machine monitor satisfying equivalence, resource control and efficiency can be constructed if the set of sensitive instructions is a subset of the set of privileged instructions.

The classic x86 architecture violated the condition: about 17 instructions were sensitive but not privileged. The best-known is `popf`, which loads the flags register; in user mode it silently ignores the interrupt-enable bit instead of trapping, so a guest kernel that disables interrupts with `popf` would not be noticed by the hypervisor. `sgdt` and similar instructions let user code read the locations of the real descriptor tables. x86 could therefore not be virtualized by trap-and-emulate, and three techniques were developed around this.

### 9.1.3. Binary Translation, Paravirtualization and Hardware Support

*Binary translation* (VMware, 1999): the hypervisor scans the guest kernel's code before it runs, block by block, and replaces sensitive instructions by calls into the hypervisor, caching the translated code. User-level code of the guest, which contains no sensitive instructions, runs unmodified. This made x86 virtualization practical and commercial.

*Paravirtualization* (Xen, 2003): the guest kernel is modified to know that it runs on a hypervisor. Instead of executing sensitive instructions, it calls the hypervisor directly through *hypercalls*, a hypervisor's analogue of **system calls**, and it cooperates on memory management and I/O. It avoids the cost of translation but requires a modified guest. Paravirtualization survives today mainly in **device drivers** (§9.2.4) and in "enlightenments" through which guests cooperate with Hyper-V or KVM for timers and interrupts.

*Hardware-assisted virtualization* (Intel VT-x, 2005; AMD-V, 2006; similar extensions on ARM and RISC-V): the CPU gains a new mode. On x86 there is *VMX root* operation for the hypervisor and *non-root* operation for guests, each with its own rings 0–3, so the guest kernel runs in ring 0 of non-root mode, as it expects. A control structure in memory (the VMCS) specifies which events cause a *VM exit*, a transfer of control to the hypervisor (privileged instructions, access to certain registers, external interrupts, I/O); after handling it, the hypervisor resumes the guest with a *VM entry*. This makes the architecture satisfy the Popek–Goldberg condition in spirit, and it is what all current hypervisors rely on. A VM exit costs on the order of a microsecond, so the remaining work of hypervisor design is to avoid exits.

## 9.2. Virtualizing Memory and I/O

### 9.2.1. Two Levels of Address Translation

A guest kernel manages **page tables** that map guest **virtual addresses** to what it believes are **physical addresses**, the *guest physical addresses*. The hypervisor must add a second mapping from guest physical addresses to *host physical addresses*, the real memory locations, because it distributes real memory among VMs.

### 9.2.2. Shadow Page Tables

Without hardware support, the hypervisor maintains for each guest page table a *shadow page table* that maps guest virtual addresses directly to host physical addresses, and points the real **MMU** at the shadow. It write-protects the guest's page tables, so that every modification by the guest traps and the hypervisor can update the shadow accordingly. Address translation then runs at full speed, but every page-table update, **context switch** and page fault in the guest costs exits, which makes process-heavy workloads (compilation, many short processes) slow.

### 9.2.3. Nested Paging

*Nested paging* (Intel's extended page tables, EPT; AMD's nested page tables, NPT) lets the hardware perform both translations. The guest controls its own page tables freely, without exits; the hypervisor maintains a second set of tables from guest physical to host physical addresses; and on a **TLB** miss the page-walk hardware walks both.

**Example 9.2.1 (Cost of a Two-Dimensional Page Walk)** With four-level page tables in both the guest and the host, each of the four guest page-table entries is located by a guest physical address, which must itself be translated by a four-level host walk before it can be read. The final guest physical address of the data needs one more host walk. The number of memory references in the worst case is

$$
\underbrace{4 \cdot 4}_{\text{host walks for guest entries}} + \underbrace{4}_{\text{guest entries}} + \underbrace{4}_{\text{final host walk}} = 24 = (4+1)(4+1) - 1,
$$

compared with 4 without virtualization.

The TLB caches the combined translation, so this cost is paid only on TLB misses, and large pages (2 MiB or 1 GiB) in the host shorten the walks. In practice nested paging is far faster than shadow paging for most workloads, and it is the default everywhere. The hypervisor can also *overcommit* memory, promising guests more than exists, by reclaiming pages through a *balloon driver* in the guest (which allocates memory inside the guest and hands those pages back to the hypervisor), by sharing identical pages between VMs (KSM in Linux), and by swapping.

### 9.2.4. I/O Virtualization

A guest's I/O can be provided in three ways, in order of increasing performance:

| Method | How it works | Performance |
|---|---|---|
| full emulation | the hypervisor emulates a real, well-known device (an IDE disk, an Intel e1000 network card); every access to its registers causes an exit | slow, but any guest has a driver |
| paravirtual devices | the guest uses a driver for an idealized virtual device: *virtio* on KVM and QEMU, VMBus devices on Hyper-V; requests travel through shared-memory queues (*virtqueues*) with few exits | near-native for most uses |
| device passthrough | a physical device, or a virtual function of a device that supports SR-IOV, is assigned directly to the guest, with the IOMMU ([4.11.8](/4.11.8#sec-8.1.3)) confining its **DMA** to the guest's memory | native, but the device is not shared or migrated easily |

The `/proc/interrupts` output in [4.11.8](/4.11.8#sec-8.1.2) shows this from inside a guest: the disk of the WSL 2 VM is a virtio device.

## 9.3. Example: WSL 2

Windows Subsystem for Linux exists in two very different versions, which illustrate two approaches to running Linux software on another OS.

| | WSL 1 (2016) | WSL 2 (2019) |
|---|---|---|
| Approach | translation layer: Linux **system calls** are implemented by a Windows kernel driver | a lightweight virtual machine running a real Linux kernel |
| Linux kernel | none | a Microsoft-built kernel from the upstream long-term branches |
| System-call compatibility | partial (no FUSE, limited `ptrace`, no kernel modules, no Docker) | complete |
| Linux file system | stored as NTFS files | ext4 in a virtual disk file (`ext4.vhdx`) |
| Access to Windows files | fast | through a 9P file server, slow for many small files |
| Memory | shared with Windows | the VM's memory, grown and reclaimed dynamically |

WSL 2 runs on the Hyper-V hypervisor in a *utility VM* that boots in about a second and is managed transparently by Windows; all installed distributions share this VM and its kernel, each in its own set of namespaces (§9.4), which is why `uname` reports the same kernel in all of them:

```text
$ uname -r
6.6.114.1-microsoft-standard-WSL2
```

Several consequences follow from the design. The Linux side has a real kernel, so containers, systemd services, FUSE and GPU computing (through a paravirtual GPU device, `/dev/dxg`, that forwards to the Windows driver) work. Files on the Windows side are reached through the 9P protocol, and file-heavy work should stay in the Linux file system ([4.11.7](/4.11.7#sec-7.5)). The VM is given at most half of the host's memory by default; a large assembly or alignment job may need more, which is set in `%UserProfile%\.wslconfig` (`[wsl2]`, `memory=`, `processors=`, `swap=`). Networking is behind a NAT by default, so a server running inside WSL is reachable from Windows through `localhost` forwarding; the *mirrored* networking mode gives Linux the host's interfaces directly.

## 9.4. Containers

### 9.4.1. The Idea

A virtual machine is a heavy unit of isolation: each VM boots its own kernel, reserves memory and runs its own background services. Often what is needed is lighter: run a program with its own set of libraries and tools, isolated from other programs, without its own kernel.

**Definition 9.4.1 (Container)** A **container** is a group of processes that run on the host's kernel but are isolated from the rest of the system by the kernel itself: they have their own view of the file system, the process tree, the network and other resources, and limits on the resources they may consume. On Linux, containers are built from namespaces (for the views), control groups (for the limits) and a root file system usually assembled from the layers of an image. The technique is also called *OS-level virtualization*.

A process in a container is an ordinary Linux process; `ps` on the host shows it. There is no hypervisor and no second kernel, so a container starts in milliseconds, runs at native speed and costs only the memory its processes use. The price is weaker isolation: all containers share one kernel, so a kernel vulnerability can let a process escape, and a container can only run programs for the host's kernel (Linux containers on Windows or macOS run inside a Linux VM, as Docker Desktop does with WSL 2).

### 9.4.2. Namespaces

**Definition 9.4.2 (Linux Namespace)** A **Linux namespace** wraps a global system resource so that the processes inside the namespace see their own isolated instance of it; changes to the resource are visible to members of the namespace and invisible to other processes. Every process belongs to one namespace of each type, and new namespaces are created with the system calls `clone`, `unshare` and `setns`.

| Namespace | Isolates | Effect inside |
|---|---|---|
| mount | the list of mount points | own file-system tree; the basis of a container's root file system |
| PID | process IDs | the first process has PID 1 and sees only processes of its namespace |
| network | interfaces, routing tables, ports, firewall rules | own network stack, usually connected to the host by a virtual Ethernet pair |
| UTS | host name and domain name | own host name |
| IPC | System V IPC objects, POSIX message queues | own shared-memory segments and semaphores |
| user | user and group IDs, capabilities | a process can be root (UID 0) inside while being an ordinary user outside |
| cgroup | the view of the cgroup hierarchy | sees its own cgroup as the root |
| time | the boot-time and monotonic clocks | own clock offsets (useful for migrating containers) |

The user namespace is what makes *rootless* containers possible: an unprivileged user creates a user namespace in which their UID is mapped to 0, and inside it they may create the other namespaces. The `unshare` command does this from the shell. Here an ordinary user starts a shell in new user, PID, UTS, network and mount namespaces (with a fresh `/proc` so that `ps` sees only the new PID namespace):

```bash
echo "host: $(hostname), pid $$, user $(id -un)"
unshare --user --map-root-user --pid --fork --mount-proc --uts --net sh -c '
  hostname sandbox
  echo "inside: $(hostname), pid $$, user $(id -un)"
  ps -o pid,user,cmd
  ip -brief link'
```

```text
host: LAPTOP-J59DFHQK, pid 27080, user zf-li23
inside: sandbox, pid 1, user root
    PID USER     CMD
      1 root     sh -c hostname sandbox; echo "inside: $(hostname), pid $$, user $(id -un)"; ps -o pid,user,cmd; ip -brief link
      5 root     ps -o pid,user,cmd
lo               DOWN           00:00:00:00:00:00 <LOOPBACK>
```

Inside, the shell is PID 1 and "root", has its own host name, and sees only its own processes and a network namespace that contains nothing but a disconnected loopback interface. Outside, nothing changed: the host name is the same, and the "root" inside has exactly the rights of user `zf-li23` on the host's files. A container runtime does the same, plus a new root file system and resource limits. The namespaces of a process are visible as links in `/proc/<pid>/ns/`.

### 9.4.3. Control Groups

**Definition 9.4.3 (Control Group)** A **control group** (cgroup) is a set of processes organized in a hierarchy, to which the kernel applies resource limits and accounting through *controllers*: CPU time (`cpu`), memory (`memory`), block I/O (`io`), number of processes (`pids`), CPU and memory-node placement (`cpuset`) and others. In cgroup version 2 (the unified hierarchy, the default on all current distributions) every process belongs to exactly one cgroup, and the hierarchy is exposed as a file system at `/sys/fs/cgroup`, where limits are set by writing to files such as `memory.max` and `cpu.max`.

The controllers available on the machine used here, and two experiments through `systemd-run`, which starts a command in a new cgroup with the given limits:

```text
$ cat /sys/fs/cgroup/cgroup.controllers
cpuset cpu io memory hugetlb pids rdma
```

```bash
# a Python process that allocates 10 MiB at a time, with a 100 MiB memory limit
systemd-run --user --scope -p MemoryMax=100M -p MemorySwapMax=0 python3 -c "
a = []
for i in range(1, 40):
    a.append(bytearray(10 * 1024 * 1024)); print(i * 10, 'MiB', flush=True)
" | tail -2
echo "exit status: ${PIPESTATUS[0]}"

# a busy loop for 3 s of wall time, limited to half a CPU
systemd-run --user --scope -p CPUQuota=50% sh -c '
  d=/sys/fs/cgroup$(cut -d: -f3 /proc/self/cgroup)
  cat $d/cpu.max
  timeout 3 sh -c "while :; do :; done"
  grep -E "usage_usec|throttled_usec" $d/cpu.stat'
```

```text
80 MiB
90 MiB
exit status: 137
50000 100000
usage_usec 1513501
throttled_usec 1715944
```

When the group's memory would exceed 100 MiB, the kernel's **out-of-memory killer** kills the process with `SIGKILL` (exit status $128 + 9 = 137$), without affecting anything outside the group. The CPU limit `50000 100000` means 50 ms of CPU time per 100 ms period; the busy loop got 1.5 s of CPU in 3 s and was throttled the rest of the time. Exit status 137 and "Killed" are exactly what a cluster job that exceeds its memory request experiences ([4.11.11](/4.11.11#sec-11.3)): Slurm, systemd, Docker and Kubernetes all enforce their limits with cgroups.

### 9.4.4. Images and Layered File Systems

A container needs a root file system with the program and all its libraries. It comes from an image.

**Definition 9.4.4 (Container Image)** A **container image** is a read-only, portable package of a root file system, organized as an ordered stack of *layers* (each layer a tar archive of the files added, changed or deleted relative to the layers below it), together with metadata: the default command, environment variables, working directory and the target architecture. Images are identified by a content hash (a *digest*) and distributed through *registries*.

At run time, the layers are combined by a union file system, usually OverlayFS, which presents a merged view of a stack of read-only *lower* directories and one writable *upper* directory. Reads find the topmost version of a file; the first write to a file from a lower layer copies it into the upper layer (**copy-on-write**); deletions are recorded as special "whiteout" files. An unprivileged user can try it inside a user and mount namespace:

```bash
mkdir lower upper work merged
echo base > lower/a.txt
unshare --user --map-root-user --mount sh -c '
  mount -t overlay overlay -o lowerdir=lower,upperdir=upper,workdir=work merged
  echo changed > merged/a.txt
  echo new > merged/b.txt
  cat merged/a.txt; ls merged'
echo "lower:"; cat lower/a.txt
echo "upper:"; ls upper
```

```text
changed
a.txt
b.txt
lower:
base
upper:
a.txt
b.txt
```

The lower directory is untouched; all changes went into the upper directory. Because layers are shared, a hundred containers started from the same image use one copy of its files on disk and in the **page cache**, and an image that differs from another only in its top layer costs only that layer to download.

Two further mechanisms complete a container's isolation. *Capabilities* split the power of root into about 40 separate privileges (binding to low ports, changing file ownership, loading kernel modules, and so on), most of which a container's "root" does not get. *seccomp* filters restrict which system calls the processes may make at all, which reduces the kernel surface exposed to an attack.

## 9.5. Docker, OCI and Podman

Docker (2013) did not invent any of the kernel features above (cgroups and most namespaces were in Linux by 2008, user namespaces were completed in 2013, and earlier systems such as FreeBSD jails and Solaris zones had the same idea); it made them usable, with a simple file format to build images, a registry to share them and a command-line tool to run them. Its formats became open standards of the Open Container Initiative (OCI): the *image specification*, the *runtime specification* (how to run a container from an unpacked image; reference implementation `runc`, with `crun` a faster alternative) and the *distribution specification* (the registry protocol). Any OCI image runs under any OCI tool.

An image is built from a `Dockerfile`, whose instructions each produce a layer:

```text
# Pin the base image; tags can be moved, so production builds pin the digest too
FROM mambaorg/micromamba:2.0.5

# Install tools from conda-forge and bioconda into the base environment
RUN micromamba install -y -n base -c conda-forge -c bioconda \
        samtools=1.21 minimap2=2.28 python=3.12 \
    && micromamba clean --all --yes

WORKDIR /data
ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]
CMD ["samtools", "--version"]
```

```bash
docker build -t aligner:1.0 .          # build an image from the Dockerfile in .
docker run --rm aligner:1.0            # run its default command, remove the container afterwards
docker run --rm -v "$PWD":/data aligner:1.0 \
    minimap2 -a ref.fa reads.fq -o out.sam   # bind-mount the current directory at /data
docker images; docker ps -a            # list images and containers
```

Often no Dockerfile is needed at all: the BioContainers project automatically builds an image for every Bioconda package and publishes it at `quay.io/biocontainers/<tool>:<version>--<build>`.

The Docker architecture has a weakness for shared machines. The `docker` command talks to a daemon, `dockerd`, that runs as root, and any user allowed to use it can **mount** the host's root directory into a container and modify it: membership in the `docker` group is equivalent to root. *Podman* (Red Hat) provides the same command-line interface without a daemon and runs *rootless* by default, using user namespaces, so that a container has no more rights than the user who starts it. Docker can also run rootless, and Kubernetes, which orchestrates containers across many machines, uses OCI runtimes through containerd or CRI-O.

## 9.6. Apptainer on Clusters

High-performance computing clusters do not allow Docker: users must not obtain root, jobs are started by a batch scheduler rather than a daemon, and the file systems and fast networks of the cluster must remain accessible inside the container. *Apptainer* (formerly Singularity; renamed in 2021 when the project joined the Linux Foundation, with Sylabs' fork continuing as SingularityCE) was designed for this setting:

- a container runs as the user who starts it, with that user's identity and permissions, and with no daemon;
- by default it is integrated with the host rather than isolated from it: the home directory, the current directory and `/tmp` are bind-mounted, the host's network is used, and other paths are added with `--bind`; `--containall` gives stronger isolation when needed;
- an image is a single file in the *Singularity Image Format* (SIF), a compressed read-only SquashFS file system, which is easy to copy, archive with a project and place on a parallel file system, and which many processes on many nodes can read at once;
- it runs OCI images directly (converting them to SIF), and GPU support is one flag (`--nv` for NVIDIA, `--rocm` for AMD).

```bash
apptainer pull samtools.sif docker://quay.io/biocontainers/samtools:<version>--<build>
apptainer exec samtools.sif samtools view -c sample.bam     # run one command in the image
apptainer shell samtools.sif                                # interactive shell inside
apptainer exec --nv pytorch.sif python train.py             # with the host's NVIDIA GPUs
apptainer exec --bind /scratch/$USER:/work tools.sif ls /work
```

Images can also be built from a definition file, which plays the role of a Dockerfile:

```text
Bootstrap: docker
From: mambaorg/micromamba:2.0.5

%post
    micromamba install -y -n base -c conda-forge -c bioconda samtools=1.21
    micromamba clean --all --yes

%environment
    export PATH=/opt/conda/bin:$PATH

%runscript
    exec samtools "$@"
```

`apptainer build tools.sif tools.def` builds it, without root on systems configured for unprivileged user namespaces (`--fakeroot`). Workflow managers such as Snakemake and Nextflow can pull and use such images automatically for each step of a pipeline ([4.11.11](/4.11.11#sec-11.6)).

## 9.7. Choosing an Isolation Mechanism

| | Virtual machine | Container (Docker, Podman) | Apptainer | Conda/pixi environment ([4.4.1](/4.4.1)) |
|---|---|---|---|---|
| What is isolated | the whole OS, including the kernel | file system, processes, network, resources | file system (mainly) | libraries and tools only, by `PATH` and prefixes |
| Kernel | own | host's | host's | host's |
| Start-up time | seconds | milliseconds | milliseconds | instant |
| Overhead | memory for the guest OS; small CPU overhead | almost none | almost none | none |
| Needs root to run | for the hypervisor | daemon or user namespaces | no | no |
| Reproducibility | the whole system can be archived | an image digest fixes every file | a SIF file fixes every file | lock file fixes package versions, but the OS and system libraries vary |
| Typical use | another OS (WSL 2), strong multi-tenant isolation, clouds | services, development, distributing tools | clusters | everyday development |

For computational work, the levels combine. A conda or pixi environment with a **lock file** is the lightest way to fix the versions of the tools in a project; an image fixes the entire user-space software stack, including the C library and system packages, and is the unit that a pipeline or a paper's supplementary material can reference by digest. Neither fixes the kernel or the hardware, and results that depend on the CPU's floating-point behavior or on GPU libraries can still differ across machines ([3.5](/3.5)); a VM or the same cluster is needed when even that matters.

## Summary

- A hypervisor runs guest operating systems on virtual machines that satisfy equivalence, resource control and efficiency. Trap-and-emulate works when every sensitive instruction is privileged (Popek–Goldberg); x86 needed binary translation or paravirtualization until VT-x and AMD-V added a separate mode for guests with VM exits.
- Memory virtualization adds a second translation from guest physical to host physical addresses: shadow page tables in software or nested paging (EPT/NPT) in hardware, whose worst-case walk takes 24 memory references with four levels. I/O is emulated, paravirtualized (virtio) or passed through with an IOMMU.
- WSL 2 is a lightweight Hyper-V VM running a real Linux kernel, with ext4 in a virtual disk and Windows files reached over 9P.
- A container is a group of ordinary processes isolated by namespaces (mount, PID, network, UTS, IPC, user, cgroup, time), limited by cgroups (cgroup v2 at `/sys/fs/cgroup`), and started on a root file system assembled by OverlayFS from the layers of an image; capabilities and seccomp narrow what it can do.
- Docker made containers practical; OCI standardized images, runtimes and registries; Podman runs them rootless without a daemon. On clusters, Apptainer runs OCI images as single SIF files with the user's own identity.
- Environments fix package versions, images fix the whole user space, VMs fix the OS; reproducible analyses pin images by digest.
