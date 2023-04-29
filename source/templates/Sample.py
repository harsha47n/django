test = int(input())

def prod(data):
    f=1
    for i in data:
        f*=i
    return f

for i in range(test):
    data = list(map(int,input().split(" ")))
    max_prod=1
    for i in range(0,len(data)-1):
        for j in range(i+1,len(data)+1):
            max_prod = max(max_prod,prod(data[i:j]))

    print(max_prod)

