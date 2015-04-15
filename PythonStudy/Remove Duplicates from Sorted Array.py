class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        j = 1
        size = len(A)
        while j < size:
            if A[i] == A[j]:
                i += 1
                A[i] = A[j]
        return i + 1    
test = Solution()
