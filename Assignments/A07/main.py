import PySimpleGUI as sg
import csv

import time                                             # needed for the sleep function
from bs4 import BeautifulSoup                           # used to parse the HTML
from selenium import webdriver                          # used to render the web page
from seleniumwire import webdriver                      
from selenium.webdriver.chrome.service import Service   # Service is only needed for ChromeDriverManager


import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)

def asyncGetWeather(url):
        """Returns the page source HTML from a URL rendered by ChromeDriver.
        Args:
            url (str): The URL to get the page source HTML from.
        Returns:
            str: The page source HTML from the URL.
            
        Help:
        https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
        """
        
        #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
        service = Service(executable_path='/Users/rakeshrapelli/Downloads/chromedriver_mac64 (2)')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        
        driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 10 seconds for dynamic data to load...")
        time.sleep(10)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML


def extractDataFromPageSource(pageSource, filter):
    """ Return the data from the page source. """
    # parse the HTML
    soup = BeautifulSoup(pageSource, 'html.parser')
    # find the appropriate tag that contains the weather data
    history = soup.find('lib-city-history-observation')

    headings = []
    data = []
    
    thead = history.find('thead').find('tr')
    # all heading have common class ng-star-inserted
    headerElements = thead.find_all(class_="ng-star-inserted")
    for head in headerElements:
        # if value is not empty then add it to heading
        if head.text.strip():
            headings.append(head.text.strip())

    tbody = history.find('tbody')
    if filter == 'daily':
        rowData = []
        tableRows = tbody.find_all('tr')
        
        for row in tableRows:
            for item in row:
                if item.text.strip():
                    rowData.append(item.text.strip())
            data.append(rowData)
    else:
        dataTables = tbody.find_all('table')
        for i in range(len(dataTables[0].find_all('tr'))):
            rowData = []
            for j in range(len(dataTables)):
                elementData = []
                for item in dataTables[j].find_all('tr')[i]:
                    if item.text.strip():
                        elementData.append(item.text.strip())
                rowData.append(elementData)
            data.append(rowData)
    
    return headings, data

def showTable(headings, tableData):
    """ Define function to show the data on the gui"""
    layout = [[sg.Table(values=tableData, headings=headings, justification='center', alternating_row_color='#b6edb2')]]
    window = sg.Window('Data Table', layout)
    event, values = window.read()


def loadAirportCodes():
    """ Load airport codes from a CSV file and return them as a list. """
    airport_codes = []
    with open('airport-codes.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            airport_codes.append(row['ident'])
    return airport_codes

def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return.  Valid values are 'tuple', 'list', or 'dict'.
    """
    from datetime import datetime
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]

    return {
        'day': datetime.now().day,
        'month': datetime.now().month,
        'year': datetime.now().year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):
    """ A GUI to pass parameters to get the weather from the web.
    Args:
        month (int): The month to get the weather for.
        day (int): The day to get the weather for.
        year (int): The year to get the weather for.
    Returns:
        Should return a URL like this, but replace the month, day, and year, filter, and airport with the values passed in.
        https://www.wunderground.com/history/daily/KCHO/date/2020-12-31
    """
    current_month, current_day, current_year = currentDate('tuple')

    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year
    if not airport:
        airport_codes = loadAirportCodes()
        airport = airport_codes[0] if airport_codes else ''

    # Define the values for the drop-down boxes
    month_values = [str(i) for i in range(1, 13)]
    day_values = [str(i) for i in range(1, 32)]
    year_values = [str(i) for i in range(2000, 2024)]
    airport_codes = loadAirportCodes()
    filter_values = ['daily', 'weekly', 'monthly']

    # Create the GUI layout using drop-down boxes for user input
    layout = [
        [sg.Text('Month')], [sg.DropDown(month_values, default_value=str(month))],
        [sg.Text('Day')], [sg.DropDown(day_values, default_value=str(day))],
        [sg.Text('Year')], [sg.DropDown(year_values, default_value=str(year))],
        [sg.Text('Code')], [sg.DropDown(airport_codes, default_value=airport)],
        [sg.Text('Daily / Weekly / Monthly')], [sg.DropDown(filter_values, default_value=filter)],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Get The Weather', layout)

    event, values = window.read()
    window.close()

    month = int(values[0])
    day = int(values[1])
    year = int(values[2])
    code = values[3]
    filter = values[4]

    base_url = "https://wunderground.com/history"
    # Return the URL to pass to wunderground to get appropriate weather data
    url = f"{base_url}/{filter}/{code}/date/{year}-{month}-{day}"
    print(url)
    return url, filter

if __name__ == "__main__":
    url, filter = buildWeatherURL()
    # get page source from url
    pageSource = asyncGetWeather(url)
    try:
        # get data from the pagesource
        headings, tableData = extractDataFromPageSource(pageSource, filter)
        showTable(headings, tableData)
    except:
        print("Plase check if you entered correct values!")
    
