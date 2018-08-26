#! /usr/bin/env python3.6

from user import User
from profile import Profile
import string
import random

def create_user(first_name,last_name, username, password): #create user
	new_user = User(first_name, last_name, username)
	return new_user

def save_users(user):
	user.save_user()

def del_users(user):
	user.delete_user()

def create_profile(account, password): #create profile
	new_user = Profile(account, password)
	return new_profile

def del_profile(profile):
	user.delete_profile()

def find_profile(user):
	return Profile.find_profile_by_account(account) 

def check_existing_username(user):
	return User.user_exists(user)

def display_users():
	return User.display_users()
short_code = input().lower()
def main():
	print("What would you like to do? \n")
	print("cu - create new user \n ex - exit the app \n")
	short_code = input().lower()
	print("\n")
	if short_code == "cu":
		print("enter first name")
		first_name = input()
		print("\n")
		print("enter last name")
		last_name = input()
		print("\n")
		print("enter username")
		username = input()

	else short_code == "ex":
		print("Bye ...")
        break

	

	# while True:
		# print(f"Hello {username} Welcome to the applocker. What do you want to do? Use these short codes : \n cu - create a new profile \n dp - display all your profiles \n fp -find a profile by account \ncheck if user profile exists \n ex -exit the app \n")

if __name__ == '__main__':
    main()