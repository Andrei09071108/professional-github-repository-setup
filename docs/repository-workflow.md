# Make a reviewable change

Start in a fresh clone. Create a branch with `git switch -c docs/clarify-intake`. Edit docs/intake.txt to explain one input assumption. Check the exact edits with `git diff`. Stage only the intended file with `git add docs/intake.txt`, inspect `git diff --cached`, then run `git commit -m "docs: clarify queue input"`. Use your chosen repository-local author identity if Git asks. Run the sample and inspect `git status --short` for unexpected changes.

With an authorized shared remote, push the branch with `git push -u origin docs/clarify-intake` and request review before merging. After merge, use `git switch main` and `git pull --ff-only`.

To repeat the original migration, copy the intake into an empty folder, run `git init -b main`, inspect all inputs for private data, stage the reviewed files and commit a baseline. Create destination folders and use git mv for each file. Inspect staged renames before committing the layout. Commit documentation separately so reviewers can distinguish moves from edits.
