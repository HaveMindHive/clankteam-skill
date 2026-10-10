# Contributing to ClankTeam

This is meant to be a community skill, not a one-person project. Contributions
of all sizes are welcome: a typo fix is as welcome as a new worker-agent
template.

## What's especially useful

- **New worker agent templates** (Support, Finance, Engineering, Growth;
  see `reference/growing-the-team.md` for the pattern each one should follow).
- **Real-world usage reports**: what happened when you actually ran this for
  a real business for a week. The brief that started this project exists
  because the commercial products in this space don't publish honest numbers
  (most autonomously-run businesses never make a dollar); this project should.
- **Safety and approval-gate improvements**. This is the part that matters
  most. If you find a way the approval gate could be bypassed, or a scenario
  where a worker agent could plausibly fabricate a claim despite the current
  instructions, that's a high-priority issue, not a nitpick.
- **Integration recipes** for `reference/growing-the-team.md`'s "wiring up a
  real send/spend integration" section, written so someone else can follow
  them carefully, not just "here's how I did it."
- Bug reports, typo fixes, clearer wording in `SKILL.md`.

## Ground rules

- **Keep the human-approval gate non-negotiable in anything you contribute.**
  A PR that makes any outward-facing action (sending, posting, publishing,
  spending) happen without an explicit human approval step won't be merged,
  no matter how useful the feature is otherwise. This is the one hard line
  in the project.
- **No fabrication, anywhere in the skill's own instructions or examples.**
  If you add an example business or sample output, make clear what's
  illustrative vs. a claim the skill would actually be allowed to make about
  a real business with no customers yet.
- Keep `SKILL.md` lean. If your contribution needs more than a few lines of
  explanation, it probably belongs in `reference/` with a pointer from
  `SKILL.md`, not inline.
- Scripts belong in `scripts/` only for genuinely deterministic, repeated
  work (file scaffolding, formatting), not for anything that requires
  judgment, which belongs in the skill's instructions instead.

## How to contribute

1. Open an issue first for anything beyond a small fix, so the approach gets
   discussed before the work does.
2. Fork, branch, make your change.
3. If you're changing `SKILL.md` or any instruction file, actually run the
   skill against a realistic prompt before opening the PR. Describe what
   you tested and what happened.
4. Open a PR describing what changed and why. Link the issue if there is one.

## License

By contributing, you agree your contribution is licensed under this
project's MIT license (see `LICENSE`).
