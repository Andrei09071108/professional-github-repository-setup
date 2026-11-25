# Handover

The first commit contains the original filenames. Use `git log --reverse --oneline` to find it and `git diff --find-renames --summary BASELINE HEAD` with its hash to inspect the migration. Keep the script in src, synthetic inputs in examples and instructions in docs. When changing a sample, repeat the documented command and update the expected count, checklist and changelog together.

The portfolio owner reviews the local delivery and controls future hosting, visibility and contributor access. Publication and remote verification require that review and approval. Local evidence is delivered alongside the repository.

The independent review reproduced the three-commit baseline from the audit bundle. Preserve those commits when publishing. Before recording remote acceptance, compare local HEAD with the public main ref, clone the public URL into a fresh directory, run the setup checks and inspect the rendered README and documentation links. Repeat against the final commit after any documentation update. Keep the audit archive and local logs outside the public repository.
