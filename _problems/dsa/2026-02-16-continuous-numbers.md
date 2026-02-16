---
title: "Longest Continuous Numbers in an Array"
difficulty: "Medium"
topics: ["Array", "Sorting"]
category: "DSA"
date: 2026-02-16
source: "Raja Software Labs Question Test"
time_complexity: "O(n log n)"
space_complexity: "O(1)"
---

## Problem Description

Given an unsorted array of integers, find the length of the longest sequence of continuous (consecutive) numbers.

The numbers must be consecutive in value (like `1, 2, 3, 4`) but do not need to be adjacent in the original array.

**Example 1:**
```
Input: arr = [100, 200, 4, 3, 1, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]
```

**Example 2:**
```
Input: arr = [1, 34, 35, 33, 23, 32, 11, 20]
Output: 4
Explanation: The longest consecutive sequence is [32, 33, 34, 35]
```

## Approach

Sort the array first, then traverse it once while counting the current consecutive streak.

**Key Insights:**
1. After sorting, consecutive numbers appear next to each other
2. If `arr[i] + 1 == arr[i + 1]`, increase the running streak
3. If duplicates appear, skip them without resetting the streak
4. For any gap, reset the streak to `1`
5. Track the maximum streak seen so far

## Solution

```java
import java.util.Arrays;

class  Solution1{
    public static void main(String[] args){
        int[] arr = {100, 200, 4,3,1,2};
        int[] arr1 = {1, 34, 35,33,23,32,11,20};
        int n = returnLength(arr);
        System.out.println(n);

    }
    public static int returnLength(int[] arr){
        int n = arr.length;
        Arrays.sort(arr);
        int temp = 1;
        int count = 1;

        for(int i=0;i<n-1;i++){
            if(arr[i]+1==arr[i+1]){
                count++;
            }
            else if(arr[i]==arr[i+1]) {
                continue;
            }
            else{
                count = 1;
            }
            if(count>temp){
                temp = count;
            }
        }

        return temp;
    }

}
```

Time Complexity = `O(n log n)`
Space Complexity = `O(1)`
