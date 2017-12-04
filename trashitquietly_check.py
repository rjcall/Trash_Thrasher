from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

def thrashit_q(num):

    s = "LAST SCREEN SHOT TAKEN %s\nSKATE & DESTROY" %datetime.now().strftime("%d %B %Y %I:%M:%S %p")
    driver = webdriver.PhantomJS(r"C:\Users\jace\Downloads\phantomjs-2.1.1-windows (1)\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    b = "--"*len(s)
    duck = True
    dounter = 1
    driver.get("http://www.thrashermagazine.com/articles/who-should-be-the-2017-skater-of-the-year/")
    while duck and dounter < 60:
        try:
            success = driver.find_element_by_xpath('//*[@id="PDI_container9879747"]/div/div/div/div/div[1]/div/div/div')
            print("Thrasher says: ",success.text)
            duck = False
        except:
            print("Thrasher didnt respond %s times:(\nSLEEPING FOR A SEC & TRYING AGIAN" %dounter)
            sleep(1)
        dounter +=1
    radio = driver.find_element_by_xpath("//*[@id='pds-answer9879747']/span[13]/label/span")
    radio.click()
    print("You selected %s for skater of the year!" %radio.text)
    vote = driver.find_element_by_xpath("//*[@id='pd-vote-button9879747']/span")
    vote.click()
    sleep(.25)
    suck = True
    counter = 1
    while suck and counter < 60:
        try:
            success = driver.find_element_by_xpath('//*[@id="PDI_container9879747"]/div/div/div/div/div[1]/div/div/div')
            print("Thrasher says: ",success.text)
            suck = False
        except:
            print("Thrasher didnt respond %s times:(\nSLEEPING FOR A SEC & TRYING AGIAN" %counter)
            sleep(1)
        counter +=1


    if num % 50 == 0:
        driver.save_screenshot('trashit_q_check.png')
        print("LAST SCREEN SHOT TAKEN %s\nSKATE & DESTROY" %datetime.now().strftime("%d %B %Y %I:%M:%S %p"))
    driver.close()

for x in range(1,1000):
    thrashit_q(x)
    print("Done %s time(s)" %(x+1))
thrashit_q(25)
