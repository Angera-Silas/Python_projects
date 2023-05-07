#importing important libraries
import csv
from IPython.display import clear_output
#creating a user registration section
def registerUser():
    with open("studentMgt.csv",mode="a",newline="") as s:
        writer = csv.writer(s,delimiter=",")
        email = input("Enter your email address")
        email1 = input("confirm Email")
        password = input("Enter a password")
        password2 = input("Confirm password")
        clear_output()
        if email1==email and password2==password:
            writer.writerow([email,password])
            print("Account successfully created")
            logged_in=True
        else:
            print("Try again your passwords do not match")
            
#creating a user login handler
def userLogin():
    trials = 0
    print("Input your credentials to login")
    email = input("Enter your email address")
    password = input("Enter your password")
    clear_output()
    with open("studentMgt.csv",mode="r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if row == [email,password]:
                print("Successfully Logged in")
                return True
    print("Wrong password or email Address...please try again")
    return False

#creating the get password
def getPassword():
    email = input("Enter your Email address")
    email1 = input("Confirm your Email address")
    clear_output()
    with open("studentMgt.csv",mode="r") as s:
        reader=csv.reader(s,delimiter=",")
        for row in reader:
            if email in row:
                print("Dear customer the Email address and password are displayed below")
                print(row)
                print("Login to change your password")
            else:
                print("Error--> Email address not found")

#reseting password
def resetPassword():
    confirm=input(" You are about to Reset your password type in one command\n1. ok\n2. cancel").lower()
    if confirm=="cancel":
        logged_in = True
    elif confirm=="ok":
        email = input("Enter your email address")
        password = input("Enter your password")
        clear_output()
        with open("studentMgt.csv",mode="r") as f:
            reader = csv.reader(f,delimiter=",")
            for row in reader:
                if row == [email,password]:
                    with open("studentMgt.csv",mode="w",newline="") as f:
                        writer=csv.writer(f,delimiter=",")
                        password = input("Enter new password")
                        password1 = input("confirm your new password")
                        if password == password1:
                            writer.writerow([email,password])
                            print("Successfully recovered your password,login to verify")
                            logged_in=True
                        else:
                            print("Kindly recheck your credentials")

#creating the main loop
active = True
logged_in = False

while active:
    if logged_in:
        print("1. Logout \n2. Change-password \n3. Quit")
    else:
        print("1. login \n2. register \n3. Forgot-password \n4. Quit")
    option=input("What do you wish to do? ").lower()
    clear_output()
    if option == "register" and logged_in == False:#if the user is not logged in and chooses to register
        registerUser()#the user will be redirected to registration page by the function
    elif option == "login" and logged_in == False:
        logged_in = userLogin()#if the user already registered and wants to login in 
    elif option == "quit":
        active = False#if the user chooses to quit then the program is terminated
        print("Thank you for using My Software!\nCode provided by Angera Silas")
    elif option =="change-password":
        resetPassword()
    elif option =="forgot-password":
        getPassword()
    elif option == "logout" and logged_in == True:
        logged_in = False
        print("Successfully logged out\nThank you for using My Software!\nCode provided by Angera Silas")
    else:
        print("Sorry,please try again")
        