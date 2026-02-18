---
title: "Longest Consecutive Sequence"
leetcode_url: "https://neetcode.io/problems/longest-consecutive-sequence/question"
difficulty: "Medium"
topics: ["Array", "Hash Table", "Union Find"]
category: "DSA"
date: 2026-02-18
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description

Given an array of integers `nums`, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly `1` greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

```
Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].
```

**Example 2:**

```
Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
```

**Constraints:**

*   `0 <= nums.length <= 1000`
*   `-10^9 <= nums[i] <= 10^9`

## Approach

The brute force simple approach would be to consider every element from the array as the start of the sequence and count the length of the sequence formed with that starting element. This would be an `O(n^2)` solution.

To achieve `O(n)` time complexity, we can use a `HashSet` to store all elements for `O(1)` lookups.

The key insight is to identify the start of a sequence. A number `num` is the start of a sequence if `num - 1` is not present in the set.

1.  Add all numbers to a `HashSet`.
2.  Iterate through the array. For each number `num`:
    *   Check if it is the start of a sequence (i.e., `!set.contains(num - 1)`).
    *   If it is the start, increment `num` and check if the next number exists in the set, counting the length of the sequence.
    *   Update the maximum length found.
3.  Return the maximum length.

## Solution

```java
import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        int n = nums.length;
        HashSet<Integer> ht = new HashSet<>();
        for(int i=0;i<n;i++){
            ht.add(nums[i]);
        }
        int count = 0;
        int maxcount = 0;
        for(int num: nums){
            if(!ht.contains(num-1)){
                count = 1;
                int number = num;
                while(ht.contains(number+1)){
                    number++;
                    count++;
                }
            }
            if(count>maxcount){
                maxcount = count;
            }
        }
        return maxcount;
    }
}
```
