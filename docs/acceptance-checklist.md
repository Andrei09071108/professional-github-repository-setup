# Acceptance checklist

| Check | Reproduction | Acceptance condition |
|---|---|---|
| Intake preserved | Compare the baseline and current Git blob IDs for all three moved files | Each pair matches |
| Clean delivery | git status --porcelain | Empty output |
| Ignore rules | git check-ignore -v .env debug.log src/__pycache__/demo.pyc | Each path matches a rule |
| Onboarding | Follow the [setup guide](setup.md) | Fresh clone prints Open items: 2 |
| Documentation | Open every relative Markdown link | Each file resolves |
| Privacy | Review tracked text and author metadata throughout history | Only synthetic inputs and intended public material |
| Hosting | Compare local HEAD with the authorized remote main, then clone from GitHub | Matching commits and successful sample run |

Local and remote test records accompany the delivery.

## Independent review of the baseline

The owner reported that the independent reviewer verified the ZIP digest and all 19 entries, recovered three commits and ten tracked files, and matched all three originals byte for byte. Git integrity, five ignore rules, six internal links, the secret-pattern scan and the clean sample run passed. This result applies to commit 346820e.

## Public repository acceptance

At commit `0d324cd1221238d395e31533e148b14b6b5a8faf`, the public main ref, local HEAD and fresh HTTPS clone matched. All four commits and eleven tracked files were present. Strict Git integrity checks passed, the three intake files matched the originals byte for byte, and the documented command printed `Open items: 2` with a clean working tree afterwards. The README rendered on GitHub and all six internal documentation links resolved. The history scan found no matches outside the intended identities for the privacy and credential patterns tested.
