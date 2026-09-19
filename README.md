# Coursecraft

**Turn a topic or a collection of sources into a course worth learning from.**

Coursecraft researches a subject, establishes a learning sequence, and writes connected lessons with examples and source references. Add review questions, practical exercises, or quizzes when they help. The result is plain Markdown you can read, edit, share, or prepare for publishing with Unpage.

This is a skills plugin for an AI assistant. It uses the host's model, research tools, and file tools; it has no separate service, model subscription, API key, or database to configure. Your host's normal access requirements and usage limits still apply.

## Quick start

Clone the repository:

```bash
git clone https://github.com/bpstr/coursecraft.git
cd coursecraft
```

Choose the instructions for your host. The commands below use a macOS/Linux shell.

### Codex CLI or IDE extension

Install the complete skill folder for your user:

```bash
mkdir -p "$HOME/.agents/skills/coursecraft"
cp -R skills/coursecraft/. "$HOME/.agents/skills/coursecraft/"
```

Start Codex in the directory where you want the course saved, then enter:

```text
$coursecraft openai
```

For a more focused course:

```text
$coursecraft Build an AI assistant with tools.
Audience: PHP developers new to AI APIs.
Length: a few evenings.
Include practical exercises and a final quiz.
```

Codex discovers user skills in `~/.agents/skills/`; use `$` or `/skills` to select one. If it does not appear, restart Codex. For a project installation, copy the same folder into that project's `.agents/skills/coursecraft/`. These are the documented [Codex skill locations and invocation methods](https://learn.chatgpt.com/docs/build-skills).

### Claude Code plugin

Load the repository as a local plugin from its root:

```bash
claude --plugin-dir .
```

Then enter:

```text
/coursecraft:coursecraft openai
```

To write a course in a different workspace, start Claude Code there with `--plugin-dir /absolute/path/to/coursecraft`. Local loading needs no marketplace. Claude Code namespaces plugin skills as `/plugin-name:skill-name`; see its [plugin quick start](https://code.claude.com/docs/en/plugins#quickstart).

### Claude Code standalone skill

If you prefer the shorter `/coursecraft` command, copy the skill instead of loading the plugin:

```bash
mkdir -p "$HOME/.claude/skills/coursecraft"
cp -R skills/coursecraft/. "$HOME/.claude/skills/coursecraft/"
```

Start Claude Code in your working directory, then enter:

```text
/coursecraft openai
```

This uses Claude Code's [personal skill location](https://code.claude.com/docs/en/skills#choose-where-skills-load). Choose one installation method per host to avoid duplicate entries. Copy all supporting files when installing or updating; merge any changes you made to an existing installed copy.

The repository also includes a Codex plugin manifest. See [host compatibility](docs/compatibility.md) for plugin packaging, distribution, and the limits of what has been verified.

## What you can ask for

Examples below use the standalone Claude syntax. Replace `/coursecraft` with `$coursecraft` in Codex, or `/coursecraft:coursecraft` when loaded as a Claude Code plugin. These are assistant prompts, not shell commands.

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

The default destination is `courses/<slug>/` in your working directory, unless you choose another destination or the host requires its own artifact storage.

| File | Contents |
| --- | --- |
| `course.md` | The readable course, with navigation, lessons, examples, and references |
| `outline.md` | Audience, learning outcomes, prerequisites, and chapter sequence |
| `sources.md` | Source records, what they support, verification dates, and known gaps |

An outline-only request saves `outline.md` and `sources.md` without writing lessons. A larger course can use `index.md` and a `chapters/` directory in place of `course.md`, with the same outline and source records. Study and quiz sessions use an existing course as context and happen in the host conversation.

Coursecraft produces editable learning material, so you can revise the outline, ask for a different explanation, or add a chapter without adopting a separate learning platform. It does not provide learner accounts, persistent grades, enrollment, or certificates.

See the [Harbor handoffs example course](examples/harbor-handoffs/course.md), built from the repository's [fictional source material](examples/source-material/harbor.md), for a complete output example.

## Unpage compatibility

The publishing boundary is Markdown. A course can be a single document with chapter headings, or an overview linking to chapter documents. Source references are ordinary links, and code examples use fenced blocks.

This release prepares files for that workflow. An Unpage API/MCP publisher is not implemented. Review the generated document and publish through the tools available in your Unpage setup; there are no invented endpoints or hidden upload steps. See [the compatibility notes](docs/compatibility.md#unpage-and-markdown) for the exact scope.

## Repository

| Path | Purpose |
| --- | --- |
| `.codex-plugin/plugin.json` | Codex plugin metadata |
| `.claude-plugin/plugin.json` | Claude Code plugin metadata |
| `skills/coursecraft/` | Shared skill instructions and supporting resources |
| `examples/` | Source material and a sample course |
| `docs/compatibility.md` | Installation assumptions, host behavior, and publishing limits |
| `scripts/validate.py` | Manifest, skill metadata, and resource-reference validation |
| `tests/` | Validator regression tests |

## Development checks

From the repository root, with Python 3.11 or later installed:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These are maintainer checks; Python is not required to use the skill's writing workflow. Installation instructions are checked against official host documentation. The [compatibility notes](docs/compatibility.md#what-verification-establishes) distinguish package validation from live client and course-quality testing.
