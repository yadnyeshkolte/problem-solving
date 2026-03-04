---
title: "Evaluate Reverse Polish Notation"
leetcode_url: "https://neetcode.io/problems/evaluate-reverse-polish-notation/question"
difficulty: "Medium"
topics: ["Array", "Math", "Stack"]
category: "DSA"
date: 2026-03-04
time_complexity: "O(n)"
space_complexity: "O(n)"
---

## Problem Description

You are given an array of strings `tokens` that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

- The operands may be integers or the results of other operations.
- The operators include `'+'`, `'-'`, `'*'`, and `'/'`.
- Assume that division between integers always truncates toward zero.

**Example 1:**

**Input:** tokens = ["1","2","+","3","*","4","-"]  
**Output:** 5  
**Explanation:** ((1 + 2) * 3) - 4 = 5  

**Constraints:**

- `1 <= tokens.length <= 1000`
- `tokens[i]` is `"+"`, `"-"`, `"*"`, or `"/"`, or a string representing an integer in the range `[-100, 100]`.

## Approach

Use a stack to evaluate the expression. Iterate through the `tokens` array. If the token is a number, push it onto the stack. If the token is an operator, pop the required number of operands from the stack (usually two), perform the operation, and push the result back onto the stack. At the end of the iteration, the stack will contain a single element, which is the final result.

## Solution

```java
class Solution {
    public int evalRPN(String[] tokens) {
        int n = tokens.length;
        Stack<Integer> st = new Stack<>();
        for(int i=0;i<n;i++){
            if(!tokens[i].equals("+") && !tokens[i].equals("-") && !tokens[i].equals("*") && !tokens[i].equals("/")){
                st.push(Integer.parseInt(tokens[i]));
            }
            else if(tokens[i].equals("+") || tokens[i].equals("-") || tokens[i].equals("*") || tokens[i].equals("/")){
                int num2 = st.pop();
                int num1 = st.pop();
                if(tokens[i].equals("+")){
                    st.push(num1+num2);
                }
                else if(tokens[i].equals("-")){
                    st.push(num1-num2);
                }
                else if(tokens[i].equals("*")){
                    st.push(num1*num2);
                }
                else{
                    st.push(num1/num2);
                }
            }
        }
        return st.pop();
    }
}
```
