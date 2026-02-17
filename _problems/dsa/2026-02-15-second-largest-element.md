---
title: "Second Largest Element"
difficulty: "Easy"
topics: ["Array"]
category: "DSA"
date: 2026-02-15
time_complexity: "O(n)"
space_complexity: "O(1)"
source: "Practice"
---

## Problem Description

Given an array of integers, return the second largest distinct element.

## Approach

Track the largest and second largest values while scanning the array once.

## Solution

```java
class Solution {
    public int secondLargest(int[] nums) {
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        for (int n : nums) {
            if (n > largest) {
                secondLargest = largest;
                largest = n;
            } else if (n != largest && n > secondLargest) {
                secondLargest = n;
            }
        }

        return secondLargest;
    }
}
```
