---
title: "Max Consecutive Ones"
leetcode_url: "https://leetcode.com/problems/max-consecutive-ones/"
difficulty: "Easy"
topics: ["Array"]
category: "DSA"
date: 2026-01-29
time_complexity: "O(n)"
space_complexity: "O(1)"
---

## Problem Description
Given a binary array nums, return the maximum number of consecutive 1's in the array.

## Approach
Re-indexing or Interleaving

## Solution

```java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxcount = 0;
        int temp = 0;
        int n = nums.length;
        if(n==1){
            if(nums[0]==1){
                return 1;
            }
            else{
                return 0;
            }
        }
        for(int i=0;i<n-1;i++){

            if(nums[i]==0){
                if(temp>=maxcount){
                    maxcount = temp;
                }
                temp = 0;
                continue;
            }
            if(nums[i]==1 && temp==0){
                temp++;
            }
            if(nums[i]==1 && nums[i+1]==1){
                temp++;
            }
        }

        if(temp==0 && maxcount==0 && nums[n-1]==1){
            return 1;
        }
        if(temp>=maxcount){
            maxcount = temp;
        }

        return maxcount;
    }
}
```

## Solution

`time_complexity: "O(n)"`
`space_complexity: "O(1)"`

```java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxcount = 0;
        int temp = 0;
        int n = nums.length;
        for(int i=0;i<n;i++){
            if(nums[i]==1){
                temp++;
            }
            else{
                if(temp>maxcount){
                    maxcount = temp;
                }  
                temp = 0;
            }
        }
        if(temp>maxcount){
            maxcount = temp;
        } 
        return maxcount;
    }
}
```

