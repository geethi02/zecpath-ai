## Day 17 Testing Status

* Planned test cases: 8 (TC01–TC08)
* Scoring method: Temporary keyword overlap baseline
* API execution: Scoring requests were accepted; completed results must be verified for each test case.
* Observed issue: Common words such as "and" and "with" are incorrectly classified as matched skills.
* Observed issue: Multi-word skills may be split into individual words.
* Precision: Not yet calculated
* Recall: Not yet calculated
* F1 score: Not yet calculated
* Overall accuracy: Not yet validated

### Next Actions

1. Retrieve and record each test case's completed result.
2. Manually label relevant skills as true matches, false matches, and missed skills.
3. Calculate precision, recall, and F1 score from verified labels.
4. Improve skill extraction and matching before claiming ATS accuracy.
