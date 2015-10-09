__author__ = 'qyuan'

# from ghost import Ghost
#
# ghost = Ghost()
# session = ghost.start()
# page, extra_resources = session.open('http://www.abcfund.cn/style/fundlist.php')
# print session.content

f = open('fund_data', 'rU')
w = open('clean_data', 'w')
c = ''
s = ''
flag = False
while c != '|':
    if r'<td>' in s or r'</td>' in s:
        s = ''
        flag = True
    c = f.read(1)
    if c == r'<' and flag == True:
        if s != '' and '%' not in s:
            # # w.write(s.strip())
            # if counter < 11:
            #     if counter != 2 and counter != 3:
            #         w.write(s.strip())
            #         w.write(' ')
            #     counter += 1
            # else:
            #     w.write('\r\n')
            #     counter = 0
            w.write(s.strip())
            w.write('\n')
        s = ''
        flag = False
    s += c

f = open('clean_data', 'rU')
w = open('info', 'w')
counter = 0

for str in f:
    if counter <= 10:
        if counter != 2 and counter != 3:
            w.write(str.strip())
            w.write('|')
        counter += 1
    else:
        counter = 1
        w.write('\n')
        w.write(str.strip())