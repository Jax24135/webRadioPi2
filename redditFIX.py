# launches Firefox webbrower to a specified URL
# waits 60 seconds then refreshes the webpage << does this 3 times (for testing)

import time
from selenium import webdriver

def main():
    # open URL in browser
    driver = webdriver.Firefox()
    driver.get('http://ice64.securenetsystems.net/WMOT?&playSessionID=B6847FBF-E170-EE5A-ED62702AF4B')

    #define loop to refresh page 3 times
    for x in range(3):
        time.sleep(60)
        driver.refresh()

main()
