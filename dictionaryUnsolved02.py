user_list =list(map(int, input().split()))
nested_dict = current = {}
for i in user_list:
    current[i] = {}
    current = current[i]
print(nested_dict)