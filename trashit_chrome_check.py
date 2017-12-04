from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

def thrashit(num):
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
    sleep(1)
    success = driver.find_element_by_xpath('//*[@id="PDI_container9879747"]/div/div/div/div/div[1]/div/div/div')
    print("Thrasher says: ", success.text)
    if num % 25 == 0:
        driver.save_screenshot('trashitchrome.png')
        print("last ss taken at %s\nSKATE & DESTROY" %datetime.now().strftime("%d %B %Y %I:%M:%S %p"))
    driver.close()

for x in range(1,1000):
    thrashit(x)
    print("Done %s time(s)" %(x))