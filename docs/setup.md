# Reproduce the setup

Install Git and Python 3. The sample uses the standard library. From the directory containing the delivered repository, use a new destination:

```sh
git clone --no-local professional-github-repository-setup review-copy
cd review-copy
git status --short --branch
python src/summary.py examples/tickets.csv
```

Expect main to track origin/main and the script to print `Open items: 2`. If your Python 3 launcher is named python3, substitute that command. Run from the clone root so both paths resolve. The CSV header is id,status and the script counts rows with the exact status open.
