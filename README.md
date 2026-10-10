# ClankTeam

A free, open Claude Code skill for running a small business or side project
with AI help: a CEO agent that reads the business's own goals and memory,
delegates real work to specialist worker agents, and reports back every
cycle. Built as the honest version of the "AI runs your company while you
sleep" pitch: owned outright, no revenue share, and structurally incapable
of sending, posting, or spending on its own.

Full behavior documentation lives in [`SKILL.md`](SKILL.md): that's the
file Claude Code actually reads. This README is the human-facing front door.

## Why this exists

Products like Polsia sell this pattern for $20-49/month plus a cut of your
revenue and ad spend, with no stable published pricing (it's changed inside
the product at least four times in 2026, per public reporting). The
underlying mechanism, an orchestrator agent delegating to specialist agents
on a schedule, isn't proprietary. Claude Code already has the subagent and
scheduling primitives to do it directly.

The part that actually matters isn't the automation. It's the discipline
around it. Autonomous-business tools have real, documented failure modes:
agents making commitments a human never agreed to, outreach that doesn't
identify itself honestly, marketing copy that invents a customer or a
testimonial because that's what a launch post "should" sound like.
ClankTeam is built around one hard rule, stated plainly: **nothing it
produces ever sends, posts, publishes, or spends on its own.** It drafts, researches, and
reports. A person decides what leaves the building.

## Install

Clone or copy this repo into `~/.claude/skills/clankteam/`:

```sh
git clone https://github.com/HaveMindHive/clankteam-skill.git ~/.claude/skills/clankteam
```

Claude Code picks up skills from that location automatically.

## Use

```
/clankteam init <business-name>     # scaffold a new business
/clankteam run <business-name>      # run one CEO + Marketing cycle
/clankteam status <business-name>   # see where things stand
/clankteam approve <business-name>  # review the approval queue
/clankteam schedule <business-name> # wire up recurring runs
```

Plain language works too: "set up an AI-run business for my newsletter,"
"run tonight's cycle," "what's waiting for my approval." The skill is
written to trigger on intent, not just exact command syntax.

Read [`reference/growing-the-team.md`](reference/growing-the-team.md) before
adding more worker agents, multi-business support, or (much later, much more
carefully) any real send/post/spend integration. None of that is in v1 on
purpose: it's deliberately minimal, one CEO agent, one Marketing worker,
report-only.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). This is meant to be a community
project: new worker-agent templates, safety-gate improvements, and
real-world usage reports are all welcome. The one hard line: nothing that
makes an outward-facing action happen without an explicit human approval
step gets merged, no matter how useful it is otherwise.

## License

MIT. See [`LICENSE`](LICENSE).
