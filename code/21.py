# -*- Encoding:UTF-8 -*-

# 21. Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val > l2.val:
            tmp = l2
            tmp.next = self.mergeTwoLists(l1, l2.next)
            return tmp
        else:
            tmp = l1
            tmp.next = self.mergeTwoLists(l1.next, l2)
            return tmp
