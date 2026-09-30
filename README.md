# YuvaIntern Week 4 - Performance Optimization

## Python Performance Optimization

This project was completed as part of the YuvaIntern Junior Python Developer Internship - Week 4 task.

The objective was to analyze a Python application, identify performance bottlenecks, optimize the code, and compare the execution time before and after optimization.

## Project Files

- `original_app.py` - Original Python application
- `optimized_app.py` - Optimized version of the application
- `performance_report.md` - Detailed performance analysis and comparison

## Application

The application processes a list of numbers and performs two operations:

- Calculates the total of the numbers
- Finds duplicate values

## Optimization Performed

The original application was optimized using:

1. Python's built-in `sum()` function instead of an unnecessary loop.
2. A set-based approach for finding duplicate values instead of nested loops.
3. Removal of unnecessary execution delays.

## Performance Comparison

| Version | Execution Time |
|---|---:|
| Original | 1.1049 seconds |
| Optimized | 0.0 seconds |

Both versions produced the same output:

```text
Total: 5200
Duplicates: [25, 50, 75]