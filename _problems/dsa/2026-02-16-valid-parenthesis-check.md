---
title: "Valid Parenthesis Check"
difficulty: "Easy"
topics: ["Stack", "String"]
category: "DSA"
date: 2026-02-16
time_complexity: "O(n)"
space_complexity: "O(n)"
source: "Practice"
---

## Problem Description

Given a string containing only brackets `()[]{}`, determine whether it is valid.

## Approach

Use a stack:
1. Push opening brackets.
2. For every closing bracket, check whether it matches the top element.
3. The string is valid only if the stack is empty at the end.

## Solution

```java
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) return false;
                char top = stack.pop();
                if ((ch == ')' && top != '(') ||
                    (ch == ']' && top != '[') ||
                    (ch == '}' && top != '{')) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
```
