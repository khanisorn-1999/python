a=input()
# input as 1000!
a=int(a[0:-1])
mem = {}
sum=0
def fac(n):
    if n == 0 or n == 1:
        return 1
    if n not in mem:
        mem[n]=(fac(n-1)+fac(n-2))*(n-1) # using memorization
        return mem[n]
    return mem[n]
b=str(fac(a))
for i in range(len(b)-1,-1,-1):
    if b[i]=='0':
        sum+=1
    else:
        break
print(sum)
