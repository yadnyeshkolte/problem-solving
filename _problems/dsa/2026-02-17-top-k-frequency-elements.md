---
title: "Top K Frequent Elements"
leetcode_url: "https://neetcode.io/problems/top-k-elements-in-list/question"
difficulty: "Medium"
topics: ["Array", "Hash Table", "Heap (Priority Queue)"]
category: "DSA"
date: 2026-02-17
time_complexity: "O(n log k)"
space_complexity: "O(n)"
---

## Problem Description

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]

Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

## Approach

The approach uses a HashMap to count the frequency of each element in the array. Then, a Min-Heap (PriorityQueue) is used to keep track of the top `k` frequent elements. We iterate through the unique elements in the map, adding them to the heap. If the heap size exceeds `k`, we remove the element with the lowest frequency (which represents the least frequent among the top candidates seen so far). This ensures that the heap always contains the `k` most frequent elements. Finally, we convert the heap elements into an array and return it.

## Solution

```java

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;
        int[] arr = new int[k];
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<n;i++){
            if(map.containsKey(nums[i])){
                map.put(nums[i], map.get(nums[i])+1);
            }
            else{
                map.put(nums[i], 1);
            }
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> map.get(a)-map.get(b));

        for(int num: map.keySet()){
            pq.add(num);
            if(pq.size()>k){
                pq.poll();
            }
        }

        for(int i=0;i<k;i++){
            arr[i] = pq.poll();
        }
        return arr;
    }
}
```
