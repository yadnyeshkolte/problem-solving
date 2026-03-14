---
title: Search a 2D Matrix
leetcode_url: https://neetcode.io/problems/search-2d-matrix/question
difficulty: Medium
topics:
- Array
- Binary Search
- Matrix
category:
- DSA
- NeetCode
date: 2026-03-07
time_complexity: O(log(m * n))
space_complexity: O(1)
neetcode_url: https://neetcode.io/problems/search-2d-matrix/question
---

## Problem Description

You are given an `m x n` 2-D integer array `matrix` and an integer `target`.

Each row in `matrix` is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.

Return `true` if `target` exists within `matrix` or `false` otherwise.

Can you write a solution that runs in `O(log(m * n))` time?

**Example 1:**

Input: `matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10`

Output: `true`

**Example 2:**

Input: `matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15`

Output: `false`

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10000 <= matrix[i][j], target <= 10000`

## Approach

- **Two-level Binary Search:** Perform a binary search on the rows to find the potential row where the target might exist. Once the correct row is found (where the target is between the first and last elements of the row), perform a standard binary search on that specific row to determine if the target exists. This gives an `O(log m + log n)` which is equivalent to `O(log(m * n))` time complexity.

## Solution

### 1. Two-level Binary Search (Optimized)

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix.length;
        int m1 = matrix[0].length;

        if (n == 1 && m1 == 1) {
            if (target == matrix[0][0]) {
                return true;
            } else {
                return false;
            }
        }
        
        int top = 0;
        int bottom = n - 1;
        while (top <= bottom) {
            int m = top + (bottom - top) / 2;
            
            if (target >= matrix[m][0] && target <= matrix[m][m1 - 1]) {
                int left = 0;
                int right = m1 - 1;

                while (left <= right) {
                    int m2 = left + (right - left) / 2; // formula
                    if (matrix[m][m2] == target) {
                        return true;
                    } else if (matrix[m][m2] < target) {
                        left = m2 + 1;
                    } else {
                        right = m2 - 1;
                    }
                }
                return false;
                
            } else if (matrix[m][0] < target) {
                top = m + 1;
            } else {
                bottom = m - 1;
            }
        }
        return false;
    }
}

```
