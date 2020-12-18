#Follow along in class to create a password hacking program. This program will be designed to hack passwords up to a length of 4 characters long.
import string
import time

alphabet = list(string.ascii_letters)
symbols = ["!","*","_","+","@"]
nums = [str(i) for i in range(10)]
all_characters = alphabet+symbols+nums
password=""

# This algorithm generates passwords of lengths 1 to 4 characters and tests each one by calling the test_pw function after every time a character is added to the password
def hack_pw():
  h_password=[]
  for char in all_characters:#1st character
    h_password.append(char)
    found = test_pw(h_password)
    if found: return True
    for char in all_characters:#2nd character
      h_password.append(char)
      found = test_pw(h_password)
      if found: return True
      for char in all_characters:#3rd character
        h_password.append(char)
        found = test_pw(h_password)
        if found: return True
        for char in all_characters: #4th character
          h_password.append(char)
          found = test_pw(h_password)
          if found: return True
          h_password.pop()
        h_password.pop()
      h_password.pop()
    h_password.pop()

# message run at the start of program to get a password to test and then starts the testing
def welcome():
  global password
  print("Welcome to password hacker")
  print("Enter up to a 4 digit pasword:")
  password = list(input())
  print("You entered %s" % password)
  found_it = hack_pw()
  if found_it: print('Found your password')
  else: print("No password found")

# code to run an individual test of a password. It can trigger the entire program to end through the return True
def test_pw(h_pw):
  if(h_pw==password):
    print(h_pw)
    return True
  else: return False


welcome()