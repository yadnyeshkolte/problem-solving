---
title: "Three Integer Sum"
leetcode_url: "https://neetcode.io/problems/three-integer-sum"
difficulty: "Medium"
topics: ["Array", "Two Pointers", "Sorting"]
category: "DSA"
date: 2026-02-21
time_complexity: "O(n^2)"
space_complexity: "O(1) or O(n)"
---

## Problem Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

**Example 2:**

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

**Example 3:**

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

**Constraints:**

*   `3 <= nums.length <= 3000`
*   `-10^5 <= nums[i] <= 10^5`

## Approach

### Brute Force Approach

The brute force approach would be to use three nested loops to check every possible triplet. This would take `O(n^3)` time complexity. To avoid duplicates, we would need to sort each triplet and store them in a set.

### Optimized Approach (Sorting + Two Pointers)

We can optimize the search by sorting the array first. Sorting allows us to use the **Two Pointers** technique and easily skip duplicate elements.

1.  **Sort** the input array `nums`.
2.  Iterate through the array with a pointer `i` from `0` to `n-3`.
    *   If `nums[i]` is the same as the previous element, **skip** it to avoid duplicate triplets.
    *   Initialize two pointers: `left = i + 1` and `right = n - 1`.
    *   While `left < right`:
        *   Calculate `sum = nums[i] + nums[left] + nums[right]`.
        *   If `sum == 0`:
            *   Add the triplet `[nums[i], nums[left], nums[right]]` to the result.
            *   Increment `left` and decrement `right`.
            *   **Skip** duplicate elements for `left` and `right`.
        *   If `sum < 0`, increment `left` to increase the sum.
        *   If `sum > 0`, decrement `right` to decrease the sum.

**Time Complexity:** `O(n^2)` because we iterate through the array once and for each element, we use the two-pointer approach which is `O(n)`.
**Space Complexity:** `O(1)` or `O(n)` depending on the sorting algorithm's space requirements.

## Solution

### Java Solution (Optimized)

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> array = new ArrayList<>();
        int n = nums.length;
        for(int i=0;i<n-1;i++){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            int start = i+1;
            int end = n-1;
            while(start<end){
                int sum = nums[i]+nums[start]+nums[end];
                if(sum==0){
                    List<Integer> al = new ArrayList<>();
                    al.add(nums[i]);
                    al.add(nums[start]);
                    al.add(nums[end]);
                    array.add(al);
                    while(start<end && nums[start]==nums[start+1]){
                        start++;
                    } 
                    while(start<end && nums[end]==nums[end-1]){
                        end--;
                    }
                    start++;
                    end--;
                }
                else if(sum<0){
                    start++;
                }   
                else{
                    end--;
                }
            }
        }
        return array;
    }
}
```
