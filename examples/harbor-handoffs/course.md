# Harbor handoffs: ownership, status, and evidence

Practice updating a task card, writing a complete handoff, and recording evidence for completion when engineering work changes hands.

**Audience:** Engineers new to Harbor; ordinary familiarity with tasks and reviews is enough.\
**Estimated time:** About 18 minutes, including three exercises; individual pace will vary.\
**Format:** English, one practical exercise per chapter, no quizzes. Use paper or a text editor.

Harbor is a fictional task tracker. This course uses only the supplied [Harbor team handbook, version 1.0](source/harbor.md). No account is needed. Task-card layouts and additional practice events are illustrative, and the linked practice records below are simulated.

## Course map

| Part | Capability | Time, including practice |
| --- | --- | --- |
| Orientation, above | Understand the task and format. | 1 minute |
| [1. Keep responsibility and progress accurate](#1-keep-responsibility-and-progress-accurate) | Update owner and status deliberately. | 5 minutes |
| [2. Write a handoff someone can act on](#2-write-a-handoff-someone-can-act-on) | Prepare a note and explicit field updates. | 6 minutes |
| [3. Close with evidence](#3-close-with-evidence) | Match acceptance conditions to evidence. | 6 minutes |

## 1. Keep responsibility and progress accurate

**Outcome:** Maintain a task card that describes who is responsible and what is happening. No earlier Harbor knowledge is required.

The owner is the one person responsible for the **next action**. A watcher receives updates without taking that responsibility.

Status describes progress separately from responsibility:

| Status | Meaning |
| --- | --- |
| Ready | Work can start, but nobody is actively doing it. |
| Active | The owner is working on the next action. |
| Waiting | Progress depends on an identified input or decision. |
| Done | Acceptance conditions are satisfied and evidence is linked. |

Acceptance conditions specify what the task's result must satisfy. Evidence supports the claim that those conditions were met; Chapter 3 makes this concrete.

Every status change is explicit. Changing the owner does not automatically make a task Active. Adding a watcher, writing a comment, or editing the description changes neither ownership nor status. Consequently, a comment saying work has started needs an explicit status update to keep the record accurate. [Source: Ownership and status](source/harbor.md#ownership-and-status).

### Worked example

In the handbook, Lea has drafted an onboarding page. It still needs a review and a verified working navigation link. Reviewer Omar is away. The team agrees that Mina will collect the review and verify navigation, and explicitly makes Mina the owner.

The resulting record is **owner: Mina; status: Waiting**. Mina owns the next action, while the required review remains a dependency. Omar's role as reviewer does not make him the task owner. Reassignment alone does not establish that work is Active. [Source: Example situation](source/harbor.md#example-situation).

### Practical exercise 1 — Update a task card

**Spend about 2 minutes.** At this illustrative earlier moment, Lea owns the Ready task, and Mina is a watcher. Lea starts the draft and comments, “I have started drafting.” No ownership change is agreed.

Write the updated task card with **owner, status, watchers, and a one-sentence current-action note**. Annotate which field needs an explicit update.

**Success criteria:** Lea remains owner, Mina remains a watcher, and the status is explicitly changed to Active. The note describes Lea drafting the page; it does not claim the comment changed status automatically.

This separates the two things a handoff must keep accurate: responsibility and progress.

## 2. Write a handoff someone can act on

**Outcome:** Create a useful handoff note and record the agreed owner and correct status. This builds on Chapter 1's independent owner and status fields.

The outgoing owner writes a note that lets the next owner continue without reconstructing the situation. It contains three elements:

1. **Current result:** Describe what exists and link the relevant artifact or task comment.
2. **Next concrete action:** Say what the next owner needs to do.
3. **Dependency:** Identify any needed person, input, or decision. If progress is blocked, name the unblock action.

The team agrees who takes the next action, then explicitly updates the owner. The note carries context; the owner field assigns responsibility. After that, choose the status from actual progress: Ready if work can start but has not, Active if the owner is working, or Waiting if a dependency blocks progress. [Source: Handoff notes](source/harbor.md#handoff-notes).

### Worked example

Return to the handbook's handoff from Lea to Mina. A note saying “Please finish this” would leave Mina to discover both remaining gaps. Lea instead needs to identify the draft, the required review, and the unchecked navigation link.

The next action is concrete: collect Omar's review and verify the navigation link. The blocked input is Omar's review; the unblock action is to obtain that required review when it can happen. Naming Omar here explains the dependency while Mina remains responsible for the next action.

The team has agreed on Mina, so Lea's handoff includes an explicit owner update to Mina. The task stays Waiting until the required review can happen. A note naming Mina or adding her as a watcher would not perform that transfer. [Sources: Handoff notes](source/harbor.md#handoff-notes), [Example situation](source/harbor.md#example-situation).

### Practice draft comment

**Simulated task comment for local practice:** The onboarding-page draft exists. Omar's required review is pending because he is away. The navigation link has not been checked. This record describes a draft, not completed work.

### Practical exercise 2 — Prepare the handoff

**Spend about 3 minutes.** Act as outgoing owner Lea. Replace the weak comment “Draft's up; Mina can take it” with a complete handoff using the situation above and this [practice draft comment](#practice-draft-comment). The team has agreed that Mina will collect the review and verify navigation.

Produce **one handoff note followed by the owner and status updates**. Include the actual Markdown link to the practice comment if working in a text editor.

**Success criteria:** Your note links the current result, names both next actions, identifies Omar's review as the dependency, and names obtaining that review as the unblock action. Record the explicit owner change from Lea to Mina and status Waiting. The unchecked navigation link remains visible as unfinished work.

Completion still needs evidence.

## 3. Close with evidence

**Outcome:** Document completion against acceptance conditions. This builds on the accurate task state and handoff context from Chapters 1–2.

Before setting Done, compare the result with every stated acceptance condition and link evidence. For this page, the two conditions are **a reviewed page** and **a working navigation link**. A draft or a review request does not establish either complete result. [Sources: Completion](source/harbor.md#completion), [Example situation](source/harbor.md#example-situation).

### Worked example

Consider an illustrative continuation: Omar reviews the page, but Mina checks navigation and discovers the link fails. The review condition is satisfied; the navigation condition is not. Setting Done would conceal that gap.

Suppose Mina is now actively fixing the link. Keep Mina as owner, explicitly set Active, and explain that navigation remains unfinished. If available work had not started, Ready would describe that state; a named blocking dependency would support Waiting. Incomplete work does not have one automatic fallback status. Choose the status describing the actual next action. [Sources: Completion](source/harbor.md#completion), [Ownership and status](source/harbor.md#ownership-and-status).

For the exercise, assume the repair and verification have now finished. These records are invented practice inputs, not observed actions:

### Practice review record

Omar reviewed the final onboarding page. No requested changes remain.

### Practice navigation record

Mina followed the navigation link and confirmed that it opens that same final onboarding page successfully.

### Practical exercise 3 — Write the completion update

**Spend about 3 minutes.** Mina still owns the task, with no further handoff. Use the two practice records to produce **an acceptance-to-evidence table and a completion note containing the owner and status**. Link each condition to its supporting record: [review](#practice-review-record) and [navigation](#practice-navigation-record).

**Success criteria:** The table covers both acceptance conditions with the relevant evidence link. The note records owner Mina and an explicit status change to Done because both conditions are satisfied. It bases completion on those results, rather than the earlier draft or transfer of ownership.

## Source coverage

All Harbor rules and the original Lea–Mina–Omar situation come from the [supplied handbook](source/harbor.md). The [source record](sources.md) documents coverage and teaching adaptations. UI instructions, APIs, permissions, integrations, and reopening are outside the supplied material. The course teaches the handbook's workflow through local practice and does not verify a live service.
