# Methods upper(), lower(), title(), capitalize(), swapcase()
# 1. A hospital system stores patient names in random case for example
# rahUl DahaL. Write a program to display the name in proper title format
# on the prescription.
name=input('Enter Your Name').title()
print(name)
# 2. A cybersecurity system requires all passwords to be checked in
# lowercase for consistency. Take a password input like ‘Pass@123’ and
# convert it for comparison.
password=input('Enter your Password ')
if password == password.lower() and '@' in password and len(password) >=8:
    print("Password is valid")
else:
    print('Password must be in lower case and contain atleast 1 special character and must be greater than 8 character')

# 3. A movie ticket booking system receives the movie name in lowercase
# ‘spider-man no way home’. Display it in title case on the ticket.
moviename='spider-man no way home'.title()
print(moviename)

# 4. A school notice board program takes a heading input and displays it in
# ALL CAPS for attention. Take input ‘annual sports day’ and display it.
heading=input('Enter annual sports ').capitalize()
print(heading)

# 5. A fun CAPS-LOCK reversal tool takes the sentence ‘hELLO wORLD’ and
# swaps every letter's case. Write a program for this.
sentence = 'hELLO wORLD'
print(sentence.swapcase())

# Methods find(), index(), count(), startswith(), endswith()
# 6. A document editor wants to find the first position where the word ‘error’
# appears in a log message: ‘System error detected, error code 404’.
log = 'System error detected, error code 404'
position = log.find('error')
print(position)

# 7. An email validation system checks whether an entered email ends with
# ‘@gmail.com’. Write a program to validate it.
email='example@gmail.com'
if email.endswith('@gmail.com'):
    print('email is valid')
else:
    print('Email is invalid .It must end with @gmail.com')
# 8. A spam filter counts how many times the word ‘free’ appears in a
# message: ‘Get free stuff, free gifts and free coupons now!’.
spam='Get free stuff, free gifts and free coupons now!'
print(spam.count('free'))

# 9. A URL checker verifies whether a website link starts with "https" for
# security. Write a program for this.
url='https://example.com'
if url.startswith('https'):
    print('The url is valid and secured')

# 10. A resume scanner checks whether the keyword ‘Python’ is present in
# a resume text. Use the in operator.
resume = 'Experienced developer with skills in Python, Java, and SQL.'
if 'Python' in resume:
    print('Python is present in the resume')
else:
    print('Python is not present in the resume')

# 11. A bank transaction log uses index() to find the exact position of the
# word ‘FAILED’ in the message ‘Transaction FAILED due to low balance’.
message = 'Transaction FAILED due to low balance'
position = message.index('FAILED')
print(position)

# 12. A government office receives a file named ‘budget_report.pdf’. Write a
# Python program that checks whether the file is a PDF document or not
# using endswith() and directly print the result.
filename = 'budget_report.pdf'
print(filename.endswith('.pdf'))


# 13. A telecom registration system receives a phone number ‘+977-
# 9841123111’. Write a Python program that checks whether the phone
# number starts with the Nepal country code ‘+977’. Print the result
# directly.
phone = '+977-9841123111'
print(phone.startswith('+977'))

# 14. A cybersecurity system receives a url ‘https://www.moha.gov.np/’.
# Write a Python program that checks whether the URL belongs to a
# government website, print the result directly.
url = 'https://www.moha.gov.np/'
print('.gov.np' in url)

# Methods replace(), strip(), lstrip(), rstrip()
# 15. A customer feedback form receives input with extra spaces: ‘ Great
# service! ‘. Clean it before saving to the database.
feedback=' Great service! '
print(feedback.strip())
# 16. A chat application replaces all occurrences of a banned word ‘hate’
# with ‘****’ in the message "I hate this, hate it completely".
chat="I hate this, hate it completely"
print(chat.replace('hate','****'))

# 17. A file system receives filenames with leading slashes like
# ‘///student_records.pdf ‘. Remove the leading slashes.
filename = '///student_records.pdf '
print(filename.lstrip('/'))

# 18. A web scraper fetches product prices as ‘Price: $120.33 ‘ with trailing
# spaces. Clean the right side using rstrip() and remove symbols too.
price = 'Price: $120.33 '
clean_price = price.rstrip('Price: ')
print(clean_price)

# 19. A phone number formatter takes ‘+977 984-123-4567’ and removes
# all dashes - using replace() to store only digits format.
phone = '+977 984-123-4567'
formatted_phone = phone.replace('-', '').replace(' ', '').replace('+', '')
print(formatted_phone)

# Methods split(), join()
# 20. A CSV file contains student data as ‘Aarav,22,Kathmandu,Computer
# Science’. Split it into individual fields and display each on a new line.
data='Aarav,22,Kathmandu,Computer Science'
newdata=data.split(',')
for field in newdata:
    print(field)
# 21. A social media app stores hashtags as a ‘Python, Coding, Nepal, Tech’.
# Join them with # prefix to display as #Python #Coding #Nepal #Tech.
media='Python, Coding, Nepal, Tech'
hashtags = media.split(', ')
result = '#' + ' #'.join(hashtags)
print(result)

# 22. A train ticket system receives passenger names separated by commas:
# 'Ram, Shyam, Hari, Sita'. Split and count the total number of passengers.
passengers = 'Ram, Shyam, Hari, Sita'
passenger_list = passengers.split(', ')
print(f'Total passengers: {len(passenger_list)}')

# 23. A sentence builder takes individual words ['The', 'flight', 'departs', 'at',
# '6AM'] and joins them with a space to form a proper sentence.
words = ['The', 'flight', 'departs', 'at', '6AM']
sentence = ' '.join(words)
print(sentence)

# Methods isdigit(), isalpha(), isalnum(), isspace(), isupper(), islower()
# 24. A government form validation checks whether the entered age
# contains only digits. Take input ‘25’ or ‘25abc’ and validate it.
age=input('Enter your Age');
print(age.isdigit())

# 25. A username registration system checks that the username contains
# only letters and numbers, no special characters.
user='ankit123'
print(user.isalnum())

# 26. A name field validator in a school admission form checks that the
# student's name contains only alphabets (no digits).
student='ankit'
print(student.isalpha())

# 27. A PIN verification system checks whether the user's PIN is all
# uppercase letters for a code like ‘ASDF’.
PIN='ASDF'
print(PIN.isupper())

# 28. A blank field detector in a form checks whether the user entered only
# spaces.
space='   '
print(space.isspace())