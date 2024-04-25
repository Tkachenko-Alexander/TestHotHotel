a = int(1)
b = int(input())
c = int(1)
d = b
for g in range(c, d+1):
    print('\t'+str(g), end='')
print(end='\n')
for i in range(a, b+1):
    print(str(i)+'\t', end='')
    for j in range(c, d+1):
        print(str(i*j), end='\t')
    print(end='\n')
