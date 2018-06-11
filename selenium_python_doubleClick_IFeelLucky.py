#doesn't work in chrome, don't know why.....
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

startTime = time.time()

browserOption = Options()
#to see how doubleclick works, should comment this out when run it
browserOption.add_argument("--headless")

browser = webdriver.Firefox(firefox_options=browserOption)
browser.maximize_window()
browser.get('https://www.google.com')

#position of I feel lucky button
clickPosition = browser.find_element_by_name('btnI')
#double click
webdriver.ActionChains(browser).double_click(clickPosition).perform()
#if internet is slow, screenshot will be a picture of loading page
time.sleep(2)
browser.get_screenshot_as_file("Ifeellucky.png")

endTime = time.time()
print("The whole process took: ", endTime-startTime, " Seconds.")
#time.sleep(2)
browser.close()

#the "I feel lucky" button actually require us to click twice to enter the new page
#I tried the move_to_element_with_offset to put cursor on the button and then perform(),
#  but there are 60% of chance not working...
