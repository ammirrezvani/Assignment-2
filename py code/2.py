import random


user=0
pc=0
a=0
while a < 5:
    user_choice = int(input("please enter your choice 1_sang,2_kaghaz,3_gheychi:"))
    pc_choice = random.randint(1,3)
    print("pc choice = ",pc_choice)    

    if pc_choice == 1 and user_choice == 2:
        user+=1
    elif pc_choice == 1 and user_choice == 3:
                pc+=1    
    elif pc_choice == 2 and user_choice == 1:
                pc+=1
    elif pc_choice == 2 and user_choice == 3:
                user+=1
    elif pc_choice == 3 and user_choice == 1:
                user+=1
    elif pc_choice == 3 and user_choice == 2:
                pc+=1
    a+=1           
print("pc = ",pc)
print("user = ",user)
