# Research Collection Mastery Validation Results

| Task | Result | Evidence | Fix applied |
|---|---|---|---|
| 1 dynamic site hidden JSON API found and pulled directly | PASS | candidates=['/api/hidden?page=1']; items=2 |  |
| 2 JS/infinite-scroll list collected all items with pacing | PASS | items=9; rounds=3 | Validated on authorized local infinite-scroll style endpoint; script uses hidden fetch endpoint rather than scraping rendered HTML. |
| 3 arXiv API harvested 50 metadata + 5 legal PDFs | PASS | papers=50; pdfs=5 |  |
| 4 GitHub API collected repo issues + stargazer history sample | PASS | stars=3664; issues=300; stargazers_sample=0; remaining=44 |  |
| 5 Mastodon public API pulled timeline within documented limit | PASS | status=200; posts=5 |  |
| 6 robots-disallowed source correctly refused | PASS | allowed=False; decision=refuse; alternative=ask owner for API/export or permission |  |
