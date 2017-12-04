from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def thrashit():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-position=1694,-22")
    driver = webdriver.Chrome("C:\\Users\\jace\\Documents\\chromedriver_win32\\chromedriver.exe", chrome_options=chrome_options)

    driver.get("http://www.thrashermagazine.com/articles/who-should-be-the-2017-skater-of-the-year/")
    radio = driver.find_element_by_xpath("//*[@id='pds-answer9879747']/span[13]/label/span")
    radio.click()
    vote = driver.find_element_by_xpath("//*[@id='pd-vote-button9879747']/span")
    vote.click()
    driver.close()

for x in range(1000):
    thrashit()
    print("Done %s time(s)" %(x+1))