def isNum(n):
    try:
        i = int(n)
    except ValueError:
        return False
    else:
        return True
def jia(x,y):
    return x+y
 
def jian(x,y):
    return x-y
 
def cheng(x,y):
    return x*y
 
def chu(x,y):
    return int(float(x)/y) 
 
operator = {'+':jia,'-':jian,'*':cheng,'/':chu}
 
def f(x,o,y):
    return operator.get(o)(x,y)
 

class Solution:
    # @param tokens, a list of string
    # @return an integer\
    def evalRPN(self, tokens):
        stack = list()
        for i, ch in enumerate(tokens):
            if isNum(ch):
                stack.append(int(ch))
            else:
                x = stack.pop()
                y = stack.pop()
                z = f(y,ch,x)
                stack.append(z)
                
        return stack.pop()

s = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(tokens)