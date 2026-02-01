---
title: "How Many Numbers Are Smaller Than the Current Number"
leetcode_url: "https://leetcode.com/problems/build-an-array-with-stack-operations/"
difficulty: "Easy"
topics: ["Array", "Stack", "Simulation"]
category: "DSA"
date: 2026-02-01
time_complexity: "O(n)"
space_complexity: "O(1)"
---

## Problem Description
You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

"Push": pushes an integer to the top of the stack.
"Pop": removes the integer on the top of the stack.
You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:

If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
If the stack is not empty, pop the integer at the top of the stack.
If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.

## Approach
Simulation with Early Exit

## Solution

```java
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> result = new ArrayList<>();
        int streamNum = 1;
        int targetIndex = 0;

        while (targetIndex < target.length) {
            result.add("Push");

            if (target[targetIndex] == streamNum) {
                targetIndex++;
            } else {

                result.add("Pop");
            }
            streamNum++;
        }

        return result;
    }
}
```