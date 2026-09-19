# Host and output compatibility

Coursecraft contains one shared skill with separate native plugin manifests for ChatGPT/Codex and Claude Code. The workflow is expressed in Markdown instructions and supporting resources. The host supplies the model, tools, authentication, permissions, and conversation interface.

The intended user experience is **native plugin distribution**: users install Coursecraft from the plugin directory or other host-provided plugin UI. Repository checkout, skill copying, and local plugin loading are development and pre-distribution testing mechanisms only.

Packaging guidance was checked against official documentation on **2026-09-19**. Package checks validate manifests, skill metadata, and skill resource references; they do not establish that a plugin has been accepted into a directory or exercised in every host/client version.

## Distribution model

| Host | Primary user path | Package entry | Development fallback |
| --- | --- | --- | --- |
| ChatGPT / Codex plugin surfaces | Install/select Coursecraft through the native plugin UI | `.codex-plugin/plugin.json` with `skills/` | Local marketplace/plugin testing or standalone skill |
| Claude Code plugin surfaces | Install Coursecraft through the native plugin ecosystem | `.claude-plugin/plugin.json` with `skills/` | `claude --plugin-dir /absolute/path/to/coursecraft` |
| Codex standalone skill | Not the primary distribution path | `skills/coursecraft/` | Copy to `~/.agents/skills/coursecraft/` or project `.agents/skills/coursecraft/` |
| Claude Code standalone skill | Not the primary distribution path | `skills/coursecraft/` | Copy to `~/.claude/skills/coursecraft/` or project `.claude/skills/coursecraft/` |

A GitHub repository and valid manifest are packaging prerequisites, not publication. Native availability still depends on the host's distribution, submission, review, workspace, and/or marketplace process. The repository therefore must not tell ordinary users that cloning it is required to install Coursecraft.

OpenAI documents plugin construction and distribution in [Build plugins](https://learn.chatgpt.com/docs/build-plugins#create-a-plugin-with-plugin-creator) and [Plugins](https://learn.chatgpt.com/docs/plugins). Codex standalone skills remain useful for development and are documented in [Build skills](https://learn.chatgpt.com/docs/build-skills). Claude Code documents [plugins](https://code.claude.com/docs/en/plugins#quickstart) and [skills](https://code.claude.com/docs/en/skills#choose-where-skills-load).

## Invocation

Native plugin selection is the canonical invocation mechanism. Documentation may use `/coursecraft <request>` as readable shorthand for “invoke the installed Coursecraft plugin with this request”; it must not imply that every host exposes that exact command syntax.

Host-specific development invocation can differ:

- Codex standalone skill: `$coursecraft <request>`.
- Claude Code local plugin: `/coursecraft:coursecraft <request>`.
- Claude Code standalone skill: `/coursecraft <request>`.

When Coursecraft is installed natively, prefer the host's plugin selector, mention, command, or conversation UI rather than asking users to know filesystem locations.

## Development and local testing

Local installation exists to test a checkout before native distribution.

For Codex, a standalone development copy can live in `~/.agents/skills/coursecraft/` or a project's `.agents/skills/coursecraft/`. Copy the complete `skills/coursecraft/` directory, including supporting resources. See [local skill discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

For Claude Code, `--plugin-dir` loads this repository as a local plugin for a session. Invoke that development plugin as `/coursecraft:coursecraft`. A standalone development copy can instead live in `~/.claude/skills/coursecraft/`. See [local plugin testing](https://code.claude.com/docs/en/plugins#test-your-plugins-locally).

Use one development route per host. Loading both the plugin and standalone skill can expose duplicate Coursecraft entries.

## ChatGPT/Codex packaging

The `.codex-plugin/plugin.json` manifest is the native package metadata. The package includes the shared `skills/` tree and intentionally has no installer script or runtime bootstrap service.

For pre-publication plugin testing, use the host's supported local marketplace/plugin development flow. Public or workspace distribution is a separate host-side step; this repository does not claim that Coursecraft is currently listed merely because the manifest exists.

The README should be written from the eventual user's perspective:

1. Install Coursecraft from the native plugin directory.
2. Select/invoke Coursecraft.
3. Ask for a course.

Clone/copy instructions belong under development, not Quick Start.

## Tools and execution

Coursecraft has no runtime service or bundled MCP server. It does not store provider credentials or make independent model requests. The host executes its instructions with the capabilities available in that session.

| Capability | Needed for |
| --- | --- |
| Reading local files or attachments | Courses based on supplied documents; loading an existing course |
| Web search and page/document retrieval | Researching a topic and checking current external claims |
| Writing files or saving artifacts | Delivering the Markdown course and supporting records |
| Conversation turns | Clarification, guided study, and interactive quizzes |

Connected private sources remain subject to the host's access controls. If a source cannot be read, the workflow must mark that limitation. Search results alone do not establish that the underlying page was inspected. Without web research tools, Coursecraft can use accessible supplied material and explain what it could not verify.

Study and quiz are conversational workflows. A host may offer richer quiz widgets, but Coursecraft does not require a proprietary widget format. Session persistence and recall follow the host's behavior; the plugin does not implement a learner database or a gradebook.

## Unpage and Markdown

Coursecraft's integration contract is readable Markdown:

- A default `course.md` can be treated as one published document.
- `outline.md` and `sources.md` retain the course plan and source audit information.
- Larger courses may use an overview with links to separate chapter documents.
- Headings, lists, standard links, and fenced code blocks carry the content without a custom application runtime.

Compatibility here means the output is suitable for a Markdown document workflow. It does not claim an Unpage upload API, MCP tool, authentication scheme, course import format, or successful publication. Those integrations are not part of this release.

Before publishing separate chapter documents, resolve their relative links to the destination URLs and check that heading anchors match the renderer. Review linked local resources as well: a local path is not a public source URL. Keep any answer material you want learners to avoid outside the learner-facing document.

## What verification establishes

The repository validator checks manifests, skill metadata, and references to skill resources. It does not validate native directory publication, host approval, course artifacts, all documentation links, external source availability, or generated explanations. Those need separate review. A structural check also cannot prove that a live assistant will follow every instruction.

For a host smoke test, create a short course from accessible supplied material, then confirm:

1. The intended Coursecraft plugin/skill loaded and its supporting resources were available.
2. The requested output exists in the host's expected artifact or filesystem destination.
3. The course follows the outline and cites the supplied material accurately.
4. Optional practice appears only when requested, with answers consistent with the lessons.
5. Study or quiz mode uses the saved course rather than inventing its contents.

No live directory publication or client execution is claimed by the repository documentation itself.
