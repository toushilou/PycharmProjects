# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = s.replace(' ', '%20')
        print s


s = Solution()

s.replaceSpace("we are ready ")


l = [1,2,3]

print l[::-1]