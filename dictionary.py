# # user = {'name':'priyal'}
# # print(user)
# # # this function for add a value in dicitionary
# # user['email']="sanajanvtr@gmail.com"
# # print(f'after adding email{user}')
# # user['email']="sanajanv@gmail.com"
# # print(f'after replace email{user}')
# # print(f'name print through{user.get("name")}')

# user = {'name':'tevanshi'}
# print(user)
# aman_contact = 123456789
# ravi_contact = 987654321
# palak_contact = 456789123
# khusbhu_contact = 789123456
# contact = {'user':user,
#            'aman_contact':aman_contact,
#            'ravi_contact':ravi_contact,
#            'palak_contact':palak_contact,
#            'khusbhu_contact':khusbhu_contact,}
# print(contact)
# user['new contact'] = "456951237"
# print(f'adding a new contact{user}')
# # print(f'delete contact through{user.pop("palak_contact")}')
# print(f'update no through{user.update({"aman_contact":aman_contact})} ')
# # print(f'count count through {})


# cotact list banane ka tarika
user_list = [{'user_name'== 'sanjana'},
             {'user_name'== 'sakshi'},
             {'user_name'=='manoj'},
             {'user_name'=='nikita'}]
def add_user():
    user_name = input("please add a contact\n Please enter your name: ")
    mobile_no = input("Please enter your mobile no: ")
    last_user = user_list[len(user_list)-1]
    id = last_user["id"]+1
    user = {"id":id,'user_name':user_name, 'mobile_no':mobile_no}
    user_list.append(user)
def delete_contact():
    name = input("Please enter a name to delete: ")
    for i in user_list:
        if i["user_name"]==name:
            user_list.remove(i)
            print("contact delete successfully")
def search_contact():
    letter = input("Please enter a letter: ")
    for j in user_list:
        if j["user_name"].startswith(letter): 
            print(d)



def dics():
    is_loop =True
    while is_loop:
        if len(user_list) == 0 :
            user_name = input("please add a contact\n Please enter your name: ")
            mobile_no = input("Please enter your mobile no: ")
            user = {"id":1,'user_name':user_name, 'mobile_no':mobile_no}
            user_list.append(user)
        else:
            print(f'these are the users\n{user_list}\n Please enter A if you want to add new contact\n Please enter E for exit\n Please enter D for delete')
            print('total contact :',len (user_list))
            options=input('Please choose A or E or D or S: ')
            if options=="A":
                add_user()
            elif options=="D":
                delete_contact()       
            elif options=="S":
                search_contact()

            else:
                is_loop =False
 
                

   
dics()
if len(user_list) == 0:
    add_user()
else: 
    print(f"these are the user list")    



