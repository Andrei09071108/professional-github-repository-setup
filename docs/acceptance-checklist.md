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

Recorded local results accompany the delivery. Owner acceptance and GitHub checks are pending.
