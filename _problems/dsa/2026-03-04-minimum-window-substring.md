---
title: Minimum Window Substring
difficulty: Hard
topics:
- String
- Sliding Window
- Hash Table
category:
- DSA
- NeetCode
date: 2026-03-04
time_complexity: O(n^3)
space_complexity: O(n)
neetcode_url: https://neetcode.io/problems/minimum-window-with-characters/question
---

## Problem Description

Given two strings `s` and `t`, return the shortest substring of `s` such that every character in `t`, including duplicates, is present in the substring. If such a substring does not exist, return an empty string `""`.

You may assume that the correct output is always unique.

**Example 1:**

**Input:** s = "OUZODYXAZV", t = "XYZ"  
**Output:** "YXAZ"  
**Explanation:** "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

**Example 2:**

**Input:** s = "xyz", t = "xyz"  
**Output:** "xyz"  

**Example 3:**

**Input:** s = "x", t = "xy"  
**Output:** ""  

**Constraints:**

- `1 <= s.length <= 1000`
- `1 <= t.length <= 1000`
- `s` and `t` consist of uppercase and lowercase English letters.

## Approach

Brute force iteration over all possible substrings. For each substring, a helper method checks if it contains all characters of `t` with at least the required frequencies using `HashMap`s. Track the minimum valid substring found.

## Solution

```java
class Solution {
    public String minWindow(String s, String t) {
        int n = s.length();
        int m = t.length();
        if(n<m){
            return "";
        }
        int minlength = n;
        String returnString = "";

        for(int i=0;i<n;i++){
            for(int j=i;j<n+1;j++){
                String substr = s.substring(i, j);
                if(isValid(substr, t)){
                    minlength = Math.min(substr.length(), minlength);
                    if(substr.length()==minlength){
                        returnString = substr;
                    }
                }   
            }
        }
        return returnString;
    }
    public static boolean isValid(String s, String t){
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();
        for(int i=0;i<t.length();i++){
            char c = t.charAt(i);
            map2.put(c, map2.getOrDefault(c,0)+1);
        } 

        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(map2.containsKey(c)){
                map1.put(c, map1.getOrDefault(c,0)+1);
            }
        }
        
        for(Map.Entry<Character, Integer> entry: map2.entrySet()){
            char c = entry.getKey();
            int n1 = map1.getOrDefault(c, 0);
            int n2 = map2.getOrDefault(c, 0);
            if(n2>n1){
                return false;
            }
        }
        return true;
    }
}
```
