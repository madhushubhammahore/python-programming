n=int(input())

hash =[10]*10

new=n

while new !=0:
    hash[new%10]+=1
    new =int(new/10)

for i in range(9,-1,-1):
    for j in range(hash[i]):

        print (i, end="")