# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        left = [x for x in array if x & 1 == 1]
        right = [x for x in array if x & 1 == 0]
        return left + right