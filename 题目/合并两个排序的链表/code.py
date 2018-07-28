# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None and pHead2 is None:
            return None
        new_list = ListNode(0)
        pre = new_list
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val < pHead2.val:
                pre.next = pHead1
                pHead1 = pHead1.next
            else:
                pre.next = pHead2
                pHead2 = pHead2.next
            pre = pre.next
        if pHead1 is not None:
            pre.next = pHead1
        else:
            pre.next = pHead2
        return new_list.next