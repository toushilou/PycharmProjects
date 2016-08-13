class Solution:
    def Find(self, array, target):
        # write code here
        row = len(array)
        index = 0

        while index < row:
            low = 0
            high = len(array[0]) - 1
            while low <= high:
                middle = (low + high) >> 1
                if array[index][middle] < target:
                    low = middle + 1
                elif array[index][middle] > target:
                    high = middle - 1
                else:
                    return True
            index = index + 1
        return False

s = Solution()
l1 = [1,2,8,9]
l2 = [2,4,9,12]
l3 = [4,7,10,13]
l4 = [6,8,11,15]
array = [l1,l2,l3,l4]
print s.Find(array, 7)