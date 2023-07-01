# This program will be used to validate that a user inputs at least two names when asked to enter their full name
full_name = input("Enter your Name and Surname:")
print(full_name)

full_name == 0
if len(full_name) == 0:
    print("You haven’t entered anything")
else:  
   print("thank you for entering your name")

if  len(full_name) < 4:
    print("You have entered less than 4 characters."" Please make sure that you have entered your name + surname.")
    
if len(full_name) > 25:
    print("You have entered more than 25 characters."" Please make sure that you have only entered your full name")

