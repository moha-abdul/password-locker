#! /usr/bin/env python3.6

from user import User
from profile import Profile
import string
import random

def create_user(username, password): #create user
    ''' Method that creates a user '''
    new_user = User(username, password)
    return new_user

def create_profile(account, password): #create profile
    ''' Method that creates a profile '''
    new_profile = Profile(account, password)
    return new_profile

def save_users(user):
    ''' Method that creates a user '''
    user.save_user()

def save_profile(profile):
    ''' Method that saves a user '''
    profile.save_profile()

def del_users(user):
    ''' Method that deletes a user '''
    user.delete_user()

def del_profile(profile):
    ''' Method that deletes a profile '''
    profile.delete_profile()

def find_profile(profile):
    ''' Method that finds a profile by account name '''
    return Profile.find_profile_by_account(profile) 

# def check_existing_username(user):
# 	return User.user_exists(user)

def display_profiles(profile):
    ''' Method that displays all profiles '''
    return Profile.display_profiles(profile)



# def password_generate(pass_length):
    # return Profile.password_generate(pass_length)

short_code = input().lower()

def main():
    print("Welcome to your password locker. What is username do you want to use?")
    username = input()
    print("")

    print(f"Welcome {username}. Use the short codes please" )
    print("")

    while True:
        print("""Use these short codes: cn - create new account lg - log in to your password profiles lt - log out of you account ex - exit profile list.""")
        short_code = input().lower()
        if short_code == "cn":
            print("Name of profile account")

            print("PLease enter your first name")
            first_name = input()

            print("Enter last name.")
            last_name = input()
            
            print("create a personal password.")
            password = input()
            
            save_users(create_user(username, password))
        else:
            print(f"New account created for - {first_name} {last_name} your account password is - {password}")
            print("")
            print("You can now create your password profiles")
        while True:
            print("""Use these short codes:
                  cp -  new profile
                  ap - display all profiles
                  fp - find profile
                  ex - exit the profiles.""")
            short_code = input().lower()
            if short_code == "cp":
                print("What account are you creating? e.g twitter")
                account_name = input()
                print("Create your password \n")
                password = input()
                print(f" The password for {account} is {password}")

                # save_profile(create_profile(account_name, password, pass_length)
            elif short_code == "ap":
                if display_profiles(account):
                    print("Displaying all profiles")
                    print("")
                    for profile in display_profiles(profile):
                        print(f"Account: {profile.account}, Password: {profile.password}, Password length: {profile.pass_length}")
                else:
                    print("The profile does not exist")

            # elif short_code == "fp":
            #     print("Enter the profile you want to find")

            #     account = input()
            #     if profile_exists(cls,account):
            #         searched_profile = find_profile(account)
            #         print("\n")
            #         print(f"{searched_profile.account}")
            #         print(f"Password - {searched_profile.account}")
            #         print("")
            #         print(
            #             f"Password Length - {searched_profile.password}")
            #     else:
            #         print("profile does not exist")
            #         print("")

            elif short_code == "ex":
                print("")
                print("Thank you for using the password locker. Bye")
                print("")
                break


if __name__ == '__main__':
    main()