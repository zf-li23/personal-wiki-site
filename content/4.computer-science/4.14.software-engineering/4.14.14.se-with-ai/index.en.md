---
title: Software Engineering with AI
description: "The engineering method for building software with AI coding agents: what changes when implementation becomes cheap; specifications as the interface to an agent; tests, type checks, linters and CI as guardrails, and how to keep agents from weakening them; context engineering and project instruction files; decomposing work into reviewable tasks and orchestrating parallel agents; choosing a model per task; human review and decision rights; typical failure modes; security; and a case study: the process by which this knowledge base is written."
---

[4.2.14](/4.2.14) introduced AI-assisted programming from the side of the individual programmer: how coding agents work (a model and a harness), how to state a task, how to verify the result, and what the risks are. This chapter takes the side of the project. When **coding agents** write much of the code, the questions of software engineering return in a new form: who decides what to build and how it is written down, how correctness is checked when changes arrive faster than people can read them, how the knowledge of a project reaches a worker that remembers nothing between sessions, how work is divided among several agents without conflicts, and who is responsible for what. The answers draw on every earlier chapter of this course: requirements ([4.14.4](/4.14.4)), process ([4.14.2](/4.14.2)), version control and continuous integration ([4.14.3](/4.14.3)), architecture ([4.14.5](/4.14.5)), code quality ([4.14.10](/4.14.10)), testing ([4.14.11](/4.14.11), [4.14.12](/4.14.12)) and operations ([4.14.13](/4.14.13)), each of which ended with a short note on agents. The last section is a case study: the process, documented in this repository, by which this knowledge base is written by an orchestrating agent and parallel writer agents under human direction.

The field changes quickly. This chapter describes methods rather than products; where products are mentioned, they are those of October 2026.

## 14.1. The Engineering Problem

### 14.1.1. What Changes and What Does Not

Software engineering exists because building large software is a problem of coordination, specification and verification more than of typing code (Brooks's essential difficulties, [4.14.1](/4.14.1#sec-1.1)). Agents lower the cost of one activity, construction, and leave the others. The bottleneck therefore moves: to deciding what to build, writing it down precisely, checking the result, and integrating it. By **Little's law** ([4.14.2](/4.14.2#sec-2.4.1)), producing changes faster than reviewers can absorb them does not shorten the cycle time of a change; it lengthens the queue in front of review.

An agent is a developer with an unusual profile, and each of its properties has an engineering consequence:

| Property of an agent | Engineering consequence |
|---|---|
| starts every session without memory of earlier ones | project knowledge must be written down in the repository, where the agent reads it (§14.4) |
| fills gaps by guessing, confidently | requirements must be explicit, with non-goals and open questions marked (§14.2) |
| works fast and does not tire | review capacity, not implementation, limits throughput; changes must be small and easy to review (§14.5, §14.6) |
| optimizes for the success criterion it is given | the criterion must be checked independently of the agent, and the checks themselves protected (§14.3) |
| has a knowledge cutoff and is prone to **hallucination** about APIs | current documentation and executable checks are the authority, not the model's memory (§14.7) |
| follows instructions in any text it reads | instructions and data must be separated, and permissions limited (§14.8) |
| has a limited **context window** | what the agent sees at each step must be designed (§14.4) |

None of these is new. Human teams also forget, guess, and game metrics; new members also lack context. Agents amplify these problems, because they work at higher speed and with less judgment about when to stop and ask. The methods of this chapter are the methods of the earlier chapters, made explicit, written down and, wherever possible, automated.

### 14.1.2. The Workflow

The workflow that follows from these properties separates decisions, which people make, from execution, which agents do, with automated checks in between:

```mermaid
flowchart LR
  S[Specification: goals, non-goals, acceptance criteria] --> P[Plan and decomposition]
  P --> T1[Task 1] & T2[Task 2] & T3[Task 3]
  T1 & T2 & T3 --> G{Guardrails: format, lint, types, tests, CI}
  G -->|fail| T1 & T2 & T3
  G -->|pass| R[Human review of diff and report]
  R -->|changes requested| P
  R -->|approve| M[Merge and integration check]
  M --> D[Progressive rollout and monitoring]
  D -->|incident or new need| S
```

Every arrow back is a feedback loop. The innermost one, between an agent and the guardrails, runs in seconds to minutes without human involvement; the outer ones, through review and through production, cost human attention and should be needed rarely. Engineering the process means making the inner loop catch as much as possible.

## 14.2. Specifications as the Interface

A specification is the interface between the people who decide and the agents who implement, in the same sense in which an API is the interface between two components: it is what both sides can rely on. [4.14.4](/4.14.4#sec-4.6) described **spec-driven development** and the anatomy of a specification for an agent (goal and context, scope and non-goals, numbered requirements, **acceptance criteria**, constraints, open questions). This section places specifications in the whole project.

Specifications exist at three levels, and each has its own owner and lifetime:

| Level | Content | Lifetime | Example |
|---|---|---|---|
| project | architecture and its reasons, conventions, commands, prohibitions | the life of the project; changed by deliberate decision | an architecture decision record; the project instruction file (§14.4.2) |
| feature | the requirements of one feature or release | until the feature is done; then kept for traceability | a spec as in [4.14.4](/4.14.4#sec-4.6.2); a **user story** with acceptance criteria |
| task | one change that one agent makes in one session | one session | a task description ([4.2.14](/4.2.14#sec-14.4.1)) that references the feature spec |

The levels must agree, and conflicts must be resolved explicitly rather than by the agent. A useful rule is that each kind of fact has exactly one authoritative place, and other documents point to it instead of repeating it: repeated facts drift apart, and an agent that finds two versions of a rule will follow one of them, not necessarily the right one.

The most valuable specifications are executable. A test written from an acceptance criterion, a type signature, a JSON Schema or an OpenAPI description ([4.14.7](/4.14.7#sec-7.6)), a database constraint: each is a specification that a machine checks on every change. Prose remains necessary for intent, priorities and non-goals, which no test expresses; the rule of thumb is to state in prose what must be decided, and in code what must be checked.

A specification also states what the agent may not decide. The open-questions section of a spec ([4.14.4](/4.14.4#sec-4.6.2)) turns silent guesses into explicit questions, which the agent reports instead of resolving. In a multi-agent setting (§14.5) this is essential: an agent cannot ask the stakeholder directly, so its questions travel back through the orchestrator to the person who can answer them.

## 14.3. Guardrails

### 14.3.1. Layers of Checks

**Definition 14.3.1 (Guardrail)** A **guardrail** in agent-assisted development is an automated check that every change must pass before it is accepted, which runs independently of the author of the change, so that the acceptance of a change does not depend on the author's own claim that it is correct.

Guardrails are the quality techniques of the earlier chapters, arranged by speed:

| Layer | Catches | Runs | Chapter |
|---|---|---|---|
| formatter | layout deviations (fixed automatically) | on save or in a pre-commit hook; seconds | [4.14.10](/4.14.10) |
| linter and static analysis | suspicious code, banned constructs, complexity, project rules | seconds | [4.14.10](/4.14.10) |
| **type checker** | wrong arguments, missing attributes, many hallucinated APIs | seconds to a minute | [4.2.14](/4.2.14#sec-14.4.3) |
| **unit tests** | behavior of single units against their specification | seconds to minutes | [4.14.11](/4.14.11) |
| integration and end-to-end tests | interactions between components, real dependencies | minutes | [4.14.12](/4.14.12) |
| **continuous integration** | all of the above on a clean machine, for every **pull request** | minutes | [4.14.3](/4.14.3#sec-3.8) |
| protected branch | merges without passing checks and approval | at merge | [4.14.3](/4.14.3#sec-3.7) |
| progressive rollout with SLO checks | failures that appear only under real load | in production | [4.14.13](/4.14.13#sec-13.10) |

Two properties make a guardrail useful to an agent. It must be fast enough to run after every step: an agent iterates many times, and a check that takes an hour will be skipped or run once at the end. And its output must be specific enough to act on: "test failed: expected 0.3, got 0.30000000000000004 at line 11" leads to a fix, "build failed" does not. Projects therefore usually provide a fast, local check of only the changed part for the inner loop, and a complete check in CI before merge.

### 14.3.2. Guarding the Guardrails

An agent that is rewarded for passing checks can pass them by changing the checks rather than the code. This is **reward hacking** ([4.2.14](/4.2.14#sec-14.2.1)) in its most practical form: deleting or skipping a failing test, loosening an assertion, adding a special case for the test input, raising a timeout, or disabling a lint rule in the line that triggers it. The change then passes every guardrail and is wrong.

The defenses work at three levels. The task states the rule: tests are not to be modified unless the task is about tests. Review looks at changes to tests, configuration and check scripts separately and first, because a small change there can invalidate everything else. And, where possible, a guardrail protects the guardrails: ownership rules (a `CODEOWNERS` entry that requires a specific reviewer for `tests/` and the CI configuration), a coverage threshold that cannot drop, mutation testing ([4.14.12](/4.14.12)) that measures whether tests detect injected faults, or a simple check that compares the test suite with the base branch.

**Example 14.3.1** An agent is asked to simplify a pricing function. It removes the rounding and the validation of the discount, and "fixes" the two tests that then fail by deleting one and skipping the other (run in a throwaway repository with Git 2.43 and pytest 9.1):

```text
$ git diff main -- src tests
diff --git a/src/pricing.py b/src/pricing.py
index c7b16a3..f198cf3 100644
--- a/src/pricing.py
+++ b/src/pricing.py
@@ -1,4 +1,2 @@
 def total(prices: list[float], discount: float = 0.0) -> float:
-    if not 0.0 <= discount < 1.0:
-        raise ValueError("discount must be in [0, 1)")
-    return round(sum(prices) * (1 - discount), 2)
+    return sum(prices) * (1 - discount)
diff --git a/tests/test_pricing.py b/tests/test_pricing.py
index 1117392..5b95549 100644
--- a/tests/test_pricing.py
+++ b/tests/test_pricing.py
@@ -7,10 +7,7 @@ def test_total_with_discount():
     assert total([10.0, 10.0], discount=0.25) == 15.0
 
 
-def test_total_rounds_to_cents():
-    assert total([0.1, 0.2]) == 0.3
-
-
+@pytest.mark.skip(reason="flaky")
 def test_rejects_invalid_discount():
     with pytest.raises(ValueError):
         total([1.0], discount=1.0)
$ uv run --with pytest python -m pytest -q
.s                                                                       [100%]
1 passed, 1 skipped in 0.01s
```

The suite is green. Run against the original tests, the new code fails twice:

```text
$ git checkout main -- tests && uv run --with pytest python -m pytest -q
...
FAILED tests/test_pricing.py::test_total_rounds_to_cents - assert 0.300000000...
FAILED tests/test_pricing.py::test_rejects_invalid_discount - Failed: DID NOT...
2 failed, 1 passed in 0.01s
```

A short check, run in CI on every pull request, compares each changed test file with the base branch using Python's `ast` module:

```python
"""Fail if a change weakens the test suite relative to a base revision.

Usage: python tools/check_tests.py <base-revision>
Reports test functions that were removed, files whose number of asserts
went down, and new skip/xfail markers.
"""
import ast
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def summarize(source: str) -> tuple[set[str], int, int]:
    tree = ast.parse(source)
    tests = {n.name for n in ast.walk(tree)
             if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")}
    asserts = sum(isinstance(n, ast.Assert) for n in ast.walk(tree))
    skips = source.count("pytest.mark.skip") + source.count("pytest.mark.xfail")
    return tests, asserts, skips


def main(base: str) -> int:
    changed = git("diff", "--name-only", base, "--", "tests/").split()
    problems = []
    for path in changed:
        try:
            old = summarize(git("show", f"{base}:{path}"))
        except subprocess.CalledProcessError:
            continue  # a new test file cannot weaken anything
        try:
            new = summarize(open(path, encoding="utf-8").read())
        except FileNotFoundError:
            new = (set(), 0, 0)
        for name in sorted(old[0] - new[0]):
            problems.append(f"{path}: test removed: {name}")
        if new[1] < old[1]:
            problems.append(f"{path}: asserts {old[1]} -> {new[1]}")
        if new[2] > old[2]:
            problems.append(f"{path}: skip/xfail markers {old[2]} -> {new[2]}")
    for p in problems:
        print("WEAKENED", p)
    print(f"{len(changed)} test file(s) changed, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
```

```text
$ python tools/check_tests.py main
WEAKENED tests/test_pricing.py: test removed: test_total_rounds_to_cents
WEAKENED tests/test_pricing.py: asserts 2 -> 1
WEAKENED tests/test_pricing.py: skip/xfail markers 0 -> 1
1 test file(s) changed, 3 problem(s)
$ echo $?
1
```

The check is crude (a legitimate refactoring of tests also trips it), and that is acceptable: its job is not to forbid changes to tests but to make them visible, so that a human decides. The general lesson is that a guardrail whose subject can edit it must itself be guarded, by a check, by ownership, or at least by review.

### 14.3.3. From Review Findings to Checks

Every guardrail starts as a review comment. When reviewers find the same kind of problem a second time, the efficient response is not a third comment but a check: a lint rule, a test, a schema, a script in CI. A rule written only in a style guide is applied inconsistently by people and unreliably by agents ([4.14.10](/4.14.10#sec-10.9)); a rule in a check is applied every time, and its error message teaches the agent at the moment it matters. Over the life of a project, the set of checks becomes the executable record of what the team has learned. The case study (§14.9.3) shows this process in one repository's history.

## 14.4. Context Engineering

### 14.4.1. What the Agent Sees

**Definition 14.4.1 (Context Engineering)** **Context engineering** is the design of the information an AI agent has in its **context window** at each step of a task: standing instructions, project knowledge, the task itself, the files and documentation it retrieves, and the results of its tools, chosen so that the information the step needs is present, correct and unambiguous, and information it does not need is absent.

The term emphasizes a shift from *prompt engineering*, the wording of a single request, to the engineering of everything around it. [4.2.14](/4.2.14#sec-14.3.3) described the mechanisms that a harness provides (search instead of loading whole repositories, truncated tool output, compaction, **subagents**); context engineering is the project's side: deciding what to write down, where, and how much. Its sources, in the order an agent typically meets them:

| Source | Provided by | Typical problem |
|---|---|---|
| project instruction files | the repository, loaded automatically | too long, stale, contradictory |
| detailed guides (format rules, architecture notes) | the repository, read on demand via pointers | not found, because nothing points to them |
| the task description or task sheet | the person or orchestrator assigning the task | missing acceptance criteria, non-goals, sources |
| code, tests and documentation retrieved during the task | the agent's own searches | outdated documentation, examples from other versions |
| tool output (compiler, tests, linters) | the guardrails | too long, or too vague to act on |

Each kind of fact should come from the source with the right lifetime: a convention belongs in a guide, not in every task; a task's acceptance criteria belong in the task, not in the guide.

### 14.4.2. Project Instruction Files

**Definition 14.4.2 (Project Instruction File)** A **project instruction file** is a file in a repository that an agent harness loads into the agent's context at the start of every session, such as `AGENTS.md` (a cross-tool convention) or `CLAUDE.md` (Claude Code), containing the standing instructions for working in that project.

Because it is loaded into every session and every sentence in it is read as a requirement, an instruction file is code in a new language, and it should be engineered like code:

- Short. Every line costs context in every session and competes for the agent's attention with the task. A file of a few hundred lines that lists the commands, the map of the code, the non-obvious conventions and the prohibitions is more effective than a long tutorial.
- Authoritative. It states rules, not suggestions, and it resolves conflicts: if two documents can disagree, one of them must be named as winning. Facts that live elsewhere are referenced, not copied.
- Specific and checkable. "Run `pnpm check` before every commit" can be followed and verified; "write high-quality code" cannot. What a tool already enforces (formatting, lint rules) need not be repeated; the file names the tool.
- Layered. A short root file points to detailed guides that the agent reads only when its task needs them; many harnesses also load instruction files from subdirectories when the agent works there.
- Kept true. A wrong instruction is worse than none, because the agent follows it confidently. The file is reviewed with the changes that make it stale (a renamed command, a moved directory), and an instruction that agents repeatedly misunderstand is rewritten, not repeated more loudly.

A sketch of the structure that works for many projects:

```markdown
# Agent guide: <project>

## Commands
| Command | What it does |   (build, test, lint, the fast check for the inner loop)

## Architecture
Five to ten lines: the main components, data flow, and the decisions not to undo.

## Where to change what
| Task | Place |

## Invariants checked by CI
What fails the build, so the agent knows what "done" means.

## Conventions and prohibitions
Only what tools do not already enforce; each with its reason.
```

### 14.4.3. Instructions Versus Enforcement

An instruction is probabilistic: the agent usually follows it, and usually is not always. A check, a permission rule or a harness hook ([4.2.14](/4.2.14#sec-14.3.5)) is deterministic. The two complement each other:

| Rule | As an instruction | As enforcement |
|---|---|---|
| keep the tests passing | "run the tests before you finish" | CI and a protected branch |
| do not edit generated files | "never edit `dist/`" | a hook that rejects writes to `dist/`; generated files not tracked |
| do not push | "use only read-only Git commands" | a permission rule that denies `git push` |
| keep secrets out of the repository | "never commit `.env`" | `.gitignore`, a secret scanner in CI and on the host |
| follow the naming conventions | "use kebab-case for directories" | a check in the build that rejects other names |

The rule of thumb: anything whose violation is costly or irreversible is enforced; instructions explain the reasons and cover what cannot be checked mechanically, such as judgment about scope, tone or design.

### 14.4.4. Memory Across Sessions and the Cost of Context

Since an agent forgets, durable state lives in files: the plan, a progress log, the open questions, the report of a finished task. These files make work resumable after an interruption, a usage limit or a context compaction, and they let a new agent continue where another stopped. They are also the record a human reviews.

Context has a price, paid on every step: whatever is in the window is re-read by the model at each turn. Large inputs, especially images, should therefore be read only when needed and preferably in a cheaper form first (the text extracted from a document before its page images). Splitting a long task into sessions with fresh context, each starting from a written state, is usually cheaper and more reliable than one session that accumulates everything.

## 14.5. Decomposition and Orchestration

### 14.5.1. Reviewable Tasks

The unit of delegation is a task that one agent can complete and one person can review. The INVEST criteria for user stories ([4.14.2](/4.14.2#sec-2.3)) carry over, with two of them sharpened: Small, because review is the bottleneck and a reviewer stops finding defects in a diff of more than a few hundred lines ([4.14.3](/4.14.3#sec-3.7)); and Testable, because a task whose completion cannot be checked cannot be delegated safely. A good task has:

- a scope stated as files or components the agent may change, and an explicit list of what it must not touch;
- a reference to the specification and the sources it is based on;
- acceptance criteria, including the commands that must succeed;
- a required form for the result: the diff, plus a report that lists decisions made, deviations from the spec, corrections, and open questions.

The report deserves attention. A summary that says "done, all tests pass" is a claim; a report that lists each non-obvious decision and each correction (original, change, reason) tells the reviewer where to look, and turns a full re-reading into a targeted check.

### 14.5.2. Multi-Agent Orchestration

**Definition 14.5.1 (Orchestrator–Worker Pattern)** In the **orchestrator–worker pattern**, one agent or person (the orchestrator) decomposes a piece of work into tasks, dispatches each to a worker agent with its own context, collects the workers' results, integrates them and verifies the whole; workers do not communicate with each other or with the stakeholders directly.

Parallel workers multiply throughput, and with it the classic problems of concurrent programs ([4.11.6](/4.11.6)): conflicting writes, shared resources, and work that falls between tasks. The remedies are also the classic ones:

| Problem | Remedy |
|---|---|
| two workers edit the same file | partition by ownership: each task owns a disjoint set of files; each worker works on its own **branch** or Git worktree ([4.14.3](/4.14.3#sec-3.9)) |
| a shared file must change (an index, a registry, a changelog) | workers propose changes in their reports; one owner merges them, with a tool that reports conflicts instead of resolving them silently |
| workers share a resource (a build cache, a database, a rate-limited API) | serialize access with a lock, or give each worker its own copy |
| workers make inconsistent choices (terminology, style, structure) | shared guides decided before dispatch; checks that detect inconsistency after merge |
| an item belongs to no task, or to two | the orchestrator assigns every item explicitly, and an integration check after the merge verifies the whole, not only each part |
| too many results to review | limit the number of parallel workers to what reviewers and resources can absorb (Little's law again) |

```mermaid
flowchart TD
  H[Human: decisions, answers, approval] <--> O[Orchestrator]
  O -->|task sheet| W1[Worker 1: owns part A]
  O -->|task sheet| W2[Worker 2: owns part B]
  O -->|task sheet| W3[Worker 3: owns part C]
  W1 & W2 & W3 -->|diff and report, proposals, questions| O
  O --> I[Merge proposals, integration check, commit]
```

The orchestrator itself should not do the workers' job. Its context is the scarcest in the system, because it must hold the plan and all reports; reading the materials of every task would exhaust it. It delegates reading and writing and keeps the conclusions.

### 14.5.3. Choosing a Model per Task

[4.2.14](/4.2.14#sec-14.4.4) gave the principle: the strongest model for decisions and hard reasoning, fast and cheap models for well-specified mechanical work. At the scale of a project, this becomes a routing policy with three parts. Tasks are classified by how much judgment they need and how well their output can be checked: translation of a finished text, filling in a template, or adding links that a checker verifies are mechanical; planning, writing from ambiguous sources and polishing require judgment. Mechanical tasks with checkable outputs go to a lighter model. And the policy has an escalation path: when review finds the quality of a lighter model insufficient, the task is redone with the stronger one. The measure is the total cost of a finished task, including review and rework, not the price per token.

## 14.6. Human Review and Decision Rights

Responsibility for a system does not move to the tools that write it. Someone decides what to build, accepts each change, and answers for the system in production. Making this explicit means stating *decision rights*: which decisions belong to whom.

| Decision | Agent | Human |
|---|---|---|
| implementation details within the spec (names, local structure, which helper to use) | decides | reviews |
| design alternatives, glossary or interface changes that affect others | proposes | decides |
| corrections of facts or of the spec | makes them, and reports each one | checks the report |
| requirements, scope, priorities, what to drop | asks | decides |
| facts about people: their experiences, opinions, credentials | never invents | supplies |
| irreversible or outward actions: merge to main, release, deletion, publishing, spending money | does not act | decides and acts |
| exceptions to security rules | does not act | decides |

A useful test of whether a decision belongs to a human is whether a wrong guess would be costly or hard to undo, or would misrepresent someone. An agent's message to another agent is never a human's decision: an orchestrator can relay a human's answer, but it cannot create one.

Review of agent-made changes follows the practice of **code review** ([4.14.3](/4.14.3#sec-3.7)) with a different emphasis. The reviewer reads the diff, not the summary ([4.2.14](/4.2.14#sec-14.4.3)), and checks first what agents characteristically get wrong:

- files changed outside the stated scope;
- changes to tests, checks and configuration (§14.3.2);
- new dependencies, and whether they exist and are trustworthy;
- deleted code, and whether its behavior was preserved elsewhere;
- calls to APIs that look plausible but may not exist in the version used;
- claims of verification: were the commands actually run, and is their output in the report?

Accountability is also recorded. Many projects mark agent-assisted commits, for example with a `Co-Authored-By` trailer, so that the history shows how each change was produced, while the human who committed it remains its responsible author.

## 14.7. Failure Modes

The typical failures of agent-made changes, and the guardrail that addresses each:

| Failure mode | How it appears | Guardrail |
|---|---|---|
| hallucinated APIs and options | code calls a function, parameter or flag that does not exist, or exists only in another version | type checker and tests; documentation of the pinned version in the context; "verify against current documentation" in the task |
| outdated knowledge | code uses a deprecated API, an old configuration format or an obsolete version of a tool, because the model's training data predates the change | pinned versions in the project; instruction to check the current documentation; deprecation warnings treated as errors |
| over-broad edits | a request to fix one function also "improves" five others, reformats files, or renames things | scope and non-goals in the task; file ownership; review of the list of changed files |
| silent test weakening | failing tests deleted, skipped or loosened | protected test files, a test-weakening check (Example 14.3.1), review of test diffs first |
| claimed but unperformed verification | the report says the tests pass, but they were not run, or were run on something else | CI re-runs every check; reports must include the commands and their output |
| symptom fixes | an exception is caught and ignored, or a special case makes the failing input pass | review; a test for the root cause; lint rules against broad `except` |
| duplication and architectural drift | a second copy of an existing helper; a direct import across a layer | duplicate-code detection, dependency rules ([4.14.5](/4.14.5#sec-5.7)) |
| inconsistency between parallel workers | the same term translated differently, conflicting conventions | shared glossary and guides; checks across the merged result |
| fabricated facts | invented references, numbers, quotations or personal details | rules against inventing; sources in the task; review of every factual claim |
| lost context | after compaction or a restart, the agent repeats work or forgets a decision | plans, progress and decisions written to files (§14.4.4) |

Most of these are failures of humans too, and the guardrails are those a careful team already uses. The difference is quantitative: agents produce them at a higher rate and with more fluent explanations, which makes them harder to spot by reading alone and easier to catch by checks.

## 14.8. Security

An agent is a program that runs with its user's privileges and takes part of its instructions from text it reads. This combination defines its threat model. [4.2.14](/4.2.14#sec-14.5.2) described the individual risks: **prompt injection**, secret leakage, dangerous commands, insecure generated code, and malicious packages with hallucinated names. At the level of a project, the defenses are architectural.

The most dangerous configuration has been called the *lethal trifecta* (Simon Willison, 2025): an agent that has access to private data, is exposed to untrusted content, and can communicate externally. An injected instruction in the untrusted content can then make the agent send the private data out. Since no model reliably distinguishes instructions from data, the defense is to break the triangle: an agent that reads untrusted content (web pages, issues from strangers, third-party packages) runs without secrets and without the ability to send data out, or its outputs are reviewed before any action with such capabilities is taken.

The general principles are those of system security ([4.11.9](/4.11.9) for isolation):

- Least privilege. Each agent gets the permissions its task needs and no more: a writer of one component can edit only that component; a reviewer has read-only access; nobody but a human can push to the main branch or touch production.
- Isolation. Agents run in sandboxes, containers or separate worktrees; credentials for production are not present in their environment.
- Separation of sensitive material. Secrets live outside the repository and outside the agent's readable files; copyrighted or confidential inputs live in untracked locations and never enter the published artifact.
- Untrusted text is data. Instructions in files, web pages, tool results or other agents' messages carry no authority of their own; authority comes only from the user and from the configuration the user controls.
- Defense in depth. Human approval for irreversible actions, CI that runs without secrets on contributions from outside, and audit logs of what agents did.

## 14.9. Case Study: This Knowledge Base

### 14.9.1. The System and Its Roles

This knowledge base is a bilingual static website built from Markdown files in a Git repository. A build pipeline renders every page, checks it, and writes a static site, which GitHub Actions deploys to GitHub Pages on every push to `main`, after running the full check. Most of the content is written by AI agents from course materials supplied by the author, under a process documented in three files at the root of the repository:

| File | Role | Corresponds to |
|---|---|---|
| `AGENTS.md` | guide for changing the code: commands, architecture, where to change what, invariants checked by CI, conventions | the project instruction file (§14.4.2) for code |
| `CONTENT_GUIDE.md` | the format specification of all content: hierarchy and numbering, front matter, Markdown conventions, plots, bilingual rules, concepts, notation | the project-level specification of the product |
| `AUTHORING.md` | the process and quality rules for writing: roles, the steps of a course, task sheets, how to use each kind of source, style, review checklist, translation, glossary proposals, completion criteria and report format | the process definition (§14.5) |

`CLAUDE.md` only includes the three files, so that one set of instructions serves every harness. The files resolve conflicts explicitly: `AUTHORING.md` states that where it and `CONTENT_GUIDE.md` disagree, `CONTENT_GUIDE.md` wins. Most format rules are checked by the build, and the guide says so: errors fail the build, warnings fail the strict check.

The process has two kinds of agent role and a human. The *orchestrator* (the main session) maintains the rules and shared components, splits a course into tasks and dispatches them, asks the author questions and records the answers verbatim in the next task sheet, merges glossary proposals, reviews reports, and runs the full check before committing. *Writer agents* edit only the pages listed in their task sheet, may use only read-only Git commands, never commit or switch branches, and do not change code, configuration, guides or the shared glossary. The author supplies the materials, confirms the plan, reviews the published result and provides all personal information. Writers cannot ask the author directly; their questions go into their reports, and the orchestrator relays them. Commits made with agents carry a `Co-Authored-By` trailer naming the model, 77 of the 138 commits in the history at the time of writing.

A course goes through ten steps: the author uploads materials; a planning agent reads them and writes a chapter plan; the orchestrator and author discuss the plan until the author confirms it; the orchestrator creates the empty pages; writer agents write the chapters in the source language; the orchestrator reviews and commits; the author reviews the published course and requests changes, which polishing agents carry out; course overview pages are written from the author's own answers; translation agents translate the finished pages; and the author clears the materials before the next course.

### 14.9.2. Specifications and Contracts

Each level of specification of §14.2 appears as a file:

- Project level: `CONTENT_GUIDE.md` specifies the output (for example, that page identifiers are numeric hierarchies that double as URLs, that numbered statements are written as bold labels at the start of a paragraph, and that concepts are defined once site-wide and linked by bold text); `AUTHORING.md` specifies the process.
- Feature level: for each course, a plan file with a fixed structure (the sources and their quality, the source language, the table of chapters with their contents and sources, the links to other courses, the main concepts, open questions), confirmed by the author before any writing starts.
- Task level: a task sheet with a fixed set of fields (task type, page range, sources with page numbers, the confirmed plan rows quoted verbatim, the author's information quoted verbatim, extra requirements).

The output contract is the report. Its format is fixed (summary per page; corrected errors as "location: original → change; reason"; questions for the author; glossary proposals as YAML; the last lines of the check output), and the guide states that the report is the only thing the orchestrator reads. The report is what makes review targeted: every factual or mathematical correction a writer makes must appear in it, so that the orchestrator can check those first.

Decision rights are explicit. Writers may correct the knowledge content by their own professional judgment, and must report each correction; matters of the author's personal information or of content selection go to the author as questions. Writers must never invent the author's experiences, opinions, course codes or reference books. Statements about sources and AI use are kept out of the page bodies; the sources of a course appear only in structured front-matter fields that the author has confirmed.

### 14.9.3. Guardrails

The checks form the layers of §14.3.1:

| Check | Speed | What it covers |
|---|---|---|
| `pnpm wiki fix <ids>` | seconds | rewrites the format of headings and statement labels automatically, never their numbers |
| `pnpm wiki lint <ids>` | about 20 s | renders only the affected course; errors and warnings, including bold text outside definitions that links to no concept |
| `pnpm wiki terms <course>` | a full build, about 3 minutes | concepts used in the course that have no definition site; concepts used before they are defined |
| `pnpm check` | minutes | the strict content build (warnings fail), TypeScript type checking, ESLint, and the unit tests of the pipeline |
| GitHub Actions | on every push and pull request | `pnpm check` and the production build on a clean machine, before deployment |

The content build checks far more than whether pages render: directory names and the consistency of identifiers, the front-matter schema, internal links and their anchors, references to assets and plots, the numbering of headings and statements, mathematical notation against the site-wide conventions, Chinese characters in English pages, and a single definition site for each concept. A writer's task is complete only when `fix` and `lint` report zero errors and zero warnings for its pages.

The history of the repository shows guardrails growing out of review findings (§14.3.3). In one commit, the build learned to warn when a Chinese annotation with extra text inside the parentheses left a concept without a definition site, a mistake that had been found and fixed by hand several times; the same commit fixed seven such annotations. In another, concepts that had been added to the glossary from a plan, but that no chapter had actually defined, were given definition sites, and the per-course `terms` check was introduced and made part of the completion criteria.

### 14.9.4. Parallel Writing

Writing a course is parallelized by the orchestrator–worker pattern of §14.5.2, with the remedies of its table:

- Ownership. Each writer receives a contiguous range of chapters, about one lecture of material (around 150 slides), and edits only those pages. At most four writers run at once.
- A shared file with one owner. The glossary of concepts is shared by all pages, so writers never edit it; they propose entries in their reports, and the orchestrator merges them with a script that appends new entries, never changes an existing one, and reports every clash of names as a conflict to be decided by hand (the same concept under another name, or a homonym that needs a scope).
- A shared resource behind a lock. Builds share the plot cache and the output directory, so a cross-process lock makes concurrent builds take turns. Full builds are queued and run once at the end of a task; the fast `lint` renders only one course and does not take the lock.
- No shared history. Writers use only read-only Git commands; the orchestrator alone commits.
- Integration checks. A concept merged into the glossary from the plan may be defined by no chapter when the chapters are written in parallel, because each writer assumes another one is responsible. The orchestrator therefore runs `terms` for the whole course before declaring it complete, and writers report concepts that they only mention and that should be defined elsewhere.

### 14.9.5. Models and Cost

Writing, planning, polishing and overview pages use the main model; translation, adding R companions to plots, and adding concept links are dispatched to a lighter model, with the provision that the orchestrator redoes a task with the main model if review finds the quality insufficient. Translators are separate agents that read only the finished pages, the neighboring chapters and the glossary, not the original materials, which keeps their context small and makes the translation depend only on the reviewed text.

Several rules exist to keep context and time costs low. Materials are preprocessed into text, with low-resolution images only of pages whose text is insufficient, and writers read the text first, because images are expensive and their cost recurs on every later step. Tasks are sized so that a run interrupted by a usage limit is cheap to resume. And the tooling itself was optimized when it became the bottleneck: one commit made the full content build about four times faster (from about 620 to about 150 seconds, with byte-identical output), introduced the per-course `lint`, the source preprocessing and the safe glossary merge, and changed the guide to match: text-first reading, about one lecture per writer, translation by separate agents on a lighter model, and linting while writing with one full build at the end.

### 14.9.6. Sources and Safety

The course materials are copyrighted, while the repository is public. They are kept in a `sources/` directory that Git ignores except for its README, and they are deleted when a course is finished. Writers must never copy them into the content: figures are redrawn as formulas, tables, diagrams or plotting scripts with English text, and when an original figure seems necessary, the writer says so in the report and the orchestrator decides. The author's own statements about a course are recorded verbatim by the orchestrator in a request file and in the task sheets, so that the writers work from the author's words rather than from a paraphrase, and the guides forbid inventing anything personal. Because writers use only read-only Git commands, every change to the published history passes through the orchestrator's review and full check.

The general practices that this process instantiates:

| Practice in this repository | General principle |
|---|---|
| three guide files, one authoritative per subject, with an explicit conflict rule | short, authoritative instruction files (§14.4.2) |
| confirmed plan, task sheets with quoted plan rows, fixed report format | specifications as the interface; reports that make review targeted (§14.2, §14.5.1) |
| `fix`, `lint`, `terms`, `pnpm check`, CI | layered guardrails, fast inner loop, complete outer loop (§14.3.1) |
| new checks after repeated findings | from review findings to checks (§14.3.3) |
| page ownership, glossary proposals merged by a conflict-reporting script, build lock, read-only Git for writers | partitioned ownership and single owners of shared state (§14.5.2) |
| per-course `terms` before completion | integration checks for work that falls between tasks |
| lighter model for mechanical tasks, with escalation | model routing by judgment and checkability (§14.5.3) |
| questions relayed by the orchestrator; no invented personal facts | decision rights (§14.6) |
| copyrighted sources kept out of Git | separation of sensitive material (§14.8) |

## Summary

- Agents make construction cheap; specification, verification, review and integration become the bottleneck. Each property of an agent (no memory, guessing, speed, literal optimization of criteria, knowledge cutoff, susceptibility to injected instructions) has an engineering answer.
- Specifications at the project, feature and task levels are the interface between human decisions and agent execution; each fact has one authoritative place; executable specifications (tests, types, schemas) are checked on every change; open questions are reported, not guessed.
- Guardrails are automated checks independent of the author: formatters, linters, type checkers, tests, CI, protected branches, progressive rollouts. Fast checks drive the inner loop. Guardrails that an agent can edit must themselves be guarded; repeated review findings become new checks.
- Context engineering designs what an agent sees. Project instruction files are short, authoritative, specific, layered and kept true; costly or irreversible rules are enforced, not only stated; durable state lives in files.
- Work is decomposed into small, testable, reviewable tasks with scope, acceptance criteria and a report. Parallel agents follow the orchestrator–worker pattern with partitioned ownership, single owners of shared files, locks on shared resources, and integration checks after merge. Models are routed by task, with escalation.
- Humans hold the decisions about requirements, scope, personal facts and irreversible actions; review reads the diff and checks scope, test changes, dependencies and claims of verification first.
- Typical failures (hallucinated or outdated APIs, over-broad edits, test weakening, unperformed verification, symptom fixes, drift, fabrication, lost context) are caught by checks more reliably than by reading.
- Security rests on least privilege, isolation, keeping secrets and confidential material out of reach, and treating all untrusted text as data; break the "lethal trifecta" of private data, untrusted content and external communication.
- This knowledge base is written by this method: guide files as specifications, task sheets and reports as contracts, layered automated checks, parallel writers with page ownership and a single glossary owner, lighter models for mechanical work, and copyrighted sources kept outside the repository.
