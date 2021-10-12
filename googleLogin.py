import time
import schedule
from selenium import webdriver
import webbrowser
import pynput
from browser import driver

def googleLogin(email, password):
  #Opening browser
  driver.get("https://accounts.google.com/signin/v2/identifier?service=accountsettings&   continue=https%3A%2F%2Fmyaccount.google.   com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&flowName=GlifWebSignIn&     flowEntry=ServiceLogin")

  #LOGGING INTO GOOGLE ACCOUNT

  #Email
  emailid = driver.find_element_by_xpath('//*[@id="identifierId"]')
  emailid.send_keys(email)
  nextbutton1 = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
  nextbutton1.click()

  time.sleep(4)#time for loading

  #Password
  passw=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
  passw.send_keys(password)
  nextbutton2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
  nextbutton2.click()

  time.sleep(5)#time for loading