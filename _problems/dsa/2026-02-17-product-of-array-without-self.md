---
title: "Product of Array Except Self"
leetcode_url: "https://neetcode.io/problems/products-of-array-discluding-self/question"
difficulty: "Medium"
topics: ["Array", "Prefix Sum"]
category: "DSA"
date: 2026-02-17
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

Constraints:

*   2 <= nums.length <= 1000
*   -20 <= nums[i] <= 20

## Approach

The brute force approach would be to iterate through the array and for each element, compute the product of all other elements. This results in O(n^2) time complexity.
A better approach uses prefix and suffix products. We can calculate the product of all elements to the left of each index (prefix) and the product of all elements to the right of each index (suffix).
The result for any index `i` is simply `prefix[i] * suffix[i]`.
This allows us to solve the problem in O(n) time.

## Solution 1

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            int mul = 1;
            for(int j=0;j<n;j++){
                if(i!=j){
                    mul = nums[j] * mul;
                }
            }
            arr[i] = mul;
        }
        return arr;


    }
}  
```

## Solution 2

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] arr = new int[n];
        int[] prefix = new int[n];
        int[] suffix = new int[n];

        prefix[0] = 1;
        for(int i=1;i<n;i++){
            prefix[i] = prefix[i-1] * nums[i-1];
        }

        suffix[n-1] = 1;
        for(int i=n-2;i>=0;i--){
            suffix[i] = suffix[i+1] * nums[i+1];
        }

        for(int i=0;i<n;i++){
            arr[i] = prefix[i] * suffix[i];
        }

        return arr;

    }
}  

```