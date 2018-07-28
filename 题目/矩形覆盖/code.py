# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if(0 >= number):
            return 0
        elif (1 == number):
            return 1
        elif (2 == number):
            return 2
        else:
            f1 = 1
            f2 = 2
            f3 = 0
            for i in range(3,number+1):
                f3 = f1+f2
                f1 = f2
                f2 = f3   
            return f3