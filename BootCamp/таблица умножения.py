a = int(input())
b = int(input())
c = int(input())
d = int(input())


for j in range (c, d+1):
    print('\t' + str(j), end = '')
print(end="\n") 

for i in range (a, b+1):
    print(str(i) + "\t" , end = "")
    for g in range (c,d+1):
        print(str(i*g),end='\t')
    print(end='\n')