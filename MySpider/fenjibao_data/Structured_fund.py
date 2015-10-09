__author__ = 'qyuan'

# from ghost import Ghost
#
# ghost = Ghost()
# session = ghost.start()
# page, extra_resources = session.open('http://www.abcfund.cn/style/fundlist.php')
# print session.content

f = open('fund_data', 'r')
w = open('clean_data', 'w')
c = ''
s = ''
flag = False
counter = 0
while c != '|':
    if r'<td>' in s or r'</td>' in s:
        s = ''
        flag = True
    c = f.read(1)
    if c == r'<' and flag == True:
        if s != '' and '%' not in s:
            # w.write(s.strip())
            # if counter < 6:
            #     counter += 1
            #     w.write(s.strip())
            #     w.write(' ')
            # else:
            #     w.write('\r\n')
            #     counter = 0
            print s
        s = ''
        flag = False
    s += c