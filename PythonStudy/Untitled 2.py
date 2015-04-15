def isNum(n):
    try:
        n + 1
    except TypeError:
        return False
    else:
        return True


class Solution:
    # @param tokens, a list of string
    # @return an integer\
    def evalRPN(self, tokens):
        