'''
This code verifies if the user can login in 10 attempts. 
The username and password should match what is in "cl" and "cp". 
#1 - stdiomask module is used to hide input password
#2 - re module is used to match specific password requirement
'''

import stdiomask
import re

# Initial inputs 
cl = 'ayaz'  # this is random user name is given, you can change it to whatever you want
cp = 'Poland2019!'  # this is random password, make sure criteria is matching
i = 1
success = False

# Initial inputs - End

# Login logic
def find_login(inp, login, count):
    if inp != login:
        print(f'Wrong login. {10 - count} attempts left!')
        return False
    else:
        print(f'Login Found. Pass verification starts')
        return True

# Password logic
def find_password(inp, password, count):
    if inp != password:
        print(f'Wrong Password. {10 - count} attempts left!')
        return False
    else:
        return True

# Verification starts
while i <= 10:
    login = input('Login: ')
    # Login logic starts
    if find_login(login, cl, i):
        print('Check pass')

        # Password logic starts
        #i = i +1
        while i <= 10:
            password = input('Password: ')
            if find_password(password, cp, i):
                print(f'SUCCESS!')
                # User logged in. You can put the rest logic as per your requirements
                success = True
                break
            i += 1
    if success: break
    i += 1
