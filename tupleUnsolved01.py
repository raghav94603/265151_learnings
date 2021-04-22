usr_tuple= tuple(map(int, input().split()))
print("The Repeated Elements of tuple are :")
for i in usr_tuple:
    if usr_tuple.count(i) > 1:
        print(i)