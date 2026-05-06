
# Create an signup form . First and lastname must be in alphabet and cannot . Email must contain @ and . . Force user to enter email again . Password msut be greater than 8 character.

first_name=input('Enter Your first name')
last_name=input('Enter Your first name')
form_email=input('Enter your email')
remail=input('Enter email again')
form_password = input('Enter your password')
if not first_name.isalpha() and first_name == '':
    print('You must enter your name in alphabet')
elif not last_name.isalpha() and not last_name != '':
    print('You must enter your name in alphabet')
elif not '@' in form_email and not '.' in form_email:
    print('Invalid email')
elif not remail== form_email:
    print('Email must match with email')
elif len(form_password) < 8:
    print('Pass word must be atleast 8 character')
else:
    print(f'Welcome ${first_name} ${last_name} . Your email is ${form_email}')

# Q1. A theme park has these rules. You can ride the roller coaster if you are at least 12 years old AND at least 140 cm tall.
#  Write the if-else code for this
age=int(input("Enter your age: "))
height=int(input("Enter your height in cm: "))
if age >= 12 and height >= 140:
    print("You can ride the roller coaster.")
else:
    print("You do not meet the requirements.")


# Q2. Design a Traffic Light System. Given a variable light that can be "red", "yellow", or "green", print the correct 
# instruction. Also handle an invalid color with an error message
light = "green"  # Example input

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Slow down")
elif light == "green":
    print("Go")
else:
    print("Error: Invalid color")

# Q3. Write a match statement that takes a number 1-4 and prints the corresponding season: 1=spring, 2=summer, 3-autumn, 
# 4-winter. Default "unknown"
month_num = 2  # Example input

match month_num:
    case 1: print("spring")
    case 2: print("summer")
    case 3: print("autumn")
    case 4: print("winter")
    case _: print("unknown")

# Q4 Write a login system using nested if Check
# If username equals "admin"
# Inside that, if password equals "pass123"
# Print appropriate messages for valid login, wrong password, wrong username
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "pass123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# Q5 Design a Bank Loan Approval System. Approve a loan only if ALL three conditions are met
# Age is between 21 and 60 (inclusive)
# Monthly income is at least 30,000
# Credit score is at least 700
# If not approved, print which condition failed. If multiple fail, pick the most important one to report
income = float(input("Enter your monthly income: "))
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))
if not (21 <= age <= 60):
    print("Loan Denied: Age must be between 21 and 60.")
elif income < 30000:
    print("Loan Denied: Monthly income too low.")
elif credit_score < 700:
    print("Loan Denied: Credit score too low.")
else:
    print("Loan Approved!")

# Q6. You are developing a simple ticket booking system for a movie theatre. The ticket price depends on the age of the person 
# and whether they have a membership card. If the person is under 12 the ticket is free. If the person is between 12 and 60: 
# If they have a membership card, the ticket costs $150. If they do not have a membership card, the ticket costs $200. 
# If the person is over 60, the ticket costs $100 regardless of membership as senior citizenship discount. Write the nested if-else 
# code to determine the ticket price based on user input for age and membership status.
age = int(input("Enter your age: "))
has_membership = input("Do you have a membership? (yes/no): ").lower()
if age < 12:
    price = 0
elif 12 <= age <= 60:
    if has_membership:
        price = 150  # Example discounted price
    else:
        price = 200  # Example standard price
else:
    price = 100  # Example senior price
print(f"The ticket price is ${price}.")


# Q7 A company decided to give 5 % bonus to employees if his/her service is more than 5 years of service. 
# Ask user for years of service and salary. If the employee is eligible for bonus, calculate the net bonus amount.
years_of_service = int(input("Enter years of service: "))
salary = float(input("Enter your salary: "))
if years_of_service > 5:
    bonus = salary * 0.05
    print(f"You are eligible for a bonus of ${bonus:.2f}.")


# Q8 Write a python program which accespts radius of circle from user and compute the area.
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {area:.2f}")

# Q9. 9. Accept the age, gender ('M', 'F'), number of days and display the wages accordingly.
# Age              Gender   Wage/day
# >=18 and <30       M        700
#                    F        750
# >=30 and <=40      M        800 
#                    F        850

age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
if 18 <= age < 30:
    if gender == 'M':
        wage = 700
    elif gender == 'F':
        wage = 750  
elif 30 <= age <= 40:
    if gender == 'M':
        wage = 800
    elif gender == 'F':
        wage = 850
print(f"Your wage per day is: ${wage}.")

# Q10. 10. Accept input from user
# If given number is a multiple of both 3 and 5 prints "Fizz Buzz" instead of number
# If given number is a multiple of 3 but not 5 prints "Fizz" instead of number
# If given number is a multiple of 5 but not 3 prints "Buzz" instead of number
# If given number is not multiple of 3 or 5 prints value as usual."
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# Q11 Write an python program to create rock paper and scissor game.
p1=input('Enter Your turn . Rock , Paper and Scissor for r ,p , s respectively').lower()
p2=input('Enter Your turn . Rock , Paper and Scissor for r ,p , s respectively').lower()
if (p1 == 'r' and p2 == 's') | (p1 == 'p' and p2 == 'r') | (p1 == 's' and p2 == 'p'):
    print('Player 1 wins the game') 
elif (p1 == 'r' and p2 == 'p') |(p1 == 'p' and p2 == 's') | (p1 == 's' and p2 == 'r'):
    print('player 2 wins the game')
else:
    print('Invalid input :You must type r,s or p')