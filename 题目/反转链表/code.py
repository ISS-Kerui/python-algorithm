# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead == None or pHead.next == None: #边界条件
            return pHead
        cur = pHead #循环变量
        tmp = None #保存数据的临时变量
        newhead = None #新的翻转单链表的表头
        while cur:
            tmp = cur.next 
            cur.next = newhead
            newhead = cur   # 更新 新链表的表头
            cur = tmp
        return newhead