---
title: 2026 03 14 Reverse Linkedlist
category:
- DSA
- LeetCode
- NeetCode
leetcode_url: https://leetcode.com/problems/reverse-linked-list/description/
neetcode_url: https://neetcode.io/problems/reverse-a-linked-list/question
---

Reverse Linked List
Solved 
Easy
Topics
Company Tags
Hints
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000


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
