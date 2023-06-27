### A07-WEB SCRAPING

### Rakesh Rapalli

### Description

This project will combine a python GUI with a beautiful soup web scraper to: 1. grab, 2. save and 3. display the data. The initial python gui will be used to enter the appropriate values to allow you to leverage the URL, meaning it will accept values for: month, day, year, airport code, and one of the following: daily, weekly, monthly. The resulting python gui will display the received data in a tabular format.

The syntax that i have used in my code to return the url is this snippet provided in the assignment folder.

base_url = "https://wunderground.com/history"

Build the url to scrape weather from
url = f"{base_url}/{filter}/{airport}/{year}-{month}-{day}"

### Requirements:

- You need to have pysimple simple GUI, beautiful soup and selenium installed on your computer to the run this code.

- Include the airport-codes.csv in the same directory as the main code.

- Run the code in pysimple simple GUI and choose the day, month and year and click submit then it will print a url link.

- Use selenium to obtain the async data sent back from wunderground using that link.

- Use BS4 to parse the data and pull out the requested data.

- Finally, use PySimpleGui tabular view to display the data received from the initial request.

### NOTE

- I have included the links for seperate files of my code and the main code which has all the code together as well.

- The links for the same is given below.

|   #   | Folder Link | Assignment Description |
| :---: | ----------- | ---------------------- |
|   1   | [buildweather.py](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/buildweather.py) | Contains the code create the url |
|   2   | [extract_html.py](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/extract_html.py) | To extract the html content from the url
|   3   | [main.py](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/main.py) |The main code which has all the code including pygui to tabulate the html data
|   4   | [airport-codes.csv](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/airport-codes.csv)| csv file with airport codes
|   5   | [output files](https://github.com/RakeshRapalli6/4883-Software-Tools/tree/main/Assignments/A07/Output%20files)| has output images 


