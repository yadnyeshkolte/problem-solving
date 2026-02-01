---
title: "Find All Numbers Disappeared in an Array"
leetcode_url: "https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/"
difficulty: "Easy"
topics: ["Array", "Hash Table"]
category: "DSA"
date: 2026-01-31
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

## Approach
HashSet Approach (or the Time-Space Trade-off approach).

## Solution

```java
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> al = new ArrayList<>();
        HashSet<Integer> set = new HashSet<>();
        
        for (int num : nums) {
            set.add(num);
        }
        
        for (int i = 1; i <= nums.length; i++) {
            if (!set.contains(i)) {
                al.add(i);
            }
        }
        
        return al;
    }
}
```