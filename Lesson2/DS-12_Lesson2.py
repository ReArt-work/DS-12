# -*- coding: utf-8 -*-

# -- Sheet --

login = input("Enter your login")

if login == "login":
    pswrd = input("Enter your password")
    if pswrd == "password":
        print("Welcome")
    else:
        print("Passwornd is wrong")
else:
    print("Login is wrong")


