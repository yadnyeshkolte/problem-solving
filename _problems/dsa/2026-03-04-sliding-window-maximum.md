---
title: "Sliding Window Maximum"
leetcode_url: "https://neetcode.io/problems/sliding-window-maximum/question"
difficulty: "Hard"
topics: ["Array", "Sliding Window", "Queue", "Monotonic Queue"]
category: "DSA"
date: 2026-03-04
time_complexity: "O(n*k)"
space_complexity: "O(k)"
---

## Problem Description

You are given an array of integers `nums` and an integer `k`. There is a sliding window of size `k` that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

**Example 1:**

**Input:** nums = [1,2,1,0,4,2,6], k = 3  
**Output:** [2,2,4,4,6]

**Explanation:**
```text
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
```

**Constraints:**

- `1 <= nums.length <= 100,000`
- `-10,000 <= nums[i] <= 10,000`
- `1 <= k <= nums.length`


## Approach

Brute force iteration over all possible sliding windows of size `k`. Inside the outer loop, there is an inner loop that finds the maximum element in the current window. This maximum is added to a temporary `ArrayList`, and finally copied to the resulting `int[]`.

## Solution

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        ArrayList<Integer> array = new ArrayList<>();
        int n = nums.length;
        int left = 0;
        int right = k-1;
        while(right<n){
            int max = nums[left];
            for(int i=left;i<=right;i++){
                max = Math.max(max, nums[i]);
            }
            array.add(max);
            left++;
            right++;
        }

        int[] result = new int[array.size()];
        for (int i = 0; i < array.size(); i++) {
            result[i] = array.get(i);
        }
        return result;
    }
}
```
