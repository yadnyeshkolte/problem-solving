---
title: "Group Anagrams"
leetcode_url: "https://neetcode.io/problems/anagram-groups/question"
difficulty: "Medium"
topics: ["Array", "Hash Table", "String", "Sorting"]
category: "DSA"
date: 2026-02-14
time_complexity: "O(m * n)"
space_complexity: "O(m * n)"
---

## Problem Description

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**
```
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

**Example 2:**
```
Input: strs = ["x"]
Output: [["x"]]
```

**Example 3:**
```
Input: strs = [""]
Output: [[""]]
```

**Constraints:**
- 1 <= strs.length <= 1000
- 0 <= strs[i].length <= 100
- strs[i] is made up of lowercase English letters

## Approach

Use a HashMap where the key represents the character frequency pattern of each string, and the value is a list of strings that match that pattern.

**Key Insights:**
1. Anagrams have the same character frequencies
2. Use a frequency array of size 26 (for 'a' to 'z') as the key
3. Convert the frequency array to a string to use as HashMap key
4. Group all strings with the same frequency pattern together



## Solution

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> mat = new ArrayList<>();
        if(strs.length==1){
            List<String> single = new ArrayList<>();
            single.add(strs[0]);
            mat.add(single);
            return mat;
        }


        for(int i=0;i<strs.length;i++){
            List<String> decoy = new ArrayList<>();
            boolean bool = false;
            if(strs[i].equals("0")==false){
                for(int j=0;j<strs.length;j++){
                    if(checkAnagrams(strs[i],strs[j])==true && strs[j].equals("0")==false && i!=j){
                        decoy.add(strs[j]);
                        strs[j] = "0";
                        bool = true;
                    }
                }
                if(bool==true){
                    decoy.add(strs[i]);
                    strs[i] = "0";
                }
            }
            if(decoy.size()>0){
                mat.add(decoy);
            }

        }

        for(String s: strs){
            if(s.equals("0") == false){
                List<String> single = new ArrayList<>();
                single.add(s);
                mat.add(single);
            }
        }
        return mat;
    }
    public boolean checkAnagrams(String s1, String s2){
        if(s1.length()!=s2.length()){
            return false;
        }
        HashMap<Character, Integer> hs1 = new HashMap<>();
        HashMap<Character, Integer> hs2 = new HashMap<>();

        for(int i=0;i<s1.length();i++){
            char x = s1.charAt(i);
            if(hs1.containsKey(x)){
                hs1.put(x, hs1.get(x)+1);
            }
            else{
                hs1.put(x, 1);
            }
        }

        for(int i=0;i<s2.length();i++){
            char x = s2.charAt(i);
            if(hs2.containsKey(x)){
                hs2.put(x, hs2.get(x)+1);
            }
            else{
                hs2.put(x, 1);
            }
        }
        return hs1.equals(hs2);
    }
}
```

Time Complexity = `O(n^2 * k)`
Space Complexity = `O(n * k)` 


**Alternative Solution (Using Sorting - O(m * n log n)):**

```java

```