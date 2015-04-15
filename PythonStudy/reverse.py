class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
s = Solution()

print s.reverseWords("the sky is blue!")

