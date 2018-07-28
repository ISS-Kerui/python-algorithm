# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        result = 1
        if exponent == 0:
            return 1
        else:
            for i in range(abs(exponent)):
                if exponent >0:
                    result =result*base
                else:
                    result = result *(1.0/base)
            return result