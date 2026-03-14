---
title: Koko Eating Bananas
difficulty: Medium
topics:
- Array
- Binary Search
category:
- DSA
- NeetCode
date: 2026-03-07
time_complexity: O(n * max(p))
space_complexity: O(1)
neetcode_url: https://neetcode.io/problems/eating-bananas/question
---

## Problem Description

You are given an integer array `piles` where `piles[i]` is the number of bananas in the `i^{th}` pile. You are also given an integer `h`, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of `k`. Each hour, you may choose a pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer `k` such that you can eat all the bananas within `h` hours.

**Example 1:**

Input: `piles = [1,4,3,2], h = 9`

Output: `2`
Explanation: With an eating rate of `2`, you can eat the bananas in `6` hours. With an eating rate of `1`, you would need `10` hours to eat all the bananas (which exceeds `h=9`), thus the minimum eating rate is `2`.

**Example 2:**

Input: `piles = [25,10,23,4], h = 4`

Output: `25`

**Constraints:**

- `1 <= piles.length <= 1,000`
- `piles.length <= h <= 1,000,000`
- `1 <= piles[i] <= 1,000,000,000`

## Approach

- **Brute Force Approach:** Iterate through potential eating speeds `k` starting from 1 up to the maximum pile size. For each `k`, compute the total hours required to finish all piles by taking the ceiling of division for each pile. Return the first `k` that meets the condition `hours <= h`.

## Solution

### 1. Brute Force (Current By User)

```java
class Solution {
    public int minEatingSpeed(int[] piles, int h) {

        int n = piles.length;
        Arrays.sort(piles);// 1 2 3 4
        int k = 0;
        for(k=1;k<=piles[n-1];k++){ //2
            int index = 0;
            int hour = 0;
            while(index<n){
                if(piles[index]>k){
                    hour += Math.ceil((double)piles[index]/k);
                    index++;
                }
                else{
                    index++;
                    hour++;
                } //1 1 1 1 1 1

            }
            if(hour<=h){
                return k;
            }
        }
        return k;
    }
}
```
