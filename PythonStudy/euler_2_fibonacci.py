f1 = 1
f2 = 2
count = 0
while True:
    if f1 % 2 == 0:
        count = count + f1
    f1,f2 = f2,f1+f2
    if f1 > 4000000:
        break
print count