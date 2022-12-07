'''Password generator is a programme that generates a random password using combinations of lower & upper case along with use of NUMBER AND Symbol'''
import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "1234567890"
Symbol = "!@#$%^&*"

all = lower + upper + NUMBER + Symbol
length = 6
password = "".join(random.sample(all,length))
print("The randomised Password You Generated is :",password)
