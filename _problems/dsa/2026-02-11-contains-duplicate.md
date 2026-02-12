---
title: "Contains Duplicate"
leetcode_url: "https://neetcode.io/problems/duplicate-integer"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
category: "DSA"
date: 2026-02-11
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

**Example 1:**
- Input: `nums = [1, 2, 3, 3]`
- Output: `true`

**Example 2:**
- Input: `nums = [1, 2, 3, 4]`
- Output: `false`

## Approach

Use a HashSet to track elements we've already seen. As we iterate through the array:
1. Check if the current element exists in the HashSet
2. If it exists, we've found a duplicate - return true
3. If not, add it to the HashSet and continue
4. If we finish the loop without finding duplicates, return false

This approach achieves O(n) time complexity by avoiding the O(n²) brute force comparison of every element against every other element.

## Solution

### Initial Approach (Hashtable)
```java
class Solution {
    public boolean hasDuplicate(int[] nums) {
        int n = nums.length;
        Hashtable<Integer, Integer> nonduplicates = new Hashtable<>();
        for(int i=0;i<n;i++){
            if(nonduplicates.containsValue(nums[i])){
                return true;
            }
            else{
                nonduplicates.put(i,nums[i]);
            }
        }
        return false;
    }
}
```

### Optimized Approach (HashSet)
```java
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> nonduplicates = new HashSet<>();
        for(int num: nums){
            if(nonduplicates.contains(num)){
                return true;
            }
            nonduplicates.add(num);
        }
        return false;
    }
}
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n)