sqdEvens = [x ** 2 for x in range(8) if not x % 2]
for i,ch in enumerate(sqdEvens):
    print i,ch
    
for t in range(1,4,2):
    print t

print sqdEvens

for i in range(len(sqdEvens)):
    print i
    
print True == 0%2