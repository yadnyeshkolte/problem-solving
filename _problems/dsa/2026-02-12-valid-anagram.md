---
title: "Valid Anagram"
leetcode_url: "https://neetcode.io/problems/is-anagram"
difficulty: "Easy"
topics: ["String", "Hash Table", "Sorting"]
category: "DSA"
date: 2026-02-12
time_complexity: "O(n)"
space_complexity: "O(1)"
---

## Problem Description

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**
- Input: `s = "racecar"`, `t = "carrace"`
- Output: `true`

**Example 2:**
- Input: `s = "jar"`, `t = "jam"`
- Output: `false`

**Constraints:**
- s and t consist of lowercase English letters.

## Approach

Use two HashMaps to track the frequency of each character in both strings:
1. First check if the strings have different lengths - if so, they cannot be anagrams
2. Iterate through string s and build a frequency map of its characters
3. Iterate through string t and build a frequency map of its characters
4. Compare both HashMaps - if they're equal, the strings are anagrams

This approach achieves O(n) time complexity by using hash tables for constant-time lookups and updates.

## Solution

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        int m = t.length();
        if(n != m){
            return false;
        }
        HashMap<Character, Integer> shash = new HashMap<>();
        HashMap<Character, Integer> thash = new HashMap<>();
        for(int i = 0; i < n; i++){
            char c = s.charAt(i);
            if(shash.containsKey(c)){
                shash.put(c, shash.get(c) + 1);
            }  
            else{
                shash.put(c, 1);
            } 
        }
        for(int i = 0; i < n; i++){
            char c = t.charAt(i);
            if(thash.containsKey(c)){
                thash.put(c, thash.get(c) + 1);
            } 
            else{
                thash.put(c, 1);
            } 
        }

        return shash.equals(thash);
    }
}
```

**Time Complexity:** O(n + m) where n and m are the lengths of strings s and t  
**Space Complexity:** O(1) - limited to 26 lowercase English letters