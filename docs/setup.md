# Reproduce the setup

Install Git and Python 3. The sample uses Python's standard library. Choose one source below and use a new destination directory.

## From GitHub

Clone the public repository over HTTPS:

```sh
git clone https://github.com/Andrei09071108/professional-github-repository-setup.git review-copy
```

## From a local repository

From the parent of the versioned repository (the source directory must contain .git), run:

```sh
git clone --no-local professional-github-repository-setup review-copy
```

## From the audit bundle

Extract the review ZIP. From the directory containing repository.bundle, run:

```sh
git init verifier
git -C verifier bundle verify ../repository.bundle
git -c core.autocrlf=false clone repository.bundle review-copy
```

The audited bundle restores the three-commit baseline. Its checkout setting preserves the original LF bytes on Windows. Later revisions carry their own line-ending policy.

## Verify any clone

```sh
cd review-copy
git fsck --full --strict
git status --short --branch
python src/summary.py examples/tickets.csv
git status --porcelain
```

Expect main to track origin/main, the script to print `Open items: 2` and the final status to be empty. If your Python 3 launcher is named python3, substitute that command. Run from the clone root. The CSV header is id,status and the script counts rows with the exact status open.
