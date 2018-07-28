# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        if pushV == None or popV == None or len(pushV) != len(popV):
            return False
        else:
            j = 0 
            for i in range(len(pushV)):
                stack.append(pushV[i])
                while stack and stack[-1] == popV[j] :
                    stack.pop()
                    j = j + 1
            
            return len(stack)== 0
           