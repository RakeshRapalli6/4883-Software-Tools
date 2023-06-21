"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumwire import webdriver                      
from selenium.webdriver.chrome.service import Service
import functools
flushprint = functools.partial(print, flush=True)

def asyncGetWeather(url):
    """Returns the page source HTML from a URL rendered by ChromeDriver.
    Args:
        url (str): The URL to get the page source HTML from.
    Returns:
        str: The page source HTML from the URL.
    """
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # run ChromeDriver
    driver = webdriver.Chrome(options=options)

    flushprint("Getting page...")
    driver.get(url)
    flushprint("waiting 6 seconds for dynamic data to load...")
    # wait for the web page to load
    time.sleep(6)
    flushprint("Done ... returning page source HTML")
    render = driver.page_source
    # quit ChromeDriver
    driver.quit()
   # return the page source HTML# return the page source HTML
    return render
    
if __name__=='__main__':

    # Could be a good idea to use the buildWeatherURL function from gui.py
    url = 'https://www.wunderground.com/history/monthly/CYEG/date/2005-4-4'

    # get the page source HTML from the URL
    page = asyncGetWeather(url)

    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
    
    # find the appropriate tag that contains the weather data
    history = soup.find('lib-city-history-observation')

    # print the parsed HTML
    print(history.prettify())
