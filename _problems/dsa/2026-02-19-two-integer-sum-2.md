---
title: "Two Integer Sum II"
leetcode_url: "https://neetcode.io/problems/two-integer-sum-ii/question"
difficulty: "Medium"
topics: ["Array", "Two Pointers"]
category: "DSA"
date: 2026-02-19
time_complexity: "O(n)"
space_complexity: "O(1)"
---

## Problem Description

Given an array of integers `numbers` that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, `[index1, index2]`, such that they add up to a given target number `target` and `index1 < index2`. Note that `index1` and `index2` cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use `O(1)` additional space.

**Example 1:**

```
Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
```

**Constraints:**

*   `2 <= numbers.length <= 1000`
*   `-1000 <= numbers[i] <= 1000`
*   `-1000 <= target <= 1000`

## Approach

### Brute Force Approach

The brute force simple approach would be to check every pair of numbers in the array. This would be an `O(n^2)` solution.

### Optimized Approach (Two Pointers)

Since the array is sorted, we can use the **Two Pointers** technique to solve this in `O(n)` time and `O(1)` space.

1.  Initialize two pointers: `start` at the beginning (`0`) and `end` at the end (`n-1`) of the array.
2.  Calculate the sum of elements at `start` and `end`.
3.  If the sum equals the `target`, return the indices (1-indexed).
4.  If the sum is greater than the `target`, we need a smaller sum, so decrement `end`.
5.  If the sum is smaller than the `target`, we need a larger sum, so increment `start`.
6.  Repeat until the pair is found.

## Solution

### Solution 1: Brute Force

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(numbers[i]+numbers[j]==target){
                    return new int[]{i+1, j+1};
                }
            }
        }
        return new int[]{-1, -1};
    }
}
```

### Solution 2: Two Pointers (Optimized)

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int start = 0;
        int end = n-1;
        while(start<end){
            int x = numbers[start]+numbers[end];
            if(x==target){
                return new int[]{start+1, end+1};
            }
            if(x>target){
                end--;
            }        
            if(x<target){
                start++;
            }    
        }
        return new int[]{-1, -1};
    }
}
```
