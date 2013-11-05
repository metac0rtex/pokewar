#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = ""  #your facebook username
pwd = ""  #your facebook password
vic = ""  #Victims Username
vicurl = "https://www.facebook.com/" + vic

def banner():
  print "             --== PokeWar ==--"
  print "              By: metacortex"
  print "Annoying your facebook friends one poke at a time"

def attack(driver):
  print "    [+] Poke!"
  poke = driver.find_element_by_partial_link_text("Poke")
  poke.click()
  close = driver.find_element_by_partial_link_text("Remove")
  close.click()

def login(driver, usr, pwd):
  print "[+] Accessing Facebook"
  driver.get("http://www.facebook.com/")
  print "  [+] Logging in"
  email = driver.find_element_by_id("email")
  email.send_keys(usr)
  password = driver.find_element_by_id("pass")
  password.send_keys(pwd)
  login = driver.find_element_by_id("loginbutton")
  login.click()

def visitvic(driver):
  print "  [+] Visiting Victims page"
  driver.get(vicurl)
  print "    [+] Sucess"
  print "  [+] Opening Timeline Menu"
  menu = driver.find_element_by_class_name("fbTimelineActionSelectorButton")
  menu.click()
  print "    [+] Sucess"


banner()
print "[+] Setting Web Driver to " + browser
driver = webdriver.Firefox()
print "  [+] Success"
login(driver, usr, pwd)
print "    [+] Logged in"
visitvic(driver)
print "  [+] Attacking Victim"
while True:
  try:
    attack(driver)
  except:
    pass

driver.close()
