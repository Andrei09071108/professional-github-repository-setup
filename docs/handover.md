# Handover

The first commit contains the original filenames. Use `git log --reverse --oneline` to find it and `git diff --find-renames --summary BASELINE HEAD` with its hash to inspect the migration. Keep the script in src, synthetic inputs in examples and instructions in docs. When changing a sample, repeat the documented command and update the expected count, checklist and changelog together.

The portfolio owner manages the public repository and contributor access. The three-commit audit bundle preserves the original handover. The public release at 0d324cd passed the remote acceptance checks recorded in the checklist.

After a documentation or sample change, compare local HEAD with the public main ref, clone the public HTTPS URL into a fresh directory and run the setup checks. Inspect the rendered README and its links. Keep the audit archive, logs and portfolio materials outside the repository.
