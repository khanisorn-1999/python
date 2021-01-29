x = [int(i) for i in input().split()]
a=0
b=0
c=0
for i in x:
    if i>a:
        a=i
        c=b
    b+=1
print(c)
    
    
