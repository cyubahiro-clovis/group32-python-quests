#!/usr/bin/python3

# A password checker 

print()
print("=" * 10)
print("This is a password checker !")
print("=" * 10)
print()


password = input('Enter the password: ')
correct_password = 'Password'

if correct_password == password:
    print("Access Granted")
else:
    print("Access Denied")

