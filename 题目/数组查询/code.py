# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        rows = len(array)
        cows = len(array[0])
        row = 0
        cow = cows - 1
        while row>=0 and row<rows and cow >=0 and cow<cows:
            if array[row][cow] == target:
                return True
            elif array[row][cow] > target:
                cow = cow - 1
            else:
                row = row + 1
                
        return False
        # write code here