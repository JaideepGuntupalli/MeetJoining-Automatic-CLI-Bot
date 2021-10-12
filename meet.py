from importlib import find_loader
import time
import schedule
from selenium import webdriver
import webbrowser
import pynput
from browser import driver

def meet(code):
  #making url
  url = "https://meet.google.com/" + code
  
  #OPENING MEET LINK
  driver.get(url)

  n=15

  time.sleep(10)

  while(n>0):
    #Setting background for safety if we need turn on cam for some reason.
    background = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/  div/div[1]/div[1]/div/div[6]/div')
    if(background!=None):
      break
    else:
      time.sleep(3)
      n-=1

  if(background==None):
    driver.close()

  background.click()

  time.sleep(2)#time for loading

  #Selecting the background
  prefback = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/  div[1]/div[1]/div[2]/div/c-wiz/div/div[5]/div/button')
  prefback.click()

  time.sleep(1)#time for loading

  #Turning of Video and Mic
  vid = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1] /div[1]/div[1]/div[4]/div[2]/div/div')
  vid.click()

  time.sleep(1)#time for loading

  aud = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1] /div[1]/div[1]/div[4]/div[1]/div/div/div')
  aud.click()

  time.sleep(1)#time for loading

  #Joining the meet
  join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div [2]/div/div[2]/div/div[1]/div[1]')
  join.click()