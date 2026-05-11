# Q1. Given  the  Python  code  below,  manually  trace  the  execution  for  each 
# set of values. Provide the final output that would appear on the screen 
# for each case. 
# a) i=3, j=5, k=7
# Answer: 5 5 7
# i,j,k=3,5,7 

# b) i=-2, j=-5, k=9
# Answer: 9 -5 9
# i,j,k=-2,-5,9

# c) i=8, j=15, k=12
# Answer: 8 12 12
# i,j,k=8,15,12

# d) i=13, j=15, k=13
# Answer: 13 13 13
# i,j,k=13,15,13

# e) i=3, j=5, k=17
# Answer: 5 5 17
# i,j,k=3,5,17

# f) i=25, j=15, k=17
# Answer: 17 15 17
# i,j,k=25,15,17
# if i < j:
#     if j < k:  
#        i=j
#     else:
#         j=k
# else:
#     if j > k:
#         j=i
#     else:
#         i=k
# print(i,j,k)
 
# 2.  Given  the  Python  code  below,  manually  trace  the  execution  for  each 
# set of values. Provide the final output that would appear on the screen 
# for each case." 
 
 
# a)  i=3, j=5, k=7 
# i,j,k=3,5,7
# Answer: 3 5 3

# b) i=-2, j=-5, k=9 
# i,j,k=-2,-5,9
# Answer: -2 -2 9

# c)  i=8, j=15, k=12 
# i,j,k=8,15,12
# Answer: 15 15 12

# d) i=13, j=15, k=13 
# i,j,k=13,15,13
# Answer: 15 15 13

# e)  i=3, j=5, k=17 
# i,j,k=3,5,17
# Answer: 3 5 3

# f)  i=25, j=15, k=17
# i,j,k=25,15,17
# Answer: 25 25 17

# if j < k:
#     if i > j:  
#        j=i
#     else:
#         k=i
# else:
#     if j > k:
#         i=j
#     else:
#         k=i
# print(i,j,k)

# Q3.  Given  the  Python  code  below,  manually  trace  the  execution  for  each 
# set  of.  Provide  the  final  output  that  would  appear  on  the  screen  for 
# each case. 
 
# a)  i=3, j=5, k=7 
i,j,k=3,5,7
# answer: 5 5 7

# b) i=-2, j=-5, k=9 
# i,j,k=-2,-5,9
# answer: -5 -5 9

# c)  i=8, j=15, k=12 
# i,j,k=8,15,12
# answer: 15 15 12

# d) i=13, j=15, k=13 
# i,j,k=13,15,13
# answer: 13 15 13

# e)  i=3, j=5, k=17 
# i,j,k=3,5,17
# answer: 5 5 17

# f)  i=25, j=15, k=17 
i,j,k=25,15,17
# answer: 25 25 17

if  k < i:
    if i > j:  
       j=i
    else:
        k=i
else:
    if k > i:
        i=j
    else:
        k=i
print(i,j,k)
 
# Q4.  Design a program for a 'Student Resource Portal.' The program should 
# ask for a username and a password. 
#   If  the  username  is  admin  and  password  is  ad123,  print 
# Access Granted: Faculty Dashboard. 
#   If the username is  student  and password  is st2026, print 
# Access Granted: Notes and Practice Questions. 
#   For any other combination, print Invalid Credentials. 
# Please try again.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard.")
elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions.")
else:
    print("Invalid Credentials. Please try again.")

# Q5.  Write  a  Python  program  that  calculates  a  customer's  final  bill  based 
# on their spending and membership status. The program should follow 
# the exact logic shown in the flowchart below.
total_spent = float(input("Enter total amount spent: "))
membership_status = input("Do you have membership? Enter 1 for yes and 2 for no: ")

if total_spent > 5000:
    if membership_status == "1":
        discount = total_spent * 0.3
        final_price = total_spent - discount
        print('Congratulations! You have received a 30% discount.')
        print('Calculating final bill...')
        print(f"Final bill after discount: {final_price}")
    elif membership_status == "2":
        print("No discount applied. Final bill: ", total_spent)
    else:
        print("Invalid input for membership status. Please enter 1 for yes and 2 for no.")
else:
    print("No discount applied. Final bill: ", total_spent)


# Q6.  Create  a  Python  program  for  a  text-based  adventure  game  called 
# Magic Forest based on the given flowchart. The program should follow 
# the exact logic shown in the flowchart.
print("Welcome to the Magic Forest!")
direction = input("Do you want to go North or South? (Enter 'N' or 'S'): ").lower()
if direction == 's':
    print("You have entered the Dark Cave. Game Over.")
elif direction == 'n':
    print("You have entered the Stage 2 of the Magic Forest.")
    action = input("Do you want to cross the river or follow the path? (Enter 'r' or 'p'): ").lower()
    if action == 'r':
        print("You have crossed the river safely. Game Over.")
    elif action == 'p':
        print("You have entered the Stage 3 of the Magic Forest.")
        choice = input("Do you want to choose fairy , ogre or elf? (Enter 'f' for fairy, 'o' for ogre, or 'e' for elf): ").lower()
        if choice == 'f':
            print("You have chosen the fairy.Game Over.")
        elif choice == 'o':
            print("You have chosen the ogre. You lose! Game Over.")
        elif choice == 'e':
            print("You have chosen the elf. You win! Game Over.")
        else:
            print("Invalid choice. Please enter 'f', 'o', or 'e'.")
    else:
        print("Invalid action. Please enter 'r' or 'p'.")
else:
    print('Invalid command .You must enter s or n')