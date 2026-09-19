# Harbor team handbook

Harbor is a fictional task tracker used for this Coursecraft example. This document
is supplied training material, version 1.0. It is the complete source for the
example; it does not describe a real service or require an account.

## Ownership and status

Each task has one owner: the person responsible for the next action. Watchers
receive updates but do not become responsible for the task. Adding a watcher,
posting a comment, or editing a description never changes ownership or status.

| Status | Meaning |
| --- | --- |
| Ready | The task can be started; nobody is actively doing it yet. |
| Active | The owner is currently working on the next action. |
| Waiting | Progress depends on an identified input or decision. |
| Done | The stated acceptance conditions are met and evidence is linked. |

All status changes are explicit. Assigning a different owner does not move a task
to Active. A task can have an owner while Ready or Waiting. A review request
alone does not make a task Done.

## Handoff notes

When work changes hands, the outgoing owner writes a note containing:

1. The current result, with a link to the relevant artifact or task comment.
2. The next concrete action.
3. Any dependency, including the person or decision needed to resolve it.

The team agrees who will take the next action, then explicitly updates the owner.
The note records the context; the owner field records responsibility. If the new
owner has not started yet, use Ready. If they are working, use Active. If progress
is blocked by a dependency, use Waiting and name the unblock action in the note.

## Completion

Before setting Done, compare the result with the task's acceptance conditions and
link evidence. A draft, a handoff, or an unverified claim of success is insufficient.
If checking reveals unfinished work, keep the task in the status that describes
the actual next action and explain the gap.

## Example situation

Lea owns a task to publish an onboarding page. The acceptance conditions require a
reviewed page and a working navigation link. The draft exists, but reviewer Omar
is away and the navigation link has not been checked. Lea writes a note naming
both gaps. The team agrees that Mina will collect the review and verify the link.
Mina becomes the owner. Until the required review can happen, the task is Waiting.
