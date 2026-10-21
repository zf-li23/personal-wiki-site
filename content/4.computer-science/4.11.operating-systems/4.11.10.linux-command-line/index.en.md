---
title: The Linux Command Line
description: "Working in a Unix shell: commands, arguments and the PATH; navigating the file system, globbing and quoting; standard streams, redirection and pipelines with the classic text tools (grep, sed, awk, sort, cut, xargs, find); users, groups and permission bits; processes, signals and job control; environment variables and configuration files; remote work with ssh and tmux; and writing robust Bash scripts."
---

Most bioinformatics software is developed for Linux and used from the command line: aligners, variant callers and assemblers are command-line programs, the servers and clusters on which they run have no graphical interface, and the glue between tools is a pipeline of commands or a shell script. The command line is also where the operating-system concepts of the previous chapters become directly visible: every command is a **process** created by `fork` and `exec` ([4.11.2](/4.11.2)), every redirection rearranges **file descriptors** ([4.11.8](/4.11.8#sec-8.5.3)), and permissions are fields of the **inode** ([4.11.7](/4.11.7#sec-7.1.3)). This chapter teaches the shell Bash, the default on **Linux distributions** and clusters, with GNU tools as found on Ubuntu (in WSL 2 or on a server). macOS ships zsh and BSD versions of the tools, which differ in some options. Examples were run with Bash 5.2 on Ubuntu 24.04; the `$` at the start of a line is the prompt and is not typed.

## 10.1. Shells and Commands

### 10.1.1. Terminal, Shell and Commands

Three programs cooperate when we "use the command line". A *terminal emulator* (Windows Terminal, GNOME Terminal, the terminal panel of VS Code) displays characters and sends keystrokes. It is connected through a pseudo-terminal device to the shell.

**Definition 10.1.1 (Shell)** A **shell** is a program that reads commands, interactively from a terminal or from a script, and executes them: it expands the command line (variables, wildcards, quotes), sets up redirections and pipes, starts programs as child processes and waits for them, and offers a programming language with variables, control flow and functions. Common shells are Bash (the GNU Bourne-again shell), zsh, fish and the minimal POSIX `sh` (on Ubuntu, `dash`).

A command line consists of words separated by spaces: the first word is the command, the others are its arguments. By convention, options start with `-` (short, combinable: `ls -l -a` is `ls -la`) or `--` (long: `ls --all`), and `--` alone ends the options, so `rm -- -file` removes a file named `-file`. A command is one of:

| Kind | Example | Found by |
|---|---|---|
| alias | `ll` defined as `ls -alF` | the shell's alias table |
| function | defined in a script or `~/.bashrc` | the shell |
| builtin | `cd`, `echo`, `export`, `source`, `type` | built into the shell (`cd` must be: a child process cannot change its parent's directory) |
| external program | `/usr/bin/grep` | a search through the directories in `PATH` |

`type grep` tells which kind a name is, `which -a python3` lists all matching programs on the `PATH`, and the first match wins, which is how activating a conda environment or loading a module ([4.11.11](/4.11.11#sec-11.2)) changes which `python3` runs.

### 10.1.2. Getting Help

`man ls` shows the manual page (`/` searches, `n` jumps to the next match, `q` quits); `man 2 open` the page of the **system call** in section 2 rather than a command; `ls --help` a summary; `help cd` the documentation of a builtin; `tldr ls` (if installed) practical examples. Bash's line editing saves much typing: Tab completes commands and file names, the up arrow and Ctrl-R search the history, Ctrl-A and Ctrl-E move to the start and end of the line, Ctrl-C interrupts the running program and Ctrl-D ends the input (and exits the shell).

## 10.2. Files and Directories

### 10.2.1. Navigation and Manipulation

| Command | Effect |
|---|---|
| `pwd` | print the working directory |
| `cd dir`, `cd ..`, `cd ~` or `cd`, `cd -` | change directory: to `dir`, the parent, home, the previous one |
| `ls -lah` | list in long format (`-l`), including hidden files whose names start with `.` (`-a`), with human-readable sizes (`-h`) |
| `mkdir -p a/b/c` | create directories, including missing parents |
| `cp -r src dst`, `mv old new`, `rm file`, `rm -r dir` | copy, move or rename, remove (permanently: there is no recycle bin) |
| `ln -s target name` | create a **symbolic link** ([4.11.7](/4.11.7#sec-7.1.4)) |
| `touch f` | create an empty file or update its mtime |
| `cat`, `less`, `head -n 20`, `tail -n 20`, `tail -f log` | print, page through, show the start or end, follow a growing file |
| `du -sh dir`, `df -h` | disk usage of a directory, free space of the **file systems** |
| `find dir -name '*.fq.gz' -size +1G` | search a directory tree by name, size, time, type |
| `tar -czf out.tar.gz dir`, `tar -xzf out.tar.gz` | create and extract compressed archives |

### 10.2.2. Expansion and Quoting

Before running a command, the shell expands the command line in a fixed order: braces (`{a,b}`, `{1..3}`), tilde (`~`), parameters and variables (`$HOME`), command substitution (`$(date)`), arithmetic (`$((7 * 6))`), word splitting, and finally pathname expansion.

**Definition 10.2.1 (Glob)** A **glob** (wildcard pattern) is a word containing `*` (any string, including the empty one), `?` (any single character) or a bracket expression `[...]` (one character from a set, such as `[0-9]`); the shell replaces it by the sorted list of matching file names. Globs are not **regular expressions**: `*` alone means "anything", and a glob that matches nothing is passed on unchanged (in Bash's default settings).

Quoting controls the expansions. Single quotes preserve every character literally; double quotes allow `$` expansions and command substitution but suppress word splitting and globbing; a backslash quotes one character.

```text
$ echo data/*.fa            # glob expanded by the shell
data/sample B.fa data/sampleA.fa
$ echo 'data/*.fa'          # single quotes: literal
data/*.fa
$ echo "$HOME" '$HOME'      # double quotes expand variables, single quotes do not
/home/zf-li23 $HOME
$ f="my file.txt"; touch "$f"
$ ls $f                     # unquoted: split into two words, "my" and "file.txt"
ls: cannot access 'my': No such file or directory
ls: cannot access 'file.txt': No such file or directory
$ ls "$f"
my file.txt
```

The rule that follows from the last example: always write variables in double quotes (`"$f"`, `"$@"`) unless word splitting is wanted. File names with spaces, which come from Windows and from sequencing facilities, break scripts that ignore this.

## 10.3. Streams, Redirection and Pipelines

### 10.3.1. Standard Streams and Redirection

**Definition 10.3.1 (Standard Streams)** Every process starts with three open file descriptors, the **standard streams**: *standard input* (descriptor 0, `stdin`), from which a program reads its input; *standard output* (descriptor 1, `stdout`), to which it writes its results; and standard error (descriptor 2, `stderr`), to which it writes diagnostics. In an interactive shell all three refer to the terminal.

Programs that read standard input and write standard output can be combined freely, because the shell can attach the streams to files or other programs before starting them.

**Definition 10.3.2 (Redirection)** **Redirection** is the shell's replacement of a command's standard streams (or other descriptors) by files, carried out in the child process before the program starts. The forms are:

| Syntax | Meaning |
|---|---|
| `cmd > file` | standard output to `file` (truncated first) |
| `cmd >> file` | standard output appended to `file` |
| `cmd 2> err.log` | standard error to `err.log` |
| `cmd > out.log 2>&1` | standard output to `out.log`, then descriptor 2 duplicated from 1: both go to `out.log` (Bash also accepts `&> out.log`) |
| `cmd < file` | standard input from `file` |
| `cmd << EOF` … `EOF` | a *here document*: the following lines up to `EOF` are standard input |
| `cmd <<< "$var"` | a *here string* |
| `cmd 2> /dev/null` | discard error messages ([4.11.8](/4.11.8#sec-8.1.4)) |

Redirections are processed from left to right, each one a `dup2` ([4.11.8](/4.11.8#sec-8.5.3)). So `cmd > out.log 2>&1` sends both streams to the file, whereas `cmd 2>&1 > out.log` makes standard error a copy of the old standard output (the terminal) and only then redirects standard output to the file. Keeping results on standard output and diagnostics on standard error is what lets `tool > result.txt` produce a clean result file while errors still appear on the screen.

### 10.3.2. Pipes and Pipelines

**Definition 10.3.3 (Pipe and Pipeline)** A **pipe** is a kernel buffer with a write end and a read end, each a file descriptor; bytes written to the write end are read, in order, from the read end, a reader blocks when the buffer is empty and a writer when it is full (64 KiB by default on Linux). A **pipeline** `cmd1 | cmd2 | ... | cmdn` connects the standard output of each command to the standard input of the next through pipes; all commands run concurrently as separate processes, and the **exit status** of the pipeline is that of the last command.

A pipeline is concurrency with no programming: `cmd2` processes the first lines while `cmd1` is still producing later ones, data flow through memory without temporary files, and on a multicore machine the stages run in parallel. A pipeline that decompresses, filters and counts a 50-GB FASTQ file needs only a few kilobytes of memory. When a reader exits early (`head`), the writer's next write fails with `SIGPIPE` and the writer terminates, so `zcat huge.fq.gz | head` returns at once.

### 10.3.3. The Text-Processing Tools

Unix tools treat text as a sequence of lines, often divided into fields by tabs, which is exactly the shape of most bioinformatics formats (BED, GTF, VCF, SAM, count tables). The core tools:

| Tool | Purpose | Example |
|---|---|---|
| `cat`, `zcat` | concatenate files, decompress gzip to stdout | `zcat reads.fq.gz \| head -4` |
| `head`, `tail` | first or last lines; `tail -n +2` from line 2 (skip a header) | `tail -n +2 table.tsv` |
| `wc` | count lines, words, bytes (`-l`, `-w`, `-c`) | `wc -l reads.fq` |
| `cut` | select fields (`-f`, tab-separated by default; `-d,` for commas) | `cut -f1,3 genes.tsv` |
| `sort` | sort lines; `-k2,2` by field 2, `-n` numerically, `-r` reversed, `-u` unique, `-t` separator | `sort -k1,1 -k2,2n regions.bed` |
| `uniq` | collapse adjacent identical lines; `-c` counts them (sort first) | `sort \| uniq -c` |
| `tr` | translate or delete characters | `tr -d '\n'`, `tr a-z A-Z` |
| `paste`, `join` | merge files side by side, or on a common key | `paste ids.txt values.txt` |
| `grep` | print lines matching a **regular expression**; `-v` invert, `-c` count, `-i` ignore case, `-E` extended syntax, `-F` fixed string, `-w` whole words, `-o` only the match | `grep -c '^>' seqs.fa` |
| `sed` | stream editor; mostly substitution `s/regex/replacement/flags` | `sed -E 's/^chr//'` |
| `awk` | a small language for field-based processing: `pattern { action }` per line, fields `$1, $2, ...`, `NR` line number, `NF` number of fields, associative arrays | see below |
| `find`, `xargs` | find files; build command lines from standard input | `find . -name '*.bam' -print0 \| xargs -0 -n1 samtools index` |

A small gene table makes the tools concrete:

```text
$ head -3 genes.tsv
gene_id	chrom	start	end	strand	biotype
ENSG01	chr1	11869	14409	+	lncRNA
ENSG02	chr1	14404	29570	-	pseudogene
```

Count genes by biotype: skip the header, take field 6, sort, count adjacent duplicates, sort by count:

```text
$ tail -n +2 genes.tsv | cut -f6 | sort | uniq -c | sort -rn
      4 protein_coding
      3 lncRNA
      1 pseudogene
```

`awk` filters and computes in one step. Lengths of protein-coding genes (coordinates are 1-based and inclusive, hence the $+1$), and the number of genes and total length per chromosome with associative arrays:

```text
$ awk -F'\t' 'NR > 1 && $6 == "protein_coding" { print $1, $2, $4 - $3 + 1 }' genes.tsv
ENSG03 chr1 6167
ENSG04 chr2 8057
ENSG06 chr3 10536
ENSG07 chrX 38854
$ awk -F'\t' 'NR > 1 { n[$2]++; bp[$2] += $4 - $3 + 1 }
>             END { for (c in n) print c, n[c], bp[c] }' genes.tsv | sort
chr1 3 23875
chr2 2 8990
chr3 1 10536
chrX 2 65889
```

On a FASTA file: count the records, the total number of bases, find records containing an ambiguous base `N` (`-B1` prints one line of context before each match), and rewrite headers with a captured group:

```text
$ grep -c '>' seqs.fa
3
$ grep -v '>' seqs.fa | tr -d '\n' | wc -c
34
$ grep -B1 N seqs.fa
>read3 sample=A
ACGTNNACGT
$ sed -E 's/^>(\S+) sample=(\S+)/>\2_\1/' seqs.fa | head -2
>A_read1
ACGTACGTTTGA
```

Two traps are worth knowing. `sort` follows the locale's collation order by default, which differs from byte order; tools that require sorted input (`join`, `comm`, many genomics tools) expect `LC_ALL=C sort`, which is also much faster. And these tools do not understand quoting in CSV files (a comma inside a quoted field); for real CSV, use a CSV-aware tool (`csvkit`, `mlr`, `xsv`/`qsv`) or pandas ([4.4.5](/4.4.5)). Dedicated tools such as `samtools`, `bcftools`, `bedtools` and `seqkit` handle the genomics formats correctly and quickly; the generic tools are for quick looks, simple tables and glue.

## 10.4. Users, Groups and Permissions

Linux is a multi-user system. Every user has a numeric user ID (UID) and belongs to a primary group and possibly further groups (`id` shows them); every file has an owner, a group and a mode.

**Definition 10.4.1 (Permission Bits)** The **permission bits** of a file are nine bits in its inode, three for each of the classes *user* (the owner), group and *others*: read (`r`), write (`w`) and execute (`x`). For a regular file they allow reading its contents, modifying it, and running it as a program. For a directory, `r` allows listing its names, `w` creating, deleting and renaming entries in it, and `x` (*search*) accessing entries by name, which is needed to reach anything inside. The kernel checks the first class that applies to the calling process (owner, else group, else others).

`ls -l` shows the type and the mode as ten characters, followed by the link count, owner, group, size and mtime:

```text
$ ls -l fasta_stats.sh
-rwxr-xr-x 1 zf-li23 zf-li23 840 Oct 21 15:47 fasta_stats.sh
$ ls -ld data
drwxr-xr-x 2 zf-li23 zf-li23 4096 Oct 21 15:47 data
```

The first character is the type (`-` regular file, `d` directory, `l` symbolic link, `b`/`c` device); `rwxr-xr-x` means the owner may read, write and execute, group and others may read and execute. In octal each class is one digit with $r = 4$, $w = 2$, $x = 1$, so `rwxr-xr-x` is 755 and `rw-r-----` is 640.

| Command | Effect |
|---|---|
| `chmod 640 results.tsv` | set the mode in octal |
| `chmod u+x script.sh`, `chmod -R g+rX project/` | add or remove bits symbolically (`X`: execute only for directories and already executable files) |
| `chgrp lab project/`, `chown` | change the group; changing the owner requires root |
| `umask` | the bits removed from the mode of newly created files; with the usual `0022`, files are created `644` and directories `755`; `umask 007` keeps new files private to the group |

Three special bits complete the mode. *setuid* on an executable makes it run with the file owner's UID (this is how `passwd`, owned by root, can update the password database); *setgid* on a directory makes new files inherit the directory's group, which keeps a shared lab directory usable by the whole group; the *sticky bit* on a directory (`/tmp` has mode `1777`, shown as `drwxrwxrwt`) lets users delete only their own files there. The superuser `root` (UID 0) bypasses these checks; ordinary users run single commands as root with `sudo`, which servers and clusters generally do not grant, which is why software there is installed in the home directory, in conda environments or in containers ([4.11.9](/4.11.9), [4.11.11](/4.11.11#sec-11.2)).

On a shared server the defaults matter: a home directory with mode 755 lets every user read everything in it. Protect private data and credentials with `chmod 700 ~` or at least `chmod 700 ~/.ssh`, and use groups, not mode 777, to share a project.

## 10.5. Processes and Job Control

The shell is a **process** manager. Every command runs as a child process with its own **PID**, and the tools for watching and controlling processes are:

| Command | Effect |
|---|---|
| `ps aux`, `ps -ef` | list all processes; `ps -u $USER` only one's own |
| `pgrep -a name`, `pidof` | find processes by name |
| `top`, `htop`, `btop` | interactive display of CPU and memory usage per process |
| `kill PID`, `kill -9 PID`, `pkill name` | send `SIGTERM` (ask the process to terminate), `SIGKILL` (force; cannot be caught), or a **signal** by name |
| `time cmd`, `/usr/bin/time -v cmd` | elapsed, user and system time; with `-v` also the maximum resident memory |
| `nice -n 10 cmd`, `renice` | run with a lower scheduling priority |

Each command returns an **exit status** (0 for success, 1–255 for failure, 128 + n when killed by **signal** n, so 137 for `SIGKILL`), which the shell stores in `$?` and uses for control flow: `cmd1 && cmd2` runs `cmd2` only if `cmd1` succeeded, `cmd1 || cmd2` only if it failed, and `cmd1; cmd2` runs both.

**Definition 10.5.1 (Job Control)** **Job control** is the shell's ability to run several pipelines, its *jobs*, from one terminal and move them between the *foreground* (attached to the terminal's input, at most one) and the *background*. `cmd &` starts a job in the background; Ctrl-Z stops the foreground job (with `SIGTSTP`); `jobs` lists the jobs; `fg %n` and `bg %n` resume job `n` in the foreground or background; Ctrl-C sends `SIGINT` to the foreground job.

Background jobs belong to the terminal session. When the terminal closes (the SSH connection drops, the laptop sleeps), the shell sends `SIGHUP` to its jobs and they normally die. Long computations must therefore be detached from the terminal: run with `nohup cmd > log 2>&1 &` (ignore `SIGHUP`), inside `tmux` (§10.7.2), or, on a cluster, as a batch job ([4.11.11](/4.11.11#sec-11.3)).

## 10.6. The Environment and Configuration

**Definition 10.6.1 (Environment Variable)** An **environment variable** is a name–value pair (both strings) in the *environment* of a process, a list that the process inherits from its parent at `exec` and passes on to its own children. The shell distinguishes ordinary shell variables (`x=1`) from exported ones (`export X=1`); only exported variables reach child processes.

Important variables:

| Variable | Meaning |
|---|---|
| `PATH` | colon-separated list of directories searched for commands, in order |
| `HOME`, `USER`, `PWD`, `SHELL` | home directory, user name, working directory, login shell |
| `LANG`, `LC_ALL` | locale: language, character encoding, sorting order |
| `TMPDIR` | where programs create temporary files (set to local scratch on clusters) |
| `OMP_NUM_THREADS` | number of threads for OpenMP programs and many numerical libraries ([4.11.11](/4.11.11#sec-11.4)) |
| `LD_LIBRARY_PATH` | extra directories searched for shared libraries at run time ([4.2.2](/4.2.2#sec-2.4.4)) |

`env` prints the environment, `echo "$PATH"` one variable, and `VAR=value cmd` sets a variable for one command only (`LC_ALL=C sort`). To add a directory of one's own programs, `export PATH="$HOME/.local/bin:$PATH"` (prepending gives it priority). Bash reads configuration files at start-up: a *login* shell (an SSH session) reads `~/.bash_profile` or `~/.profile`, an interactive non-login shell (a new terminal tab) reads `~/.bashrc`; the usual arrangement is to put everything in `~/.bashrc` and have `~/.profile` source it. After editing, `source ~/.bashrc` applies the changes to the current shell. Lines that tools such as `conda init` add to these files are a frequent cause of a "wrong" `python3` on the `PATH`.

## 10.7. Remote Work

### 10.7.1. SSH

**Definition 10.7.1 (SSH)** **SSH** (Secure Shell) is a cryptographic network protocol for logging in to and running commands on a remote machine, and for tunneling other connections and copying files over an encrypted, authenticated channel. The client is `ssh`; the server is `sshd`, listening on TCP port 22 by default.

`ssh alice@login.cluster.example.org` opens a shell on the remote machine; `ssh host cmd` runs a single command there. Instead of a password, use a key pair: the private key stays on the laptop, the public key is placed in `~/.ssh/authorized_keys` on the server, and the server verifies that the client holds the private key without it ever being sent.

```bash
ssh-keygen -t ed25519 -C "alice@laptop"      # create ~/.ssh/id_ed25519 and id_ed25519.pub
ssh-copy-id alice@login.cluster.example.org  # append the public key to the server's authorized_keys
```

Protect the private key with a passphrase, and let `ssh-agent` remember it for the session. The file `~/.ssh/config` saves typing and handles clusters reachable only through a gateway:

```text
Host gateway
    HostName gateway.example.org
    User alice

Host cluster
    HostName login.cluster.example.org
    User alice
    ProxyJump gateway          # connect through the gateway
    ServerAliveInterval 60     # keep idle connections open
```

With this, `ssh cluster`, `scp results.tsv cluster:project/` and `rsync -av data/ cluster:project/data/` all work by name ([4.11.11](/4.11.11#sec-11.5)). Port forwarding reaches services that listen only on the remote machine: `ssh -L 8888:localhost:8888 cluster` makes a Jupyter server running on the cluster at port 8888 available in the laptop's browser at `localhost:8888`. VS Code's Remote-SSH extension uses the same configuration to edit and run code on the server.

### 10.7.2. tmux

**Definition 10.7.2 (Terminal Multiplexer)** A **terminal multiplexer** is a program that runs shells in virtual terminals managed by a server process that is independent of any real terminal; a client attaches to these sessions, can split them into windows and panes, and can detach without terminating them. `tmux` and GNU `screen` are the common ones.

The typical use is a long job on a remote server: connect with SSH, start `tmux new -s assembly`, run the job, detach with Ctrl-B then D, log out. The job keeps running because its terminal belongs to the tmux server, not to the SSH connection; later, `ssh server` and `tmux attach -t assembly` (or `tmux ls` to list the sessions) return to it. Inside tmux, the prefix Ctrl-B followed by `c` creates a window, `n` and `p` switch windows, `%` and `"` split the window into panes, and `[` enters scroll mode. On a cluster, tmux belongs on the login node for editing and monitoring only; computations go to compute nodes through the scheduler ([4.11.11](/4.11.11#sec-11.1)).

## 10.8. Bash Scripts

### 10.8.1. A Complete Script

A script is a file of shell commands. The following one summarizes FASTA files and shows the elements of a robust script:

```bash
#!/usr/bin/env bash
# Summarize FASTA files: number of sequences and total length per file.
set -euo pipefail

usage() {
    echo "usage: $(basename "$0") [-o OUT] FILE..." >&2
    exit 2
}

out=/dev/stdout
while getopts "o:h" opt; do
    case "$opt" in
        o) out=$OPTARG ;;
        *) usage ;;
    esac
done
shift $((OPTIND - 1))
[[ $# -ge 1 ]] || usage

tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT          # clean up even if the script fails

printf 'file\tsequences\tbases\n' > "$tmp"
for f in "$@"; do
    if [[ ! -r $f ]]; then
        echo "warning: cannot read '$f', skipped" >&2
        continue
    fi
    n=$(grep -c '^>' "$f" || true)            # grep exits 1 when nothing matches
    bases=$(grep -v '^>' "$f" | tr -d '\n' | wc -c)
    printf '%s\t%d\t%d\n' "$(basename "$f")" "$n" "$bases" >> "$tmp"
done
cat "$tmp" > "$out"
```

```text
$ chmod +x fasta_stats.sh
$ ./fasta_stats.sh data/*.fa missing.fa
warning: cannot read 'missing.fa', skipped
file	sequences	bases
sample B.fa	1	2
sampleA.fa	2	9
$ ./fasta_stats.sh; echo "exit status: $?"
usage: fasta_stats.sh [-o OUT] FILE...
exit status: 2
```

Line by line:

- The first line, the *shebang* `#!`, tells the **kernel** at `exec` which interpreter runs the file; `/usr/bin/env bash` finds `bash` on the `PATH`. With the execute bit set (`chmod +x`), the script runs as `./fasta_stats.sh`; without it, as `bash fasta_stats.sh`.
- `set -euo pipefail` is the "strict mode": `-e` exits at the first command that fails (outside conditions), `-u` treats undefined variables as errors (catching typos such as `rm -rf "$OUTDIR/"` with `OUTDIR` unset), and `-o pipefail` makes a pipeline fail if any stage fails, not only the last. Without `pipefail`, `false | true` succeeds. Commands that are allowed to fail are marked explicitly, as `grep -c ... || true` above.
- Functions (`usage`) are called like commands, and their arguments are `$1`, `$2`, ….
- `getopts` parses short options; `"$@"` expands to all remaining arguments, each one a separate word even when it contains spaces (the file `sample B.fa` is handled correctly), and `$#` is their number.
- `[[ ... ]]` is Bash's test command: `-r` readable, `-f` regular file, `-d` directory, `-z` empty string, `==` pattern match, `=~` regular-expression match, `-lt`/`-gt` numeric comparison.
- `$(...)` is *command substitution*: it runs a command and substitutes its standard output.
- `mktemp` creates a unique temporary file, and `trap ... EXIT` removes it however the script ends; output is written to the final destination only at the end, so an interrupted run does not leave a half-written result under the final name.
- Messages go to standard error (`>&2`), data to standard output, and errors produce a nonzero exit status, so the script composes with pipelines and with workflow managers.

### 10.8.2. Variables, Loops and Arrays

```bash
samples=(ctrl_1 ctrl_2 treat_1 treat_2)       # an indexed array
echo "${#samples[@]} samples, first: ${samples[0]}"

for s in "${samples[@]}"; do                   # quote to keep elements intact
    echo "aligning $s"
    # minimap2 -t 8 -a ref.fa "fastq/${s}.fq.gz" > "bam/${s}.sam"
done

for i in {1..22} X Y; do echo "chr$i"; done   # brace expansion

while IFS=$'\t' read -r id chrom start end _; do   # read a TSV line by line
    echo "$id is on $chrom"
done < <(tail -n +2 genes.tsv)

f=sample.sorted.bam
echo "${f%.bam}.bai"      # remove a suffix: sample.sorted.bai
echo "${f##*.}"           # extension: bam
echo "${OUTDIR:-results}" # default value if OUTDIR is unset or empty
```

Shell arithmetic is integer only (`$(( (a + b) / 2 ))`); for floating point, call `awk` or Python. The shell is the right language for orchestrating programs and files; once a script needs data structures, floating-point arithmetic or more than a page of logic, Python is the better choice, and once it needs to run many steps over many samples with re-execution of only what changed, a workflow manager is ([4.11.11](/4.11.11#sec-11.6)). ShellCheck (`shellcheck script.sh`) finds most quoting mistakes and other common bugs in shell scripts and is worth running on every script.

### 10.8.3. Running Many Commands in Parallel

A machine with many cores can process independent files in parallel directly from the shell:

```bash
# Compress every FASTQ file, 8 at a time
find fastq -name '*.fq' -print0 | xargs -0 -P 8 -n 1 gzip

# The same with GNU parallel, which also collects output in order and logs jobs
parallel -j 8 --joblog jobs.log 'samtools sort -o {.}.sorted.bam {}' ::: bam/*.bam
```

`-print0` and `-0` separate names by null bytes, which is safe for names with spaces. This is the shell form of an **embarrassingly parallel** computation ([4.4.7](/4.4.7)); on a cluster the same pattern becomes a job array ([4.11.11](/4.11.11#sec-11.4)).

## Summary

- The shell reads command lines, expands them (variables, command substitution, globs) and runs programs as child processes found through `PATH`. Quote variables (`"$f"`, `"$@"`); globs are not regular expressions.
- Every process has standard input, output and error. Redirections (`>`, `>>`, `2>`, `2>&1`, `<`) are `dup2` calls in the child, processed left to right; a pipeline runs its commands concurrently, connected by pipes.
- The text tools `grep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `tr`, `find` and `xargs` handle line- and field-oriented data; use `LC_ALL=C sort` for byte order, and format-specific tools for SAM, VCF and real CSV.
- Permission bits (`rwx` for user, group, others; octal 755, 640) control access, with special meanings for directories; `umask` sets defaults, setgid directories and groups support sharing.
- Exit statuses drive `&&` and `||`; job control moves jobs between foreground and background; jobs die with their terminal unless detached with `nohup` or `tmux`.
- Environment variables are inherited by child processes; `PATH` determines which program runs; `~/.bashrc` configures interactive shells.
- SSH with ed25519 keys and `~/.ssh/config` (with `ProxyJump` and port forwarding) is the way into servers; `tmux` keeps sessions alive across disconnections.
- Robust Bash scripts use a shebang, `set -euo pipefail`, quoting, `trap` cleanup, messages on standard error and meaningful exit statuses; ShellCheck catches common mistakes.
