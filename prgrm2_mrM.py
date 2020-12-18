import time
import string

password = []
alphabet = list(string.ascii_letters)
nums = [str(i) for i in range(10)]
symbols = ["-", "_", "."]
all_chars = alphabet + nums + symbols


def app_welcome():
    global password, start
    print(
        "Welcome to password hacker test. Enter 4 digit pw:"
    )
    password = list(input())
    print(password)
    set_combos()

def set_combos():
    combos_2 = ([x,y] for x in all_chars for y in all_chars)
    combos_3 = ([x,y,z] for x in all_chars for y in all_chars for z in all_chars)
    combos_4 = ([w,x,y,z] for w in all_chars for x in all_chars for y in all_chars for z in all_chars)
    #combos_5 = ([v,w,x,y,z] for v in all_chars for w in all_chars for x in all_chars for y in all_chars for z in all_chars)
    combos = [all_chars,combos_2, combos_3, combos_4]
    for l in combos:
      check_list(l)

def check_list(l):
  global start
  for item in l:
    if item == password:
      print("Found it!")
      print(list(item))
      return

app_welcome()