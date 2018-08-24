#! /usr/bin/env python3.6

from user import User
import string
import random

def create_account(first_name,last_name,username, password): #create contact
	new_user = User(first_name, last_name, username, password)
	return new_user

if __name__ == '__main__':
    main()