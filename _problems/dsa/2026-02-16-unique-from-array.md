---
title: "Find the Unique Element in an Array"
difficulty: "Easy"
topics: ["Array"]
category: "DSA"
date: 2026-02-16
time_complexity: "O(n^2)"
space_complexity: "O(1)"
---

## Problem Description

Given an array of integers where every element appears an even number of times except for one element, find and return the unique element that appears an odd number of times.

**Example 1:**
```
Input: arr = [1, 4, 1, 4, 2]
Output: 2
```

**Example 2:**
```
Input: arr = [9, 3, 2, 9, 3, 2, 3, 6]
Output: 6
```

**Constraints:**
- The array will have at least one unique element

## Approach

Use a brute-force approach with nested loops. For each element, check if it appears again later in the array. If no duplicate is found for an element, it is the unique one.

**Key Insights:**
1. For each element, scan the rest of the array for a match
2. If no match is found, that element is unique
3. Track the result and return it after iterating through all elements

## Solution

```java
class Solution {
    public static int returnUnique(int[] arr) {
        int number1 = -1;
        int number2 = -1;
        for (int i = 0; i < arr.length; i++) {
            number1 = arr[i];
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    number1 = -1;
                    break;
                }
            }
            if (number1 != -1) {
                number2 = number1;
            }
        }
        return number2;
    }
}
```

Time Complexity = `O(n^2)`
Space Complexity = `O(1)`