A07-WEB SCRAPING

Rakesh Rapalli

This project will combine a python GUI with a beautiful soup web scraper to: 1. grab, 2. save and 3. display the data. The initial python gui will be used to enter the appropriate values to allow you to leverage the URL, meaning it will accept values for: month, day, year, airport code, and one of the following: daily, weekly, monthly. The resulting python gui will display the received data in a tabular format.

The syntax that i have used in my code to return the url is this snippet provided in the assignment folder.
base_url = "https://wunderground.com/history"
filter = "monthly"
airport = "YPJT"
year = "2021"
month = "6"
day = "1"

# build the url to scrape weather from
url = f"{base_url}/{filter}/{airport}/{year}-{month}-{day}"


|   #   | Folder Link | Assignment Description |
| :---: | ----------- | ---------------------- |
|   1   | [buildweather.py](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/buildweather.py) | Contains the code create the url |
|   2   | [extract_html.py](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/extract_html.py) | To extract the html content from the url
|   3   | [main.py](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/main.py) |The main code which has all the code including pygui to tabulate the html data
|   4   | [airport-codes.csv](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/airport-codes.csv)| csv file with airport codes
|   5   | [output files](https://github.com/RakeshRapalli6/4883-Software-Tools/tree/main/Assignments/A07/Output%20files)| has output images 


