---
title: "Shuffle the Array"
leetcode_url: "https://leetcode.com/problems/shuffle-the-array/"
difficulty: "Easy"
topics: ["Array"]
category: "DSA"
date: 2025-01-28
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the form [x1,y1,x2,y2,...,xn,yn].

## Approach
Two-Pointer Approach, Linear Re-indexing

## Solution

```java
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int m = nums.length;
        int[] arr = new int[m];
        int temp = 0;
        for(int i=0;i<m;i=i+2){
            arr[i] = nums[temp];
            arr[i+1] = nums[n+temp];
            temp++;
        }
        return arr;
    }
}
```