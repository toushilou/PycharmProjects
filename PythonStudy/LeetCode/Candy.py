__author__ = 'sweety'

class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        total = 0
        start = 1
        length = len(ratings)
        ratings.sort()
        for x in xrange(length):
            if x != length -1:
                if ratings[x] != ratings[x + 1]:
                    total += start
                    start += 1
                else:
                    total += start
            else:
                total += start

        return total



i = [6,1,1,1,2,3,4,5,5,5,5,5]

j = [1,6,1,1,2,3,4,5,5,5,5,5]

print i.sort() == j.sort()

s = Solution()
print s.candy(i)