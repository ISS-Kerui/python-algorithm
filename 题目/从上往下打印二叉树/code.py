## -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        A = []
        result = []
        if not root:
            return result
        A.append(root)
        while A:
            current_root = A.pop(0)
            result.append(current_root.val)
            if current_root.left:
                A.append(current_root.left)
            if current_root.right:
                A.append(current_root.right)
        return result 