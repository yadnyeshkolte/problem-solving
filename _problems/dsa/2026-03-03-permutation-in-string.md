---
title: Permutation in String
difficulty: Medium
topics:
- String
- Sliding Window
- Hash Table
category:
- DSA
- NeetCode
date: 2026-03-03
time_complexity: O(n^3)
space_complexity: O(1)
neetcode_url: https://neetcode.io/problems/permutation-string/question
---

## Problem Description

You are given two strings `s1` and `s2`.

Return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. That means if a permutation of `s1` exists as a substring of `s2`, then return `true`.

Both strings only contain lowercase letters.

**Example 1:**

Input: `s1 = "abc"`, `s2 = "lecabee"`

Output: `true`
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

**Example 2:**

Input: `s1 = "abc"`, `s2 = "lecaabee"`

Output: `false`

**Constraints:**

- `1 <= s1.length, s2.length <= 1000`

## Approach

The provided code implements a search that iterates through all possible substrings of `s2`. For each substring, it passes it to an `isValid` helper method which uses HashMaps to compute the character frequencies of both `s1` and the current substring. It then compares the maps. If the maps are exactly the same, it means they are anagrams/permutations of each other. 
*(Note: A more optimal sliding window approach of fixed length `s1.length()` could reduce the time complexity down to `O(n)`).*

## Solution

```java
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s2.length();
        int left = 0;
        int right = 0;
        while(right<n){
            String substr = s2.substring(left, right+1);
            if(isValid(s1, substr)){
                return true;
            }
            else if(right==n-1){
                left++;
                right = left;
            }   
            else{
                right++;
            }
        }

        return false;
    }
    public static boolean isValid(String s1, String s2){
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();
        for(int i=0;i<s1.length();i++){
            char c = s1.charAt(i);
            map1.put(c, map1.getOrDefault(c, 0)+1);
        }

        for(int i=0;i<s2.length();i++){
            char c = s2.charAt(i);
            map2.put(c, map2.getOrDefault(c, 0)+1);
        }
        
        return map1.equals(map2);

    }
}
```
