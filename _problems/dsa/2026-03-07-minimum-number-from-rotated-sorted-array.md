---
title: "Find Minimum in Rotated Sorted Array"
leetcode_url: "https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question"
difficulty: "Medium"
topics: ["Array", "Binary Search"]
category: "DSA"
date: 2026-03-07
time_complexity: "O(log n)"
space_complexity: "O(1)"
---

## Problem Description

You are given an array of length `n` which was originally sorted in ascending order. It has now been rotated between `1` and `n` times. For example, the array `nums = [1,2,3,4,5,6]` might become:

- `[3,4,5,6,1,2]` if it was rotated `4` times.
- `[1,2,3,4,5,6]` if it was rotated `6` times.

Notice that rotating the array `4` times moves the last four elements of the array to the beginning. Rotating the array `6` times produces the original array.

Assuming all elements in the rotated sorted array `nums` are unique, return the minimum element of this array.

A solution that runs in `O(n)` time is trivial, can you write an algorithm that runs in `O(log n)` time?

**Example 1:**

Input: `nums = [3,4,5,6,1,2]`

Output: `1`

**Example 2:**

Input: `nums = [4,5,0,1,2,3]`

Output: `0`

**Example 3:**

Input: `nums = [4,5,6,7]`

Output: `4`

**Constraints:**

- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`

## Approach

- **Binary Search:** We use an optimized binary search approach. The key observation is that if the `middle` element is less than the `right` element, it means the minimum element must exist in the left half (including the `middle` element itself). Conversely, if the `middle` element is greater than the `right` element, then the minimum element resides in the right half (excluding `middle`). We can apply this logic repeatedly to find the absolute minimum in `O(log n)` time. The trivial linear search `O(n)` is also possible by directly tracking the minimum across all elements.

## Solution

### 1. Optimized Approach (Binary Search)

```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0 ;
        int right = nums.length-1;
        while(left<right){
            int middle = left+(right-left)/2;
            if(nums[middle]<nums[right]){
                right =  middle;
            }
            else{
                left = middle+1;
            }
        }

        return nums[right];

        /*
        int min = nums[0];
        for(int num: nums){
            min = Math.min(num, min);
        }
        
        return min;
        */
    }
}
```
