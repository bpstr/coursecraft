# Coursecraft

**Turn a topic or a collection of sources into a course worth learning from.**

Coursecraft researches a subject, establishes a learning sequence, and writes connected lessons with examples and source references. Add review questions, practical exercises, or quizzes when they help. The result is plain Markdown you can read, edit, share, or prepare for publishing with Unpage.

Coursecraft is packaged as a native AI plugin. It uses the host's model, research tools, and file tools; there is no separate service, model subscription, API key, or database to configure.

## Install

### ChatGPT and Codex

**Install Coursecraft from the plugin directory.**

Once Coursecraft is available in your account or workspace, install/select it from the host's plugin UI and start using it in a conversation. There is no repository clone, shell installer, or manual skill copy in the normal user flow.

For example:

```text
/coursecraft openai
```

Or simply ask Coursecraft:

```text
Create a course that teaches me how to build an AI assistant with tools.
Audience: PHP developers new to AI APIs.
Length: a few evenings.
Include practical exercises and a final quiz.
```

The exact invocation UI can vary by host surface. Selecting the installed Coursecraft plugin is the canonical route; command-style examples describe the intended action rather than requiring a shell command.

### Claude Code

Coursecraft also includes native Claude Code plugin packaging. Distribution through Claude's plugin ecosystem is the intended user installation path. Local checkout loading is documented under [Development and local testing](#development-and-local-testing), not as the normal install experience.

> **Distribution status:** the repository contains the native plugin manifests and package, but a GitHub repository alone does not publish a plugin into a host directory. Until Coursecraft is submitted/approved and made available by the relevant host, the native listing may not yet be visible.

See [host compatibility](docs/compatibility.md) for the packaging and distribution boundary.

## What you can ask for

These examples use `/coursecraft` as shorthand for invoking the installed plugin. You can also select Coursecraft and ask the same thing naturally.

| Request | Example |
| --- | --- |
| Research a topic and write a course | `/coursecraft openai` |
| Specify an outcome and audience | `/coursecraft Teach a PHP developer how to design reliable background jobs` |
| Work from your own material | `/coursecraft Turn README.md and docs/architecture.md into a new developer onboarding course. Use only these sources.` |
| Review the structure first | `/coursecraft outline Git for a designer who has never used a terminal` |
| Add selected practice | `/coursecraft HTTP caching for backend developers. Include exercises and a final quiz, but no chapter quizzes.` |
| Learn from an existing course | `/coursecraft study courses/http-caching/course.md` |
| Check your understanding | `/coursecraft quiz courses/http-caching/course.md` |

You can supply a topic, a learning goal, local documents, readable URLs, or a mixture. For a broad request, Coursecraft establishes the intended audience and outcome before committing to a large course. For a specific request, it proceeds using your stated constraints. Ask for `outline` when you want the structure alone. Questions, exercises, and quizzes are off by default and can be selected independently.

## How the course is built

1. **Set the learning goal.** Establish the learner's starting knowledge, desired outcome, scope, and optional practice.
2. **Research the material.** Read relevant sources, prefer primary documentation for technical claims, and record what was actually checked. Supplied-source requests stay within the requested material.
3. **Design the progression.** Arrange prerequisites and chapters so each outcome prepares the learner for the next step.
4. **Write connected lessons.** Use explanations, worked examples, consistent terminology, and optional practice tied to what was taught.
5. **Review and deliver.** Check coverage, navigation, citations, examples, and answer consistency, then save the course and its supporting records.

The host needs access to the supplied files or URLs and a way to write the result. Fresh topic research needs suitable web or documentation tools. If those tools or sources are unavailable, Coursecraft identifies the gap rather than claiming fresh verification. A course based entirely on supplied documents does not require web research unless you request it.

## Output

On coding hosts with a working directory, the default destination is `courses/<slug>/`, unless you choose another destination. Other host surfaces can return or save the same Markdown through their normal artifact workflow.

| File | Contents |
| --- | --- |
| `course.md` | The readable course, with navigation, lessons, examples, and references |
| `outline.md` | Audience, learning outcomes, prerequisites, and chapter sequence |
| `sources.md` | Source records, what they support, verification dates, and known gaps |

An outline-only request produces the outline and source record without writing lessons. A larger course can use an index and chapter documents instead of one course document. Study and quiz sessions use an existing course as context and happen in the host conversation.

Coursecraft produces editable learning material, so you can revise the outline, ask for a different explanation, or add a chapter without adopting a separate learning platform. It does not provide learner accounts, persistent grades, enrollment, or certificates.

See the [Harbor handoffs example course](examples/harbor-handoffs/course.md), built from the repository's [fictional source material](examples/source-material/harbor.md), for a complete output example.

## Unpage compatibility

The publishing boundary is Markdown. A course can be a single document with chapter headings, or an overview linking to chapter documents. Source references are ordinary links, and code examples use fenced blocks.

This release prepares files for that workflow. An Unpage API/MCP publisher is not implemented. Review the generated document and publish through the tools available in your Unpage setup; there are no invented endpoints or hidden upload steps. See [the compatibility notes](docs/compatibility.md#unpage-and-markdown) for the exact scope.

## Development and local testing

You do **not** need this section to use a natively distributed Coursecraft plugin. These instructions are for contributors and pre-distribution testing.

Clone the repository:

```bash
git clone https://github.com/bpstr/coursecraft.git
cd coursecraft
```

For Codex standalone skill testing:

```bash
mkdir -p "$HOME/.agents/skills/coursecraft"
cp -R skills/coursecraft/. "$HOME/.agents/skills/coursecraft/"
```

For Claude Code local plugin testing:

```bash
claude --plugin-dir .
```

For Claude Code standalone skill testing:

```bash
mkdir -p "$HOME/.claude/skills/coursecraft"
cp -R skills/coursecraft/. "$HOME/.claude/skills/coursecraft/"
```

Use one local route per host to avoid duplicate entries. These are development fallbacks; native plugin distribution remains the intended installation experience.

### Repository checks

With Python 3.11 or later:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These checks validate package structure and resource references; they do not prove directory publication or live-client compatibility.

## Repository

| Path | Purpose |
| --- | --- |
| `.codex-plugin/plugin.json` | ChatGPT/Codex plugin metadata |
| `.claude-plugin/plugin.json` | Claude Code plugin metadata |
| `skills/coursecraft/` | Shared skill instructions and supporting resources |
| `examples/` | Source material and a sample course |
| `docs/compatibility.md` | Distribution, host behavior, and publishing limits |
| `scripts/validate.py` | Manifest, skill metadata, and resource-reference validation |
| `tests/` | Validator regression tests |

Coursecraft is MIT licensed.
