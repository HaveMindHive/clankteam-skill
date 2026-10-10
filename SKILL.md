---
name: clankteam
description: Set up and run an AI-operated business or side project: a CEO agent that reads the business's own memory and goals, delegates real work to specialist worker agents (starting with Marketing), and writes a status report every cycle, with a hard human-approval gate on anything outward-facing (sending email, posting, publishing, spending money) so nothing ever goes out without a person signing off first. Use this whenever the user wants to automate running a business, side hustle, or project; mentions "AI-run business," "autonomous business," "AI employee," or an agent that works while they sleep; wants a recurring/nightly agent that handles marketing, outreach, or content for them; mentions ClankTeam by name; or describes wanting something like Polsia, Lindy, or a similar "AI runs your company" product but without a revenue-share SaaS middleman. Also trigger for "set up a business workspace for Claude to run," "scaffold a new ClankTeam business," "what's my business's status," or "run tonight's cycle" once a ClankTeam business already exists in the project.
---

# ClankTeam

An honest version of the "AI runs your business while you sleep" pitch. The
products that sell this (Polsia and others) charge a monthly fee plus a cut
of revenue and ad spend for something that is mostly API calls wrapped in a
dashboard. ClankTeam does the same underlying work (an orchestrator agent
that delegates to specialist agents on a schedule) using Claude Code's own
subagent and scheduling tools directly, owned outright by whoever runs it.

The honest part matters more than the automation part. The two products this
pattern is modeled on have real, documented failure modes: agents that make
commitments a human never agreed to, outreach that doesn't identify itself
truthfully, founders discovering only ~10% of autonomously-run companies ever
earn a dollar. None of that is a reason not to build this. It's the reason
every outward-facing action here stops at a human before it goes anywhere.
**No step in this skill ever sends an email, posts anything, publishes
anything, or spends money on its own.** It drafts, researches, and reports.
A person decides what leaves the building.

## Before you start

**Build the smallest version first, then grow it.** A business that runs a
CEO + one worker agent cleanly for a week, with a human reviewing every draft
it produces, is worth more than a six-agent system nobody has watched work
yet. This skill's default (`init`) sets up exactly that minimal loop: a CEO
agent and a Marketing agent, report-only. Don't reach for more agents,
auto-approval, or real send/spend integrations until that loop has actually
run a few times and the human running it trusts what it produces. When
that's true, `reference/growing-the-team.md` covers adding Engineering,
Growth, Support, Finance agents, multi-business management, and what it
takes to responsibly wire up a real send/payment integration later.

**Never fabricate.** A worker agent drafting marketing copy, an outreach
message, or a report must never invent a customer, testimonial, metric,
review, or result that isn't grounded in something actually in the
business's own memory files. If a number or claim isn't confirmed, the draft
says so plainly (e.g. "benchmark pending" or "no customers yet") instead of
writing around the gap. This is the single most important rule in this
skill. An AI-run business that lies to look more finished than it is will
get caught, and it should.

## Commands

- **`/clankteam init <business-name>`**: scaffold a new business workspace
  in the current directory.
- **`/clankteam run <business-name>`**: run one CEO + Marketing cycle.
- **`/clankteam status <business-name>`**: summarize the business's current
  state: last report, what's pending approval, recent decisions.
- **`/clankteam approve <business-name>`**: walk through everything sitting
  in the approval queue with the human, one item at a time.
- **`/clankteam schedule <business-name>`**: wire up a recurring cycle using
  Claude Code's own scheduling, not a custom cron reimplementation.

A request in plain language ("set up an AI-run business for my newsletter,"
"run tonight's cycle for acme-widgets," "what did ClankTeam do last night")
maps to the matching command above. Don't make the user learn the slash
syntax if they didn't use it.

## Directory layout

Each business is a plain, inspectable directory: markdown and YAML, nothing
hidden, easy to read in a diff:

```
<business-name>/
  business.yaml       # goals, audience, voice, constraints: the facts
  memory/
    decisions.md       # append-only log: what was decided, and why
    learnings.md        # what was tried, what happened, what to do differently
  approvals/
    pending.md          # drafts awaiting a human's yes/no
    approved.md          # signed-off drafts (still not sent, see note below)
    rejected.md           # declined drafts, with the human's reason if given
  reports/
    <YYYY-MM-DD>.md        # one file per cycle
```

In this minimal (v1) setup, "approved" only means a human confirmed the
draft is good. There is no send/post/publish integration wired up yet, so
approval is a record, not a trigger. That's deliberate: build the judgment
loop first, wire up real actions only once you trust what it's approving.

## `init`: scaffold a business

Run `scripts/init_business.py <business-name>` from the directory the user
wants the business to live in (default: their current working directory,
unless they name another path). It creates the layout above from the
templates in `templates/`, with `business.yaml` left mostly blank for the
human to fill in. **Don't guess their goals, audience, or voice; ask.**

After scaffolding, interview the user for `business.yaml`'s fields if they
haven't given you this already in conversation:
- What does this business do, in one sentence?
- Who is it for, and what are they trying to accomplish when they find it?
- What's the goal for the next cycle or two, not "grow the business," but
  something concrete enough that a worker agent can act on it this week?
- Brand voice or tone constraints, if any.
- Anything explicitly off-limits (claims not to make, channels not to use,
  topics to avoid).

Write their answers into `business.yaml` yourself; don't hand them a form.

## `run`: one CEO + Marketing cycle

This is the core loop, and it's reasoning, not a script: read the business's
state, then act as the CEO:

1. **Read the business's current state**: `business.yaml`, both memory
   files, the most recent report (if one exists), and `approvals/pending.md`
   (so you don't re-draft something already waiting on the human).
2. **Pick ONE priority for this cycle.** Not a list, not "grow engagement,"
   one concrete, achievable thing a worker agent could meaningfully move
   forward today, chosen from the business's stated goals and informed by
   `learnings.md` (don't repeat something that's already been tried and
   logged as not working, unless you have a real reason to try it
   differently this time).
3. **Delegate to a Marketing worker agent** using the Agent tool. Give it:
   the business's facts from `business.yaml`, the chosen priority, the
   no-fabrication rule above (restate it explicitly in the subagent's
   prompt; don't assume it inherits your instructions), and instructions
   to produce a draft (content, outreach message, etc.) rather than take
   any outward action itself. A fresh subagent has no memory of this
   conversation, so give it everything it needs to act well, not a vague
   pointer back to files it may not read closely.
4. **File the output.** Append the worker's draft to `approvals/pending.md`
   with a timestamp, a short label, and what it's for. Never send, post, or
   publish it. That's not this skill's job yet.
5. **Write the cycle's report** to `reports/<date>.md`: what you prioritized
   and why, what the worker produced, what's now waiting on human approval,
   and a one-line plan for next cycle. Keep it to the length a person would
   actually read before coffee: a few short paragraphs, not a dump of
   everything that happened.
6. **Update `memory/decisions.md`** with what was decided this cycle and the
   reasoning, so the next cycle (and the next person reading this file)
   understands why, not just what.

If there's nothing good to prioritize (no clear next step, or everything
promising is already in the approval queue awaiting a human), say so in the
report instead of manufacturing busywork. An honest "nothing urgent, here's
what's pending" report is more useful than padding.

## `approve`: human review

Read `approvals/pending.md`. For each item, show the human what it is and
the full draft content, then ask approve or reject (a structured question
tool if one is available; otherwise ask and wait for a clear answer). Move
approved items to `approved.md` and rejected ones to `rejected.md`,
preserving any reason the human gives for a rejection. That reason belongs
in `memory/learnings.md` too, since it's exactly the kind of signal the next
cycle should act on.

## `schedule`: recurring runs

Don't reimplement scheduling. If the `schedule` skill or Claude Code's own
cron/scheduled-task capability is available, use it to run `/clankteam run
<business-name>` on whatever cadence the human wants (nightly is the
default Polsia-style cadence, but ask: a slower cadence is often more
honest about how much there actually is to do). Confirm the cadence with
the human before setting anything recurring; don't assume nightly just
because that's the category default.

## Why the approval gate is non-negotiable

This isn't caution for its own sake. The products this pattern is modeled
on have a documented failure case: an agent scheduled a call with a
journalist and then didn't show up, because nothing stopped it from making
a commitment a human hadn't actually agreed to. The fix isn't "make the
agent more careful." It's structural: an agent that can only draft,
and a human who decides what's real, can't fail that way. Keep that
property even as you grow past the v1 scope in
`reference/growing-the-team.md`.
