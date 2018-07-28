# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or not k:
            return None
        left, right = head, head
        for i in range(k - 1):
            if not right.next:
                return None
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        return left