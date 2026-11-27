# Preserve 3D-printing shopping learnings

Date: 2026-11-27

1. Review repository conventions and existing shopping entries; preserve newer decisions already in the repository.
2. Expand filament data with confirmed inventory, unresolved purchase status, and historical checkout snapshots kept separate from current offers.
3. Document the X2D setup, material choices, supplier evidence, black comparison method, and board-game organizer requirements with source links.
4. Update navigation and research conventions, run the existing read-only YAML validator and report, and check links and the diff for accidental personal data.
5. Commit the completed documentation locally on the feature branch. Obtain Josh's explicit approval before pushing or opening a pull request, as required by his global AGENTS.md instructions.

Scope: documentation and YAML only. No application code, purchases, account changes, database operations, or new live-price claims.

Completed: six imported research notes, expanded filament data, README navigation, and research conventions. Existing read-only validator and report scripts were inspected before execution; neither accesses a database. Both shopping lists pass schema validation, the filament report runs, local Markdown links resolve, and git diff whitespace checks pass. Validation used the declared PyYAML dependency in a temporary virtual environment; no dependency or script changes were made. External source links are preserved from prior research rather than asserted to be freshly checked.

Reconciliation: Josh approved pushing the branch and opening a PR, with a conflict check. Filament PR #2 had merged into main. Rebased onto that merge, retained every upstream option and its checked date/status, kept upstream filament.md deal recommendations, moved the imported overview to filament-context.md, linked the two, and retained both sets of agent conventions. No changes to main were made.
