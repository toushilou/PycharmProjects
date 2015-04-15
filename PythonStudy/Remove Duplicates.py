#! /usr/bin/env python
#coding=utf-8
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count = 0
        size = len(A)
        index = 0
        while index < size - 1:
            if A[index] == A[index + 1]:
                count += 1
            else:
                A[index + 1 - count] = A[i + 1]
            index += 1
        return size - count

if __name__ == '__main__':
    A = [1,1,1,1,1]
    s = Solution()
    print s.removeDuplicates(A)
    