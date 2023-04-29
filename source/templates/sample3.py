data = list(map(int,input().split(" ")))
number=int(input())

n = len(data)
list1=[]
for i in range(n):
    if(data[i]==number):
        list1.append(str(data[i]))
    else:
        data.append(str(data[i]))

print(' '.join(data[n:]+list1))