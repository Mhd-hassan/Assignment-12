# Name: Muhammad Hassan Noorsumar
# Day: Tuesday
# Date: 18/07/2023
# Sub: Python
# Topic: Assignment-12
# Assignment-12: Q4
# Q4: It should be a proper project, such as a management system or a login page (if it is a login page then it should navigate to that particular site)

def authenticate_user(username,password):
    if username == "admin" and password == "password": # perform authentication logic here
        return True
    else:
        return False
    
"""
1. Output of entire code:
=== Login Page ===
Username Hassan
Password 123
Invalid username or password. Please try again.
"""

"""
2. Output of entire code:
=== Login Page ===
Username: admin
Password: password
Login successful !
"""