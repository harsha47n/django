test_cases = int(input())

for i in range(test_cases):

    data = list(map(int,input().split(" ")))

    n = len(data)
    min_element = min(data)
    min_element_index= data.index(min_element)
    if(min_element_index==n-1):
        print(0)
    else:
        max_value=0
        for j in range(min_element_index,n):
            max_value = max(max_value,abs(data[j]-min_element))
        print(max_value)