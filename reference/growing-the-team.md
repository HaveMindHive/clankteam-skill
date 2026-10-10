# Growing past the minimal loop

Everything here assumes the CEO + Marketing loop in SKILL.md has actually
run a few times, a human has reviewed what it produced, and the memory
files show it's learning rather than repeating itself. If that's not true
yet, go run it a few more times before adding anything from this file.
More agents on a loop nobody trusts yet just means more unreviewed drafts.

## Adding specialist agents

The pattern is the same for each: a short role prompt, a narrow set of
facts it's allowed to act on, and a single kind of output it hands back to
the CEO for the report/approval-queue step. Don't give a new agent access
to anything the CEO itself doesn't already read from `business.yaml` and
`memory/`.

- **Engineering**: works in a real git repo via branches/PRs a human
  merges, never pushes to a default branch directly. Good first addition
  once Marketing is trusted, since code changes are inherently reviewable
  (a diff) in a way marketing copy sometimes isn't.
- **Growth / Outreach**: researches and drafts outreach to named, real
  targets (never a fabricated or guessed contact). Everything it produces
  goes through the same approval queue as Marketing's output. Outreach is
  exactly the "outward-facing" category the approval gate exists for.
- **Support**: drafts replies to real inbound questions (pulled from
  wherever support requests actually come in). Approval gate still applies
  until you've built real confidence in its judgment on tone and accuracy.
- **Finance / Reporting**: reads real numbers (read-only access to
  whatever the business's actual metrics source is) and writes them into
  the cycle report. This is the one role where read-only access to a real
  system is reasonable before the approval-gate threshold matters, since it
  can't take an action, only report one.

## Scoped credentials

Once any agent needs a real credential (an email account, a Stripe key, an
ads account), give that credential to that agent's invocation only, scoped
as narrowly as the task allows, never a project-wide secret every agent
can read. A sandbox around an agent's reasoning doesn't constrain what its
credential can do; the credential's own scope is the real boundary. A key
that can only read analytics should never also be able to send a campaign.

## Multi-business

Each business is already a self-contained directory, so running several is
mostly a matter of running `/clankteam run <business-name>` for each one on
its own schedule, not a shared orchestrator across businesses. Keep that
separation. A bug or a bad decision in one business's loop shouldn't be
able to touch another's files or credentials.

## When (and whether) to automate sending

This is the biggest step past the v1 design, and it's the one to be most
deliberate about. Before wiring up a real send/post/spend integration for
anything:

- The approval queue should have a real track record: enough cycles that
  you can say with some confidence what a human usually approves vs.
  rejects, and why (that pattern lives in `memory/learnings.md` if it's
  been kept up).
- Pick the narrowest possible action to automate first (e.g. "send this one
  pre-approved weekly newsletter template" is a much smaller trust step
  than "send any email a worker agent drafts").
- Keep a kill switch (one file or flag that halts all runs), and keep
  spend capped wherever money is involved, hard-failing rather than
  guessing when a cap is hit.
- Even after automating a send step, keep logging everything that goes out
  somewhere a human can audit after the fact. Removing the approval gate
  for one narrow, trusted action is not the same as removing the audit
  trail.

None of this is in the v1 skill on purpose. Build it when there's a real
track record to build it on, not on day one because the pattern allows it.
