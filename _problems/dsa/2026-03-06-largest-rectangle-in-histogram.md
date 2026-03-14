---
title: Largest Rectangle In Histogram
leetcode_url: https://neetcode.io/problems/largest-rectangle-in-histogram/question
difficulty: Hard
topics:
- Array
- Stack
- Monotonic Stack
category:
- DSA
- NeetCode
date: 2026-03-06
time_complexity: O(n^2)
space_complexity: O(1)
neetcode_url: https://neetcode.io/problems/largest-rectangle-in-histogram/question
---

## Problem Description

You are given an array of integers `heights` where `heights[i]` represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

**Example 1:**

**Input:** heights = [7,1,7,2,2,4]  
**Output:** 8

**Example 2:**

**Input:** heights = [1,3,7]  
**Output:** 7

**Constraints:**

- `1 <= heights.length <= 1000`
- `0 <= heights[i] <= 1000`

## Approach

The provided solution uses a brute force approach. It iterates through all possible pairs of starting and ending bars using two nested loops. The outer loop selects the starting bar `i`, and the inner loop selects the ending bar `j`. As the inner loop progresses, it continuously keeps track of the minimum height (`minheight`) encountered between the starting bar `i` and the current ending bar `j`. The area of the rectangle formed by this continuous segment is calculated by multiplying the `minheight` with the width of the segment (`j - i + 1`). We compute this area for all possible segments and keep track of the maximum area found, which is ultimately returned. While simple, this approach has a time complexity of O(n^2). *Note: More optimal solutions using a monotonic stack exist that can solve this in O(n) time.*

## Solution

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int area = 0;
        for(int i=0;i<n;i++){
            int minheight = heights[i];
            for(int j=i;j<n;j++){
                minheight = Math.min(heights[j], minheight);
                int dist = j-i+1;
                int areac = dist*minheight;
                area = Math.max(area, areac);
            }
        }
        return area;
    }
}
```
