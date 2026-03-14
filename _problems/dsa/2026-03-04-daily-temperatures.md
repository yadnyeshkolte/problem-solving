---
title: Daily Temperatures
difficulty: Medium
topics:
- Array
- Stack
- Monotonic Stack
category:
- DSA
- NeetCode
date: 2026-03-04
time_complexity: O(n^2)
space_complexity: O(n)
neetcode_url: https://neetcode.io/problems/daily-temperatures/question
---

## Problem Description

You are given an array of integers `temperatures` where `temperatures[i]` represents the daily temperatures on the `ith` day.

Return an array `result` where `result[i]` is the number of days after the `ith` day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the `ith` day, set `result[i]` to `0` instead.

**Example 1:**

**Input:** temperatures = [30,38,30,36,35,40,28]  
**Output:** [1,4,1,2,1,0,0]  

**Example 2:**

**Input:** temperatures = [22,21,20]  
**Output:** [0,0,0]  

**Constraints:**

- `1 <= temperatures.length <= 1000`
- `1 <= temperatures[i] <= 100`

## Approach

The provided solution uses nested loops (a brute-force like approach) combined with a stack to find the next warmer day. For each day, it scans forward until it finds a strictly greater temperature, adding intermediate temperatures to a stack along the way. The size of the stack determines the number of days waited.

## Solution

```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> st = new Stack<>();
        int[] array = new int[temperatures.length];  
        int n = temperatures.length;
/*
        for(int i=0;i<n;i++){
            int index = i+1;
            while(index<n){
                st.push(index);
                if(st.peek()<=temperatures[i]){
                    continue;
                }   
            }
        }
*/
        for(int i=0;i<n-1;i++){
            int index = i+1;
            while(index<n && temperatures[i]>=temperatures[index]){
                st.push(temperatures[index]);
                index++;
                
            }
            if(index<n && temperatures[i]<temperatures[index]){
                array[i] = st.size()+1;
            }
            else{
                array[i] = 0;

            }
            st = new Stack<>();

        }
        return array;
    }
}
```
