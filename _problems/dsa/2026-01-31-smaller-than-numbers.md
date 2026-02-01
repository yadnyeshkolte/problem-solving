---
title: "How Many Numbers Are Smaller Than the Current Number"
leetcode_url: "https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/"
difficulty: "Easy"
topics: ["Array", "Hash Table", "Sorting", "Counting Sort"]
category: "DSA"
date: 2026-01-31
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array.

## Approach
Brute force for each array element.

## Solution

```java
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            int count = 0;
            for(int j=0;j<n;j++){
                if(j==i){
                    continue;
                }
                if(nums[i]>nums[j]){
                    count++;
                }
            }
            arr[i] = count;
        } 
        return arr;
    }
}
```