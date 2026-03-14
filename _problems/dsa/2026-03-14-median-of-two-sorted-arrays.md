---
title: Median of Two Sorted Arrays
leetcode_url: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
difficulty: Hard
topics:
- Array
- Binary Search
- Divide and Conquer
category:
- DSA
- LeetCode
date: 2026-03-14
time_complexity: O(m + n)
space_complexity: O(m + n)
---

## Problem Description

You are given two integer arrays `nums1` and `nums2` of size `m` and `n` respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

Your solution must run in `O(log(m + n))` time.

**Example 1:**

**Input:** nums1 = [1,2], nums2 = [3]  
**Output:** 2.0  
**Explanation:** Among [1, 2, 3] the median is 2.

**Example 2:**

**Input:** nums1 = [1,3], nums2 = [2,4]  
**Output:** 2.5  
**Explanation:** Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

**Constraints:**

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Approach

Use a two-pointer approach to merge the two sorted arrays (`nums1` and `nums2`) into a single sorted array. Iterate through both arrays, comparing the elements and adding the smaller one to the new array. Once the merged array is fully populated, calculate the median based on whether the total length is even or odd. This approach takes `O(m + n)` time and `O(m + n)` space. Even though it's a valid and simple approach, it doesn't meet the stricter `O(log(m + n))` requirement specified in the problem statement.

## Solution

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len = nums1.length+nums2.length;
        int n = nums1.length;
        int m = nums2.length;
        int[] array = new int[len];
        int i=0;
        int j=0;
        int k=0;
        while(i<n && j<m){
            if(nums1[i]<nums2[j]){
                array[k] = nums1[i];
                i++;
            }
            else{
                array[k] = nums2[j];
                j++;
            }
            k++;
        }
        while(i<n){
            array[k] = nums1[i];
            i++;
            k++;
        }
        while(j<m){
            array[k] = nums2[j];
            k++;
            j++;
        }
        int alen = array.length;
        if(alen%2==1){
            return (double) array[alen/2]; 
        }
        else{
            return (double) (array[alen/2]+array[(alen/2)-1])/2;
        }
        
    }
}

```
