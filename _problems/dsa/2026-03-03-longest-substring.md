---
title: Longest Repeating Character Replacement
leetcode_url: https://neetcode.io/problems/longest-repeating-substring-with-replacement/question
difficulty: Medium
topics:
- String
- Sliding Window
- Hash Table
category:
- DSA
- NeetCode
date: 2026-03-03
time_complexity: O(n^2)
space_complexity: O(1)
neetcode_url: https://neetcode.io/problems/longest-repeating-substring-with-replacement/question
---

## Problem Description

You are given a string `s` consisting of only uppercase english characters and an integer `k`. You can choose up to `k` characters of the string and replace them with any other uppercase English character.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

**Example 1:**

Input: `s = "XYYX"`, `k = 2`

Output: `4`
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

**Example 2:**

Input: `s = "AAABABB"`, `k = 1`

Output: `5`

**Constraints:**

- `1 <= s.length <= 1000`
- `0 <= k <= s.length`

## Approach

The current code implements a sliding window but re-calculates the character frequency for every window.
- Expand the window by incrementing the `right` pointer as long as the current substring is valid.
- A substring is valid if its `length - max_character_frequency <= k`.
- If the substring is not valid, shrink the window by incrementing the `left` pointer.
- Continue to update the maximum length found so far.

## Solution

```java
class Solution {
    public int characterReplacement(String s, int k) {
        int n = s.length();
        int maxlength = 0;
        int left = 0;
        int right = 0;
        while(right<n){
            String str = s.substring(left, right+1);
            if(isItValid(str, k)){
                maxlength = Math.max(maxlength, str.length());
                right++;
            }
            else{
                left++;
            }
        }

        return maxlength;
    }
    public static boolean isItValid(String str, int m){
        int n = str.length();
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i=0;i<n;i++){
            char c = str.charAt(i);
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        int maxfreq = 0;
        for(Map.Entry<Character, Integer> entry: map.entrySet()){
            maxfreq = Math.max(maxfreq, entry.getValue());
        }

        if((n-maxfreq)<=m){
            return true;
        }
        return false;
    }
}
```
