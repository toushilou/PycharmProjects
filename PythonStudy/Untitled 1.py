a = ('123'#test
'456')

print a

list = ['a','b','c']
list[1] = 'd'

print list

se = ['a', 'b', 'c', 'd'] 
print se[1:-2]

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        d = {}
        i = len(s)
        l = []
        index = 0
        flag = False
        if i < 10:
            return l
        else:
            while index <= i - 10:
                substr = s[index:index+10]
                if d.has_key(substr):
                    for str in l:
                        if str == substr:
                            flag = True
                            break
                    if not flag:
                        l.append(substr)
                else:
                    d[substr] = 1
                index += 1
        return l


if __name__ == '__main__':
    sl = Solution()
    s = "AAAAAAAAAAAA"
    print sl.findRepeatedDnaSequences(s)
    
    for i in range(10):
        print i