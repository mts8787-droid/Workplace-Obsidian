---
title: "06_Harness_Layer_Fence_Hook"
description: "Hard constraint that keeps AGENTS, Skills, Rules, and Hooks separated by layer."
category: "hook"
tags:
  - harness
  - layer
  - fence
---

# Hook: Harness Layer Fence
**Precedence: 0 (hard stop)**

## 1. Hard Rules
- `AGENTS.md` is a hub only. It may define scope, precedence, index entries, and governance, but it must not contain step-by-step procedures, file-specific runbooks, or execution recipes.
- `Skill` files contain how-to workflows and automation steps.
- `Rule` files contain standards, formats, and evaluation criteria.
- `Hook` files contain prohibitions and hard stops.
- Every harness edit must map to exactly one target layer before writing.

## 2. Edit Protocol
- If a requested change mixes layers, split it into separate file edits.
- Do not keep command-specific behavior in `AGENTS.md` for convenience.
- Do not move standards into skills or procedures into rules.
- If the correct layer is unclear, pause and ask for clarification.

## 3. Self-Check
- After editing, verify that each new paragraph belongs to only one layer.
- If the content could be read as more than one layer, rewrite it or split it.
- If an edit would make `AGENTS.md` longer by adding operational detail, move that detail back into the relevant skill, rule, or hook.
