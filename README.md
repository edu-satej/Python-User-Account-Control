# Python User Account Control
## Overview
Python User Account Control is a simple application built in Python for managing user accounts using SQLite as the backend database. It provides basic functionalities for user signup and login operations.
## Features
- **Signup**: Allows users to create new accounts with unique usernames and passwords.
- **Login**: Validates user credentials against stored records in the database.
## Requirements
- Python 3.x
- SQLite 3 (comes pre-installed with Python)
## Installation
1. Clone the repository
2. Install dependencies (no external dependencies required beyond Python itself).
3. Run the application `main.py`
## Language Syntax
The UAC program prompts the user with a terminal that allows two functions to be executed with a few parameters. The syntax to create an account on the database is
`SIGNUP AS {USERNAME} WITH PASSWORD {PASSWORD}`.
Likewise, logging into an existing account would use a similar syntax:
`LOGIN AS {USERNAME} WITH PASSWORD {PASSWORD}`.
The UAC proogram is meant to be quite simple and helpful; hence, it kindly alerts the user if their syntax is incorrect. If you want to quit the shell, simply type `QUIT`.
