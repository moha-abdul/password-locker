#! /usr/bin/env python3.6

from user import User
import string
import random

def create_account(first_name,last_name, username, password): #create user
	new_user = User(first_name, last_name, username, password)
	return new_user
def create_user(fname,lname,phone,email): #create user
	new_user = User(fname,lname,phone,email)
	return new_user

def save_users(user):
	user.save_user()

def del_users(user):
	user.delete_user()

def find_user(user):
	return User.find_user_by_username(user) 

def check_existing_users(user):
	return User.user_exists(user)

def display_users():
	return User.display_users()

def main():
	print("What username do you want?")

	while True

    print("Hello Welcome to the applocker. What do you want to do? Use these short codes : cu - create a new user \n dc - display users \n fu -find a user \n ex -exit the app \n A. Register account \n B. Log in to account \n C. Check if user exists \n D. Find user by username \n")
    username = input()

if __name__ == '__main__':
    main()