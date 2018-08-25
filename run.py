#! /usr/bin/env python3.6

from user import User
import string
import random

def create_user(first_name,last_name, username, password): #create user
	new_user = User(first_name, last_name, username)
	return new_user

def save_users(user):
	user.save_user()

def del_users(user):
	user.delete_user()

def find_user(user):
	return User.find_user_by_account(user) 

def check_existing_account(user):
	return User.user_exists(user)

def display_users():
	return User.display_account()

def main():
	print("What username do you want?")

	while True:
		print("Hello Welcome to the applocker. What do you want to do? Use these short codes : \n cu - create a new user \n dc - display all users \n fu -find a user \n ex -exit the app \n ch - check if user exists \n fd - find user by username \n")
		first_name = input()
		last_name = input()
		username = input()

if __name__ == '__main__':
    main()