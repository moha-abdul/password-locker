#! /usr/bin/env python3.6

from user import User
from profile import Profile
import string
import random

def create_user(first_name,last_name, username): #create user
	new_user = User(first_name, last_name, username)
	return new_user

def create_profile(account, password): #create profile
	new_profile = Profile(account, password, pass_length)
	return new_profile

def save_users(user):
	user.save_user()

def save_profile(profile):
	profile.save_profile()

def del_users(user):
	user.delete_user()

def del_profile(profile):
	profile.delete_profile()

def find_profile(profile):
	return Profile.find_profile_by_account(profile) 

# def check_existing_username(user):
# 	return User.user_exists(user)

# def display_users():
# 	return User.display_users()

def password_generate(pass_length):
    return Profile.password_generate(pass_length)

short_code = input().lower()

def main():
	
	print("Welcome to my new app Pasword Locker \n")
	print("create user account to continue")
	# print("cu - create new user \n du - delete user \n ex - exit the app \n")

	short_code = input().lower()
	print("\n")
	
	print("What is your first name")
	first_name = input()
	print("\n")
	print("What is your last name")
	last_name = input()
	print("\n")
	print("Create a username")
	username = input()

	print(f"Hello {first_name} {last_name}. You are logged in as {username} \n")
	print(f"What would you like to do {username}? Use the short codes. cp - create profile \n dp - delete profile \n fp - find profile \n ap - see all profiles ")

	if short_code == "cp":
		password = input().lower()
		print("Enter account name to create profile like twitter -")
        # account = input()
		print ("Do you want to \n g - generate from system\n s - set own password")
		password = input().lower()
		if password == "g":
			pass_length = int(input("How many characters do you want your password to be?"))
			password = password_generate(pass_length)
			print(f"Your new password is {password}")
		else:
			print("Write a password of your own")
			password = input()

		  
	# else short_code == "du":

	# 	print("Bye ...")
    #     break

	

	# while True:
		# print(f"Hello {username} Welcome to the applocker. What do you want to do? Use these short codes : \n cu - create a new profile \n dp - display all your profiles \n fp -find a profile by account \ncheck if user profile exists \n ex -exit the app \n")

if __name__ == '__main__':
    main()