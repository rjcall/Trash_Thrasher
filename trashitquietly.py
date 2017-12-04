from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def thrashit_q():
    driver = webdriver.PhantomJS(r"C:\Users\jace\Downloads\phantomjs-2.1.1-windows (1)\phantomjs-2.1.1-windows\bin\phantomjs.exe")

    driver.get("http://www.thrashermagazine.com/articles/who-should-be-the-2017-skater-of-the-year/")
    radio = driver.find_element_by_xpath("//*[@id='pds-answer9879747']/span[13]/label/span")
    radio.click()
    vote = driver.find_element_by_xpath("//*[@id='pd-vote-button9879747']/span")
    vote.click()
    sleep(1)
    driver.close()

for x in range(1000):
    thrashit_q()
    print("Done %s time(s)" %(x+1))

