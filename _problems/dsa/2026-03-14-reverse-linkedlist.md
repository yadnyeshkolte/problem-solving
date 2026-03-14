---
title: "Reverse Linked List"
leetcode_url: "https://leetcode.com/problems/reverse-linked-list/description/"
neetcode_url: "https://neetcode.io/problems/reverse-a-linked-list/question"
difficulty: "Easy"
topics: ["Linked List", "Recursion"]
category: ["DSA", "LeetCode", "NeetCode"]
date: 2026-03-14
time_complexity: "O(n)"
space_complexity: "O(1)"
---

## Problem Description

Given the beginning of a singly linked list `head`, reverse the list, and return the new beginning of the list.

**Example 1:**

**Input:** head = [0,1,2,3]  
**Output:** [3,2,1,0]

**Example 2:**

**Input:** head = []  
**Output:** []

**Constraints:**

- `0 <= The length of the list <= 1000`
- `-1000 <= Node.val <= 1000`

## Approach

Use an iterative approach with two pointers: `prev` (initially `null`) and `current` (initially the `head`). Traverse the linked list, and at each step, temporarily store the `nextStep` node, then reverse the current node's `next` pointer to point to `prev`. Move `prev` and `current` one step forward. Continue this process until `current` becomes `null`, at which point `prev` pointing to the new head of the reversed list is returned. This runs in `O(n)` time complexity and `O(1)` space complexity.

## Solution

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        while(current!=null){
            ListNode nextStep = current.next;
            current.next = prev;
            prev = current;
            current = nextStep;
        }
        return prev;
        
    }
}
```
