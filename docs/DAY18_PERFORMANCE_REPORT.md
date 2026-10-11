# Day 18 — ATS Performance Report

## 1. Objective

Measure the existing resume text-extraction performance before optimization.

## 2. Test Environment

- Project: Zecpath AI
- Component: `parsers/resume_extractor.py`
- Input format: PDF
- Input folder: `data/resumes`
- Number of test resumes: 10

## 3. Baseline Results

| Metric | Result |
|---|---:|
| Total resumes | 10 |
| Successful extractions | 10 |
| Failed extractions | 0 |
| Total extraction time | 0.620 seconds |
| Average time per resume | 0.062 seconds |
| Total extracted characters | 12,100 |

## 4. Initial Observations

- All 10 PDF resumes were processed successfully in the benchmark run.
- The extractor uses `pypdf` for PDF text extraction.
- The extractor uses `python-docx` for DOCX text extraction.
- Text cleaning uses regular expressions and line-by-line processing.
- The current implementation repeatedly concatenates text inside extraction loops.

## 5. Optimization Plan

1. Reduce unnecessary intermediate string operations.
2. Preserve existing extraction and cleaning behaviour.
3. Test noisy and inconsistently formatted resume text.
4. Measure extraction time again using the same PDF files.
5. Run the automated test suite after modifications.
6. Compare before-and-after performance results.

## 6. Current Limitations

These results represent one local benchmark run. They do not establish performance under concurrent requests, large workloads, or production traffic.

Model response time and memory usage have not yet been measured.

## 7. Status

Baseline measurement completed. Optimization and post-change validation are pending.

## 8. Post-Optimization Results

| Metric | Baseline | After Optimization |
|---|---:|---:|
| Total resumes | 10 | 10 |
| Successful extractions | 10 | 10 |
| Failed extractions | 0 | 0 |
| Total extraction time | 0.620 seconds | 0.557 seconds |
| Average time per resume | 0.062 seconds | 0.056 seconds |
| Total extracted characters | 12,100 | 12,100 |

### Performance Analysis
- Total measured extraction time decreased by 0.063 seconds.
- The benchmark showed an approximately 10.2% reduction in extraction time.
- All 10 resumes were extracted successfully.
- The total extracted character count remained unchanged.
- The benchmark represents one run before and one run after optimization; repeated runs are needed for a more reliable comparison.

### Stability Validation
- Automated test suite: 15 tests passed.
- PDF extraction benchmark: 10 successful, 0 failed.
- Model response time and memory usage have not yet been measured.

### Conclusion
The extraction-loop optimization preserved the measured text output and passed the existing tests. Initial benchmark results indicate a modest improvement in extraction speed. Further testing is required before claiming production readiness.
