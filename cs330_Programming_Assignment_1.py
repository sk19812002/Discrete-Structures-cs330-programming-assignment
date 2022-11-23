# Hari Srikrishna, A20517199

DDDDD = input("Enter your student id: ")

unlock_code = DDDDD[-5:] + "1"
lock_code = DDDDD[-5:] + "4"

user_input = input("Enter access code: ")

if user_input == unlock_code:
   print("Unlocking the lock.")
elif user_input == lock_code:
   print("Locking the lock.")
else:
   print("Invalid code.")

import re

def security_engine(input_string, access_code):
 if re.search(access_code, input_string):
   print("unlocked")
 else:
   print("locked")

security_engine(user_input, DDDDD)