import schedule
from selenium import webdriver
import webbrowser
import pynput

def browser():
  opt = webdriver.EdgeOptions()
  opt.add_argument("--disable-infobars")
  opt.add_argument("--disable-extensions")
  opt.add_argument("start-maximized")
  opt.add_argument("--start-maximized")
  # Pass the argument 1 to allow and 2 to block
  opt.use_chromium=True
  opt.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_mic": 1, 
      "profile.default_content_setting_values.media_stream_camera": 1,
      "profile.default_content_setting_values.geolocation": 1, 
      "profile.default_content_setting_values.notifications": 1 
    })

  #Intialising browser
  global driver
  driver=webdriver.Edge(executable_path="C:\\Users\\LENOVO\\Auto\\msedgedriver.exe",options=opt)