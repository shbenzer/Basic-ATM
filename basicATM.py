#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#user_list for storing usernames
#each user needs a list
#data_list is a list of lists
#something to keep track of index
user_list = []
data_list = []
index = -1

user_input = 0
logged_in_input = 0

while user_input != 3:
    logged_in_input = 0
    print("1.) Login\n2.) New User\n3.) Exit")
    user_input = int(input("Please pick an option: "))
    
    if user_input == 1:
        username = input("Login: ")
        while username not in user_list:
            username = input("No user, try again: ")
        index = user_list.index(username)
        while logged_in_input != 5:
            print("1.) Store a number")
            print("2.) Sum numbers")
            print("3.) Print list")
            print("4.) Clear list")
            print("5.) Logout")
            logged_in_input = int(input("Pick an option: "))
            if logged_in_input == 1:
                number = int(input("Type a number: "))
                data_list[index].append(number)
            elif logged_in_input == 2:
                print("The sum of the list is: ", sum(data_list[index]))
            elif logged_in_input == 3:
                print(data_list[index])
            elif logged_in_input == 4:
                print("List cleared!")
                data_list[index] = []
    elif user_input == 2:
        username = input("Please pick a username: ")
        while username in user_list:
            username = input("Pick another please: ")
        user_list.append(username)
        data_list.append([])
        #print(user_list)
        #print(data_list)

