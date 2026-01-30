---
title: "Set Mismatch"
leetcode_url: "https://leetcode.com/problems/set-mismatch/"
difficulty: "Easy"
topics: ["Array","Hash Table", "Bit Manipulation", "Sorting"]
category: "DSA"
date: 2026-01-30
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number. You are given an integer array nums representing the data status of this set after the error. Find the number that occurs twice and the number that is missing and return them in the form of an array.

## Approach
We keep track of the numbers we've seen. If we see a number again, it's the duplicate. After checking all numbers, we look for which number from $1$ to $n$ was never seen that’s the missing one.

## Solution

```java
import java.util.HashSet;

class Solution {
    public int[] findErrorNums(int[] nums) {
        int duplicate = -1, missing = -1;
        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            if (set.contains(num)) {
                duplicate = num;
            }
            set.add(num);
        }

        for (int i = 1; i <= nums.length; i++) {
            if (!set.contains(i)) {
                missing = i;
                break;
            }
        }

        return new int[]{duplicate, missing};
    }
}

```