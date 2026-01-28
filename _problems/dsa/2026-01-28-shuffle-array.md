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

## Solution

`time_complexity: "O(n)"`
`space_complexity: "O(1)"`

```java
class Solution {
    public int[] shuffle(int[] nums, int n) {
        // Step 1: Pack pairs into the right half of the array
        for (int i = 0; i < n; i++) {
            nums[i + n] = (nums[i + n] << 10) | nums[i];
        }
        
        // Step 2: Unpack them into the correct positions
        for (int i = 0; i < n; i++) {
            int x = nums[i + n] & 1023;       // Get the original first 10 bits (x)
            int y = nums[i + n] >> 10;        // Get the shifted 10 bits (y)
            
            nums[2 * i] = x;
            nums[2 * i + 1] = y;
        }
        return nums;
    }
}
```