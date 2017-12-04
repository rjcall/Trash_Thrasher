from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime


def thrashit_q(num):
    s = "LAST SCREEN SHOT TAKEN %s\nSKATE & DESTROY" %datetime.now().strftime("%d %B %Y %I:%M:%S %p")
    driver = webdriver.PhantomJS(r"C:\Users\jace\Downloads\phantomjs-2.1.1-windows (1)\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    b = "--"*len(s)

    driver.get("http://www.thrashermagazine.com/articles/who-should-be-the-2017-skater-of-the-year/")
    radio = driver.find_element_by_xpath("//*[@id='pds-answer9879747']/span[13]/label/span")
    radio.click()
    vote = driver.find_element_by_xpath("//*[@id='pd-vote-button9879747']/span")
    vote.click()
    sleep(1)

    if num % 25 == 0:
    	driver.save_screenshot('trashitchrome.png')
    	print(b)
    	print(s)
    	print(b)
    driver.close()


thrashit_q(25)