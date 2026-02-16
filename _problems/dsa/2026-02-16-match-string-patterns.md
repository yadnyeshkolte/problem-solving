---
title: "Match String Patterns"
difficulty: "Easy"
topics: ["Hash Map", "String"]
category: "DSA"
date: 2026-02-16
source: "Raja Software Labs Question Test"
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description

Given a pattern string and a sentence, check whether the sentence follows the same pattern.

Each character in the pattern should map to exactly one word, and each word should map to exactly one character.

**Example 1:**
```
Input: pattern = "abba", str = "cat dog dog cat"
Output: true
```

**Example 2:**
```
Input: pattern = "abbaab", str = "cat dog dog cat horse dog"
Output: false
```

## Approach

Use two hash maps to maintain a two-way mapping:

1. Character -> Word
2. Word -> Character

At each index, both maps must stay consistent. If any mismatch occurs, return `false`.

**Key Insights:**
1. Pattern length and number of words must be equal
2. Use two maps to enforce one-to-one mapping (bijection)
3. If mapping exists, verify it
4. If mapping does not exist, create it in both maps

## Solution

```java
import java.util.Arrays;
import java.util.HashMap;
public class Solution4 {
    public static void main(String[] args) {
        String pattern = "abba";
        String str = "cat dog dog cat";

        String pattern1 = "abbaab";
        String str1 = "cat dog dog cat horse dog";

        boolean b = checkPattern(pattern1, str1);
        System.out.println(b);
    }
    public static boolean checkPattern(String pattern, String str){
        HashMap<Character, String> map = new HashMap<>();
        int n = pattern.length();
        char[] patternarray = new char[n];
        String[] strarray = str.split(" ");
        for(int i=0;i<n;i++){
            patternarray[i] = pattern.charAt(i);
        }
        for(int i=0;i<n;i++){
            if(map.containsKey(patternarray[i])){
                continue;
            }
            map.put(patternarray[i], strarray[i]);
        }

        for(int i=0;i<n;i++){
            if(map.get(patternarray[i]).equals(strarray[i])==false){
                return false;
            }
        }
        return true;
    }
}
```

Time Complexity = `O(n)`
Space Complexity = `O(n)`
