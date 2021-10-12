import schedule
from selenium import webdriver
import webbrowser
from browser import *
from googleLogin import *
from meet import *

def googleMeet():
  print("---------------WELCOME TO GOOGLE MEET CLI SERVICE---------------")
  
  print("This only works with Microsoft Edge.")
  print("Enter your Google Account details")
  email = str(input("Email Address: "))
  password = str(input("Enter the password: "))

  newMeet = int(input("Do you want to make a new meet? (Enter 1 if yes or 0 if no): "))
  if (newMeet!=1):
    code = str(input("Enter a Google Meet Code: "))

  browser()
  googleLogin(email,password)
  meet(code)

if __name__=="__main__":
  googleMeet()