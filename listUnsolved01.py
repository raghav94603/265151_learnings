#Using inbuilt list and map functions
arr= list(map(int, input().split()))

#Inbuilt Sort Functions
arr.sort()
min_element=arr[0]
for sec_min in arr:
    if sec_min!=min_element:
        result=sec_min
        print(result)
        break