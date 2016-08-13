__author__ = 'sweety'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        preRet = 0
        ret = 1
        negativeRet = 0
        if set(nums) == set([0]):
            return 0

        length = len(nums)
        if length == 1:
            return nums[0]
        for x in xrange(length):
            if nums[x] >= 0:
                ret *= nums[x]
                if ret > preRet:
                    preRet = ret

            else:
                temp = ret
                ret *= nums[x]
                if temp > ret:
                    preRet = temp


        if preRet > ret:
            ret = preRet
        if negativeRet > ret:
            ret = negativeRet
        return ret

a = [-2,0,1]

s = Solution()
print s.maxProduct(a)