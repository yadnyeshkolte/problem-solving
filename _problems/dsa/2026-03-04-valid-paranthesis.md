---
title: "Valid Parentheses"
leetcode_url: "https://neetcode.io/problems/validate-parentheses/question"
difficulty: "Easy"
topics: ["String", "Stack"]
category: "DSA"
date: 2026-03-04
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description

You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`.

The input string `s` is valid if and only if:

1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return `true` if `s` is a valid string, and `false` otherwise.

**Example 1:**

**Input:** s = "[]"  
**Output:** true  

**Example 2:**

**Input:** s = "([{}])"  
**Output:** true  

**Example 3:**

**Input:** s = "[(])"  
**Output:** false  
**Explanation:** The brackets are not closed in the correct order.

**Constraints:**

- `1 <= s.length <= 1000`

## Approach

Use a stack to keep track of open brackets. Iterate through the string, pushing open brackets onto the stack. When a close bracket is encountered, check if the stack is not empty and if the top of the stack matches the type of the current close bracket. If it does, pop from the stack; otherwise, the string is invalid. At the end, if the stack is empty, it means all brackets were matched correctly.

## Solution

```java
class Solution {
    public boolean isValid(String s) {
        int n = s.length();
        Stack<Character> st = new Stack<>();
        for(int i=0;i<n;i++){
            if(s.charAt(i)=='(' || s.charAt(i)=='[' || s.charAt(i)=='{'){
                st.push(s.charAt(i));
            }
            else{
                if(!st.isEmpty() && ((st.peek()=='(' && s.charAt(i)==')') 
                || (st.peek()=='[' && s.charAt(i)==']') || (st.peek()=='{' && s.charAt(i)=='}'))){
                    st.pop();
                }
                else{
                    return false;
                }
            }
        }
        return st.isEmpty();
    }
}
```
