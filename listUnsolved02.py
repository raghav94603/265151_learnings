
def update_list(usr_list):
    new_list=[]
    for i in range(len(usr_list)):
        usr_list[i],usr_list[i+1]=usr_list[i+1],usr_list[i]
        return usr_list

usr_list= list(map(int, input().split()))
print(update_list(usr_list))