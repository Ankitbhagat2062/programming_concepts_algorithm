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


# 7.  Design  a  Traffic  Light  System.  Given  a  variable  light  that  can  be  red, 
# yellow, or green, print the correct instruction. Also handle an invalid 
# color with an error message. 
color=input('Traffic Light color : Enter red, yellow or green: ').lower()
if color == 'red':
    print("Stop")
elif color == 'yellow':
    print("Get Ready")
elif color == 'green':
    print("Go")
else:
    print("Invalid color. Please enter red, yellow, or green.")
 
# 8.  Write  a  match  statement  that  takes  a  number  1–4  and  prints  the 
# corresponding season: 1=spring, 2=summer, 3=autumn,  4=winter. 
# Default: unknown. 
number=int(input('Enter number 1,2 , 3 or 4'))
match number:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print('')
    case 4:
        print('Winter')
    case _:
        print('Unknown')
 
# 9.  Design a Bank Loan Approval System. Approve a loan only if ALL three 
# conditions are met: 
#   Age is between 21 and 60 (inclusive) 
#   Monthly income is at least 30,000 
#   Credit score is at least 700 
# If not approved, print which condition failed. 
age=int(input('Enter your age: '))
income=float(input('Enter your monthly income: '))
credit_score=int(input('Enter your credit score: '))

if 21 <= age <= 60:
    if income >= 30000:
        if credit_score >= 700:
            print("Loan Approved")
        else:
            print("Loan Denied: Credit score must be at least 700.")
    else:
        print("Loan Denied: Monthly income must be at least 30,000.")
else:
    print('You are minor Your age must be between 21 and 60 to apply for a loan.')

# 10. Write  a  Python  program  that  calculates  a  person’s  Body  Mass 
# Index  and  determines  their  weight  category  based  on  the  following 
# rules: 
# Ask the user to input their weight in float. 
# Ask the user to input their height in float. 
# Calculate the BMI using the formula: 
# BMI = weight / height² 
# Determine the weight status according to this criteria: 
# Underweight if BMI < 18.5 
# Normal weight if 18.5 <= BMI <= 25 
# Overweight if 25 <= BMI <= 30 
# Obese if BMI >=30 
# Finally, print the result in the following format: 
# Weight: 70 
# Height: 1.75 
# BMI: 22.9 Normal weight 
weight=float(input('Enter your weight in kg: '))
height=float(input('Enter your height in meters: '))
bmi=weight/(height**2)
if bmi < 18.5:
    print(f'Weight: {weight} kg')
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.1f} Underweight")
elif 18.5 <= bmi <= 25:
    print(f'Weight: {weight} kg')
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.1f} Normal weight")
elif 25 <= bmi <= 30:
    print(f'Weight: {weight} kg')
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.1f} Overweight")
elif bmi >= 30:
    print(f'Weight: {weight} kg')
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.1f} Obese")

# 11. You are developing a simple ticket booking system for a movie 
# theatre. The ticket price depends on the age of the person and 
# whether they have a membership card. If the person is under 12, the 
# ticket  is  free.  If  the  person  is  between  12  and  60:  If  they  have  a 
# membership  card,  the  ticket  costs  Rs.  150.  If  not,  the  ticket  costs  Rs. 
# 200.  If  the  person  is  above  60,  they  get  a  senior  citizen  discount, 
# and  the  ticket  costs  Rs.
# 100. Write a Python program using nested if-else to calculate and print 
# the ticket price based on the user's age and membership status. 
age=int(input('Enter your age: '))
membership_status = input("Do you have a membership card? Enter 'yes' or 'no': ").lower()
if age < 12:
    print("The ticket is free.")
elif 12 <= age <= 60:
    if membership_status == 'yes':
        print("The ticket costs Rs. 150.")
    elif membership_status == 'no':
        print("The ticket costs Rs. 200.")
    else:
        print("Invalid input for membership status. Please enter 'yes' or 'no'.")
elif age > 60:
    print('You got senior citizenship discount and ticket costs Rs 100')

# 12. A company decided to give bonus of 5% to employee if his/her 
# year of service is more than 5years. Ask user for their salary and year 
# of service and print the net bonus amount.
salary=float(input('Enter your salary: '))
years_of_service=int(input('Enter your years of service: '))
if years_of_service > 5:
    print(f'Congratulations! You have received a bonus of Rs. {0.05*salary:.2f}.')
else:
    print(f'Your salary is ${salary}and you didnot receive any bonus')

# 13. Write a python program which accepts the radius of circle from 
# user and compute the area. 
import math
radius=float(input('Enter the radius of the circle: '))
area=math.pi*(radius**2)
print(f"The area of circle with radius {radius} is: {area:.2f}")

# 14. Accept the age, gender ('M', 'F'), number of days and display the 
# Wages accordingly.
user_age=int(input('Enter your age: '))
user_gender=input('Enter your gender:  male or female').lower()
number_of_days=int(input('Enter number of days: '))
if user_gender not in ['male', 'female']:
    print("Invalid input for gender. Please enter 'male' or 'female'.")
elif user_age < 18:
    print("You are underage. You cannot work.")
elif user_age >= 18 and user_age <= 30:
    if user_gender == 'male':
       print(f'You are {user_age} years old {user_gender} So Your wages is Rs. 700 per day.')
    elif user_gender == 'female':
        print(f'You are {user_age} years old {user_gender} So Your wages is Rs. 750 per day.')
elif user_age >= 30 and user_age <= 40:
    if user_gender == 'male':
       print(f'You are {user_age} years old {user_gender} So Your wages is Rs. 800 per day.')
    elif user_gender == 'female':
        print(f'You are {user_age}  years old {user_gender} So Your wages is Rs. 850 per day.')
else:
    print("You are above 40 years old. You cannot work.")



# 15. Accept input from user 
# If given number is a multiple of both 3 and 5 prints Fizz Buzz instead 
# of number 
# If  given  number  is  a  multiple  of  3  but  not  5  prints  Fizz  instead  of 
# number 
# If  given  number  is  a  multiple  of  5  but  not  3  prints  Buzz  instead  of 
# number 
# If given number is not multiple of 3 or 5 prints value as usual. 
user_number=(input('Enter a number: '))
if not user_number.isdigit():
    print("Invalid input. Please enter a valid number.")
elif user_number % 3 == 0 and user_number % 5 == 0:
    print("Fizz Buzz")
elif user_number % 3 == 0 and user_number % 5 != 0:
    print("Fizz")
elif user_number % 5 == 0 and user_number % 3 != 0:
    print("Buzz")
else:
    print(user_number)
 
# 16. A  utility  company  charges  different  rates  based  on  electricity 
# usage: If usage < 100 units then cost Rs 5 per unit 
# If usage is between 100 to 300 units:  First 100 units: Rs 5 Next units: Rs 8 
# If usage is > 300 units: First 100: Rs 5 Next 200: Rs 8 Remaining: Rs  10 
electricity_usage=input('Enter your electricity usage in units: ')
if not electricity_usage.isdigit():
    print("Invalid input. Please enter a valid number.")
else:
    electricity_usage=int(electricity_usage)
    if electricity_usage < 100:
        cost = electricity_usage * 5
    elif electricity_usage <= 300:
        cost = 100 * 5 + (electricity_usage - 100) * 8
    else:
        cost = 100 * 5 + 200 * 8 + (electricity_usage - 300) * 10
    print(f"Your electricity bill is Rs. {cost}")

# 17. Write a complete Python program that: 
#   Asks  Player  1  to  enter  their  move  (  input:  rock,  paper,  or  scissors) 
#   Asks  Player  2  to  enter  their  move  (  input:  rock,  paper,  or  scissors)   Prints who wins or
# print who wins or if it's a tie 
print("Welcome to Rock, Paper, Scissors Game!")
player1_move = input("Player 1, enter your move (rock, paper, or scissors): ").lower()
player2_move = input("Player 2, enter your move (rock, paper, or scissors): ").lower()
valid_moves = ['rock', 'paper', 'scissors']
if player1_move not in valid_moves or player2_move not in valid_moves:
    print("Invalid move. Please enter rock, paper, or scissors.")
elif player1_move == player2_move:
    print("It's a tie!")
else:
    if (player1_move == 'rock' and player2_move == 'scissors') or (player1_move == 'paper' and player2_move == 'rock') or (player1_move == 'scissors' and player2_move == 'paper'):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
 
# 18. Write  a  Python  program  that  takes  a  number  as  input,  first 
# checks if it is positive if yes then check whether it is even or odd. 
users_number=input('Enter a number: ')
if not users_number.lstrip('-').isdigit():
    print("Invalid input. Please enter a valid number.")
else:
    users_number=int(users_number)
    if users_number > 0:
        if users_number % 2 == 0:
            print(f"{users_number} is a positive even number.")
        else:
            print(f"{users_number} is a positive odd number.")
    else:
        print(f"{users_number} is not a positive number.")

# 19. A  store  gives  a  20%  discount  if  the  total  purchase  is  above  RS 
# 1000  AND  the  customer  is  a  member,  or  a  10%  discount  if  the 
# purchase is above RS 1000 but the customer is not a member. Write a 
# program that takes total_amount and is_member (True/False) as 
# input and prints the final amount after applying the correct discount 
# or no discount.
total_amount=float(input('Enter total purchase amount: '))
is_member_input=input('Are you a member? Enter True or False: ').lower()
if is_member_input not in ['true', 'false']:
    print("Invalid input for membership status. Please enter True or False.")
else:
    is_member = is_member_input == 'true'
    if total_amount > 1000:
        if is_member:
            discount = total_amount * 0.20
            final_amount = total_amount - discount
            print(f"Congratulations! You have received a 20% discount. Final amount: Rs. {final_amount:.2f}")
        else:
            discount = total_amount * 0.10
            final_amount = total_amount - discount
            print(f"You have received a 10% discount. Final amount: Rs. {final_amount:.2f}")
    else:
        print(f"No discount applied. Final amount: Rs. {total_amount:.2f}")

# 20. Create a weight conversion program that: 
# Asks the user what their Earth weight is as a float. Asks  the user for a planet number as an int. 
# Then, use an if/elif/else statement to calculate the user's weight on the destination planet. 
# To  calculate the  user's  weight:  destination  weight=Earth weight × relative gravity. 
# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'
earth_weight=float(input('Enter your Earth weight in kg: '))
planet_number=int(input('Enter a planet number (1-7): '))
relative_gravity = {1: 0.38, 2: 0.91, 3: 0.38, 4: 2.53, 5: 1.07, 6: 0.89, 7: 1.14}

if planet_number in relative_gravity:
    destination_weight = earth_weight * relative_gravity[planet_number]
    print(f"Your weight on planet {planet_number} would be {destination_weight:.2f} kg.")
else:
    print("Invalid planet number. Please enter a number between 1 and 7.")


# 21. WAP  which  accepts  marks  of  four  subjects  and  display  total 
# marks, percentage and grade. Hint: more than 70 –> distinction, more 
# than 60 –> first, more than 40 –> pass, less than 40 –> fail 
marks = []
for i in range(1, 5):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 400) * 100
if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")


# 22. Write  a  Python  program  to  simulate  a  simple  ATM  with  the 
# following specifications:    Assume the card is valid (is_valid = True) 
#   Initial account balance is RS 5000 
#   Correct PIN is 123 
#   After entering correct PIN, display the menu: 
# 1. Withdraw 
# 2. Check Balance 
# 3. Exit 
#   If user selects 1 then ask amount and deduct from balance 
#   If user selects 2 then show current balance 
#   If  user  selects  3  then  print  Thank  you  for  visiting 
# Show proper messages for wrong PIN and invalid option 
pin=input('Enter your pin')
if not pin.isdigit():
    print("Invalid input. Please enter a valid PIN.")
elif pin == "123":
    print("Correct PIN. Please select an option:")
    print("Enter 1. Withdraw")
    print("Enter 2. Check Balance")
    print("Enter 3. Exit")
    option=input('Enter your option: ')
    if option == "1":
        amount=float(input('Enter amount to withdraw: '))
        if amount > 5000:
            print("Insufficient balance.")
        else:
            balance = 5000 - amount
            print(f"Withdrawal successful. Your new balance is Rs. {balance:.2f}.")
    elif option == "2":
        print("Your current balance is Rs. 5000.")
    elif option == "3":
        print("Thank you for visiting.")
    else:
        print('You must enter 1, 2 or 3')
else:
    print("Incorrect PIN. Please try again.")


# 23. Write a program that simulates the elevator's internal logic. The 
# program should accept user inputs for the desired floor, the current weight 
# load, and the door status, then determine if the elevator is cleared to move. 
# Requirements 
# Target Floor: An integer representing the user's selection. 
# Total Weight: A numerical value (in kg) representing the current load inside the lift. 
# Door  Status:  A  Boolean  or  string  indicating  whether  the  door  is  closed  or  open. 
# Logic Constraints  
# Floor Validation 
#  The elevator only services floors in the range of 0 to 10. 
#  If the input is outside this range, the system must display 
# INVALID FLOOR and terminate the process. 
# Weight Limit Sensor 
#  The safety limit for this lift is 500kg. 
#  If the total weight is greater than 500kg, the system must 
# display OVERWEIGHT: LIFT CANNOT MOVE and terminate.  Door Mechanism Status 
#  The lift cannot move unless the door is fully engaged/closed. 
#  If  the  door  is  open,  display  WARNING: CLOSE  THE  DOOR  and terminate. 
# If all three conditions are met, the program should output: ACTIVATE  ELEVATOR MOTION. 
floor=input('Enter your desired floor(0-10): ')
if not floor.isdigit():
    print("Invalid input. Please enter a valid floor number.")
elif int(floor) < 0 or int(floor) > 10:
    print("INVALID FLOOR")
else:
    weight=input('Enter the current weight load in kg: ')
    if not weight.replace('.', '', 1).isdigit() or float(weight) < 0:
        print("Invalid input. Please enter a valid weight.")
    elif float(weight) > 500:
        print("OVERWEIGHT: LIFT CANNOT MOVE")
    else:
        door_status=input('Is the door closed? Enter yes or no: ').lower()
        if door_status == 'yes':
            print("ACTIVATE ELEVATOR MOTION")
        elif door_status == 'no':
            print("WARNING: CLOSE THE DOOR")
        else:
            print("Invalid input for door status. Please enter yes or no.")

# WAP to validate the input for a facebook sign up form. The program should ask for first name, last name, email, re-email 
# and password. Then it should validate the input based on the following requirements and print appropriate messages for 
# each validation failure.
# Requirements for facebook sign up form
# First name: not empty + letters only 
# Last name: not empty + letters only 
# Email: contains @ and . 
# Re-email: matches first email 
# Password: minimum 6 characters 
first_name=input('Enter your first name: ')
last_name=input('Enter your last name: ')
email=input('Enter your email: ')
re_email=input('Re-enter your email: ')
password=input('Enter your password: ')

if (not first_name.isalpha() and not last_name.isalpha()) or (not first_name==' ' and not last_name==' '):
    print("Invalid first/last name. First and last name must contain letters only and cannot be empty.")
elif '@' not in email or '.' not in email:
    print("Invalid email. Email must contain '@' and '.'.")
elif email != re_email:
    print("Email mismatch. Re-entered email does not match the first email.")
elif len(password) < 6:
    print("Invalid password. Password must be at least 6 characters long.")
else:
    print("Sign up successful! Welcome to Facebook.")