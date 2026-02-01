---
title: "Evaluate Reverse Polish Notation"
leetcode_url: "https://leetcode.com/problems/evaluate-reverse-polish-notation/"
difficulty: "Medium"
topics: ["Array", "Stack", "Math"]
category: "DSA"
date: 2026-02-01
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

## Approach
Reverse Polish Notation (also called Postfix Notation)

## Solution

```java
import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/")) {
 
                int b = stack.pop();
                int a = stack.pop(); 
                switch (token) {
                    case "+":
                        stack.push(a + b);
                        break;
                    case "-":
                        stack.push(a - b);
                        break;
                    case "*":
                        stack.push(a * b);
                        break;
                    case "/":
                        stack.push(a / b); 
                        break;
                }
            } else {

                stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }
}
```