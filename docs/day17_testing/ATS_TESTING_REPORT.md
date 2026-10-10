## Final Testing Summary

### Testing Coverage

Eight test scenarios were planned to evaluate entry-level and senior technical roles, non-technical roles, and graduate candidates with different skill profiles.

### Key Findings

* The API accepted scoring requests and returned job IDs.
* Completed scoring results were retrieved for the tested cases where status was verified.
* The temporary keyword-overlap baseline identifies some relevant terms but also matches ordinary words such as "and" and "with".
* Multi-word skills can be split into separate terms, reducing the reliability of the results.
* A match score alone does not establish ATS accuracy.

### Limitations

The same resume was reused for different job descriptions. Therefore, these tests are an initial role-adaptability probe, not a complete evaluation of different candidate profiles.

Precision, recall, F1 score, and overall accuracy remain unverified until the outputs are manually labelled and evaluated.

### Conclusion

The API scoring workflow is operational, but the current baseline requires improvements to skill extraction, phrase matching, and role-specific evaluation before it can be considered reliable for candidate screening.

### Next Steps

1. Verify and record the completed result for each test case.
2. Compare matched and missing skills against a manual review.
3. Calculate accuracy metrics using verified labels.
4. Improve the matching logic and repeat the tests.
