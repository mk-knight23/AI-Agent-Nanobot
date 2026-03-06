---
name: git-automator
description: "Automates git workflows: generates conventional commit messages from staged diffs, writes changelogs from git history, creates pull request descriptions, and suggests branch names. Use when you want AI-assisted git hygiene without leaving your terminal. Works on any git repository. Does not push or merge without explicit confirmation."
---

# git-automator

AI-assisted git workflows: commit messages, changelogs, PR descriptions — from your actual diff.

## Usage
```
@Nanobot git-automator commit                    # Generate commit message from staged diff
@Nanobot git-automator changelog --since v1.2.0  # Write CHANGELOG section from git log
@Nanobot git-automator pr-description            # Write PR description from branch vs main diff
@Nanobot git-automator branch-name --describe "fix auth bug where JWT expired early"
```

## Commands

### `commit`
- Reads `git diff --staged`
- Produces a conventional commit message: `type(scope): description`
- Shows message for you to confirm before running `git commit`
- Never commits without confirmation

### `changelog --since <tag>`
- Reads `git log <tag>..HEAD` with full diffs
- Groups commits by type (feat, fix, refactor, etc.)
- Writes a `## [Unreleased]` Markdown section
- Appends to `CHANGELOG.md` (creates if missing)

### `pr-description`
- Reads `git diff main...HEAD`
- Writes a PR description with Summary, Changes, and Test Plan sections
- Saves to `.pr_description.md` for use with `gh pr create --body-file`

### `branch-name`
- Takes a description of the work in natural language
- Suggests 3 branch name options following `<type>/<scope>-<description>` convention

## Files Modified
```
CHANGELOG.md                    # Updated by changelog command
.pr_description.md              # Written by pr-description command (gitignored)
```

## Philosophy
Commit messages and changelogs are read far more than they're written. Every commit message is a future `git blame` annotation. Every changelog entry is a future release note. Write them like they matter — because they do.
