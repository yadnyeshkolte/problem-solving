https://neetcode.io/problems/merge-two-sorted-linked-lists/question



https://leetcode.com/problems/merge-two-sorted-lists/description/


Merge Two Sorted Linked Lists
Solved 
Easy
Topics
Company Tags
Hints
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100





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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode list3 = new ListNode(0);
        ListNode head = list3;
        while(list1!=null && list2!=null){
            if(list1.val<=list2.val){
                list3.next = new ListNode(list1.val);
                list1 = list1.next;
            }
            else{
                list3.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            list3 = list3.next;
        }
        while(list1!=null){
            list3.next = new ListNode(list1.val);
            list1 = list1.next;
            list3 = list3.next;
        }
        while(list2!=null){
            list3.next = new ListNode(list2.val);
            list2 = list2.next;
            list3 = list3.next;
        }
        return head.next;
    }
}