---
title: Longest Substring Without Repeating Characters
difficulty: Medium
topics:
- String
- Sliding Window
- Hash Set
category:
- DSA
- NeetCode
date: 2026-02-27
time_complexity: O(n)
space_complexity: O(m)
neetcode_url: https://neetcode.io/problems/longest-substring-without-duplicates/question
---

## Problem Description

Given a string `s`, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

**Example 1:**

Input: `s = "zxyzxyz"`

Output: `3`
Explanation: The string "xyz" is the longest without duplicate characters.

**Example 2:**

Input: `s = "xxxx"`

Output: `1`

**Constraints:**
- `0 <= s.length <= 1000`
- `s` may consist of printable ASCII characters.

### Hints
**Hint 1:** A brute force solution would be to try the substring starting at index i and try to find the maximum length we can form without duplicates by starting at that index. We can use a hash set to detect duplicates in O(1) time. Can you think of a better way?

**Hint 2:** We can use the sliding window algorithm. Since we only care about substrings without duplicate characters, the sliding window can help us maintain valid substring with its dynamic nature.

**Hint 3:** We can iterate through the given string with index r as the right boundary and l as the left boundary of the window. We use a hash set to check if the character is present in the window or not. When we encounter a character at index r that is already present in the window, we shrink the window by incrementing the l pointer until the window no longer contains any duplicates. Also, we remove characters from the hash set that are excluded from the window as the l pointer moves. At each iteration, we update the result with the length of the current window, r - l + 1, if this length is greater than the current result.

## Approach

- **Initial Approach (Brute Force):** Iterate through all possible substrings using two nested loops. For each substring, check if it contains duplicate characters using a `HashSet`. Track the maximum length found. This solution is easier to think of but less optimal in terms of time complexity.
- **Optimized Approach (Sliding Window):** Use two pointers (`left` and `right`) to represent a sliding window over the string. Iterate through the string with the `right` pointer, adding characters to a `HashSet`. If a duplicate is found, remove characters from the `left` pointer and shrink the window until the duplicate is gone. Update the maximum length at each valid step.

## Solution

### 1. Initial Solution (By me)

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int max = 0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n+1;j++){
                String str = s.substring(i,j);
                if(isDuplicate(str)){
                    max = Math.max(max, str.length());
                }
            }
        }
        return max;
    }
    public static boolean isDuplicate(String str){
        HashSet<Character> hash = new HashSet<>();
        for(int i=0;i<str.length();i++){
            if(!hash.add(str.charAt(i))){
                return false;
            }
            else{
                hash.add(str.charAt(i));
            }
        }
        return true;
    }

}
```

### 2. Optimized Solution

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int left = 0, right = 0;
        int maxlength = 0;
        HashSet<Character> ht = new HashSet<>();
        while(right<n){
            char currentchar = s.charAt(right);
            if(!ht.contains(currentchar)){
                ht.add(currentchar);
                maxlength = Math.max(maxlength, (right-left+1));
                right++;
            }
            else{
                ht.remove(s.charAt(left));
                left++;
            }

        }
        return maxlength;
    }

}
```