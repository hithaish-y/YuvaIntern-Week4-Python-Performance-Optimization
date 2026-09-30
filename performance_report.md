# YuvaIntern Week 4 - Performance Optimization

## Project: Python Performance Optimization

### 1. Objective

The objective of this task is to analyze a Python application, identify performance bottlenecks, optimize the code, and compare the execution time before and after optimization.

The application processes a list of numbers. It calculates the total of the numbers and identifies duplicate values.

---

## 2. Original Application

The original application used a loop with an artificial delay while calculating the total. It also used nested loops to find duplicate values.

The original implementation worked correctly but required more execution time.

### Original Performance

- Total: 5200
- Duplicates: [25, 50, 75]
- Execution Time: 1.1049 seconds

---

## 3. Performance Bottlenecks

Two main performance issues were identified:

1. The `calculate_total()` function used a loop and included a `time.sleep()` delay for every number.
2. The `find_duplicates()` function used nested loops, resulting in inefficient comparisons.

The nested-loop approach becomes slower as the number of input values increases.

---

## 4. Optimization Techniques

The following optimizations were implemented:

### Using `sum()`

The manual loop used for calculating the total was replaced with Python's built-in `sum()` function.

This makes the code simpler and avoids the unnecessary delay.

### Using Sets

The duplicate detection algorithm was changed from nested loops to a set-based approach.

A `seen` set keeps track of values already encountered, while a `duplicates` set stores repeated values.

This significantly reduces the number of comparisons.

---

## 5. Optimized Application

The optimized application maintains the same functionality as the original program.

It produces:

- Total: 5200
- Duplicates: [25, 50, 75]

The optimized version also removes the unnecessary delay from the calculation.

---

## 6. Performance Comparison

| Version | Execution Time |
|---|---:|
| Original | 1.1049 seconds |
| Optimized | 0.0 seconds |

The optimized implementation completed the same operation much faster in the test run.

---

## 7. Verification

The optimized program was executed successfully in VS Code.

The results were compared with the original application to make sure that the optimization did not change the expected output.

Both versions produced:

```text
Total: 5200
Duplicates: [25, 50, 75]