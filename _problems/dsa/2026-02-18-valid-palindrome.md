---
title: "Valid Palindrome"
leetcode_url: "https://neetcode.io/problems/is-palindrome/question"
difficulty: "Easy"
topics: ["String", "Two Pointers"]
category: "DSA"
date: 2026-02-18
time_complexity: "O(n)"
space_complexity: "O(1)"
---

## Problem Description

Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Note:** Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

**Example 1:**

```
Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
```

**Example 2:**

```
Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.
```

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s` is made up of only printable ASCII characters.

## Approach

A brute force solution would be to create a copy of the string, reverse it, and then check for equality. This would be an `O(n)` solution with extra `O(n)` space.

However, we can solve this with `O(1)` space by using the **Two Pointers** technique.

1.  Initialize two pointers: `start` at the beginning (`0`) and `end` at the end (`n-1`) of the string.
2.  While `start < end`:
    *   Move `start` forward until an alphanumeric character is found.
    *   Move `end` backward until an alphanumeric character is found.
    *   Compare characters at `start` and `end` (ignoring case). If they differ, return `false`.
    *   Increment `start` and decrement `end`.
3.  If the loop completes, it's a palindrome. Return `true`.

## Solution

```java
class Solution {
    public boolean isPalindrome(String s) {
        int n = s.length();
        int start = 0;
        int end = n-1;
        while(start<end){
            if(!Character.isLetterOrDigit(s.charAt(start))){
                start++;
                continue;
            }
            if(!Character.isLetterOrDigit(s.charAt(end))){
                end--;
                continue;
            }
            if(Character.toLowerCase(s.charAt(start))!=Character.toLowerCase(s.charAt(end))){
                return false;
            }
            start++;
            end--;
        }

        return true;
    }
}
```
