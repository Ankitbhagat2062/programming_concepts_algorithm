#  1. Write a program to check whether the given number is in between 1 and 100 or not.
number=50
if number>1 and number<100:
    print("The number is between 1 and 100.")
else:
    print("The number is not between 1 and 100.")


#      2. Check whether the user input number is even or odd and 
#       display it to user.
user_input = int(input("Enter a number: "))
if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#     3. Write a program that asks the user for a number 
#           in the range of 1 to 12. 
#        The program should display the corresponding month, where 
#        1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 
#        8=august,9=september,10=october,11=november,12=december. The program should display an error 
#        message if the user enters a number that is outside the range of 1 to 12.
user_number = int(input("Enter a number between 1 and 12: "))
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
print(f'Your month is {months.get(user_number, "Error: Number is outside the range of 1 to 12.")}')



#        4. A school has following rules for grading system:
#         a. Below 25 - F
#         b. 25 to 45 - E
#         c. 45 to 50 - D
#         d. 50 to 60 - C
#         e. 60 to 80 - B
#         f. Above 80 - A
#         Ask user to enter marks and print the corresponding grade.
user_marks = int(input("Enter your marks: "))
if user_marks < 25:
    print("Grade: F")
elif 25 <= user_marks < 45:
    print("Grade: E")
elif 45 <= user_marks < 50:
    print("Grade: D")
elif 50 <= user_marks < 60:
    print("Grade: C")
elif 60 <= user_marks < 80:
    print("Grade: B")
else:
    print("Grade: A")


#         5. Write a program to check whether a number is divisible by 
#         7 or not.
number_to_check = int(input("Enter a number: "))
if number_to_check % 7 == 0:
    print(f"{number_to_check} is divisible by 7.")
else:
    print(f"{number_to_check} is not divisible by 7.")



#         6. Write a program to accept two numbers and mathematical operators and 
#         perform operation accordingly.
#             Like:
#             Enter First Number: 7
#             Enter Second Number : 9
#             Enter operator : +
#             Your Answer is : 16
first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number

print(f"Your Answer is : {result}")


#          7. Write a Python program to check car loan eligibility:
#             Salary >= 50,000 and Credit Score >= 700: "Eligible"
#             Otherwise: "Not Eligible"
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if salary >= 50000 and credit_score >= 700:
    print("Eligible for car loan.")
else:
    print("Not eligible for car loan.")

#         8. Write a Python program that takes an integer input n n. 
#         From given number, 
#         check if it is divisible by both 3 and 5, and print "FizzBuzz" 
#         if true. 
#         If the number is divisible only by 5, print "Buzz." If it is 
#         divisible only by 3, print "Fizz." 
#         Finally, if the number is not divisible by either 3 or 5, 
#         print the number itself.
num1 = int(input("Enter an integer: "))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("FizzBuzz")
elif num1 % 5 == 0:
    print("Buzz")
elif num1 % 3 == 0:
    print("Fizz")
else:
    print(num1)


# 9. Write a Python program that takes a character input and 
# checks whether it is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")    
else:
    print(f"{char} is a consonant.")


# 10. Write a Python program to input marks and determine the grade based on the following conditions:
# 90-100: A
# 80-89: B
# 70-79: C
# Below 70: Fail
marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:  
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
else:
    print("Fail")



# 11. Write a Python program to categorize a person’s age:
# Age < 13: Child
# 13 <= Age <= 19: Teenager
# Age > 19: Adult
age = int(input("Enter your age: "))
if age < 13:
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")


# 12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.
given_char=input("Enter a character: ")
if given_char.isupper():
    print(f"{given_char} is an uppercase letter.")
elif given_char.islower():
    print(f"{given_char} is a lowercase letter.")
elif given_char.isdigit():
    print(f"{given_char} is a digit.")



# 13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and 
# outputs the corresponding action ("Stop", "Get Ready", "Go").
color=input("Enter a traffic light color (Red, Yellow, Green): ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")


# 14. Write a Python program to check eligibility for a job based on age and experience:
# Age > 18 and Experience >= 2 years: Eligible
# Otherwise: Not Eligible
your_age = int(input("Enter your age: "))
your_experience = int(input("Enter your years of experience: "))
if your_age > 18 and your_experience >= 2:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")



# 15. Write a Python program to give advice based on the temperature:
# Temperature > 30°C: "It's hot, stay hydrated!"
# Temperature between 15-30°C: "Enjoy the weather!"
# Temperature < 15°C: "It's cold, wear warm clothes!"
temperature = float(input("Enter the temperature in °C: "))
if temperature > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temperature <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")



# 16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
# Pizza: $10
# Burger: $7
# Pasta: $8

menu_option = input("Enter a menu option (Pizza, Burger, Pasta): ").lower()
if menu_option == "pizza":
    print("Price: $10")
elif menu_option == "burger":
    print("Price: $7")
elif menu_option == "pasta":
    print("Price: $8")
else:
    print("Invalid menu option.")


# 17. Write a Python program to select players based on height:
# Height >= 6 feet: Selected
# Height < 6 feet: Not Selected
height = float(input("Enter your height in feet: "))
if height >= 6:
    print("You are selected.")
else:
    print("You are not selected.")



# 18. Write a Python program to check if a person is eligible to watch a movie based on their age:
# Age >= 18: Allowed
# Age < 18: Not Allowed
age_crit = int(input("Enter your age: "))
if age_crit >= 18:
    print("You are allowed to watch the movie.")
else:
    print("You are not allowed to watch the movie.")


# 19. Write a Python program to check login credentials:
# Username: "admin", Password: "password123"
# If correct, print "Access Granted"; otherwise, print "Access Denied."
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")


# 20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:
# 12, 1, 2: "Winter"
# 3, 4, 5: "Spring"
# 6, 7, 8: "Summer"
# 9, 10, 11: "Autumn"

month = int(input("Enter a month number (1-12): "))
if month in [12, 1, 2]:
    print("Season: Winter")
elif month in [3, 4, 5]:
    print("Season: Spring")
elif month in [6, 7, 8]:
    print("Season: Summer")
elif month in [9, 10, 11]:
    print("Season: Autumn")
else:
    print("Invalid month number.")
