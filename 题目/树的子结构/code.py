# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if  pRoot1 == None or pRoot2 == None:
            return False
        else:
            return self.IsSubtree(pRoot1,pRoot2) or self.IsSubtree(pRoot1.left,pRoot2) or self.IsSubtree(pRoot1.right,pRoot2) 
        
    def IsSubtree(self,a,b):
        if   b == None:  
            return True  
        if   a == None:
            return False
        if a and b:  
            if a.val!= b.val:  
                return False  
            return self.IsSubtree(a.left,b.left) and self.IsSubtree(a.right,b.right)  
        else:  
            return False  