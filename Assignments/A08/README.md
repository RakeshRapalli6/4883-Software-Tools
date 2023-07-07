
# COVID Data API

The COVID Data API is a Python FastAPI application that provides an interface to access COVID-19 data. It loads data from a CSV file containing COVID-19 statistics and offers endpoints to retrieve unique countries, WHO regions, and total deaths based on various filters.

## Installation

To run the COVID Data API, you need to have Python 3.x installed on your system. Follow these steps to set up the project:

1. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

2. Prepare the data file:
Place the CSV data file named data.csv in the project directory. The CSV file should contain the necessary COVID-19 data with headers.


## Usage
To start the FastAPI application, use the following command:

```bash
python api.py
```
Once the application is running, you can access the API documentation by opening the URL http://127.0.0.1:8080/docs in your web browser.

## Endpoints

### Get Unique Countries
Retrieves a list of unique countries present in the loaded data.

Endpoint: /countries/ 

Method: GET

Response:
```json
{
  "countries": ["Country A", "Country B", ...]
}
```

### Get Unique WHO Regions
Retrieves a list of unique WHO regions present in the loaded data.

Endpoint: /regions/

Method: GET

Response:
```json
{
  "regions": ["Region X", "Region Y", ...]
}
```


### Get Total Deaths
Retrieves the total number of deaths based on the given filters.

Endpoint: /deaths/

Method: GET

Parameters:

country (str): A country name.

region (str): A WHO region.

year (int): A 4-digit year.

Response:
```json
{
  "total": 8443748,
  "params": {
    "country": "Afghanistan",
    "region": "EMRO",
    "year": 2020
  },
  "success": true
}

```

### Get cases
Retrieves the num of cases by country, region and year

Endpoint: /cases/

Method: GET

Parameters:

country (str): A country name.

region (str): A WHO region.

year (int): A 4-digit year.


Response:
```json
{
  "total": 52330,
  "params": {
    "country": "Afghanistan",
    "region": "EMRO",
    "year": 2020
  },
  "success": true
}
```

### Get max_deaths
Retrieves the maximum number of deaths or can be filtered by country, region, and year.

Endpoint: /max_deaths/

Method: GET

Parameters:

country (str): A country name.

region (str): A WHO region.

year (int): A 4-digit year.


Response:
```json
 {
  "max_deaths": 52330,
  "params": {
    "country": "Afghanistan",
    "region": "EMRO",
    "year": 2020
  },
  "success": true
}
```

### Get min_deaths
Retrieves the minimum number of deaths or can be filtered by country, region, and year.

Endpoint: /min_deaths/

Method: GET

Parameters:

country (str): A country name.

region (str): A WHO region.

year (int): A 4-digit year.


Response:
```json
 {
  "min_deaths": 0,
  "params": {
    "country": "Afghanistan",
    "region": "EMRO",
    "year": 2020
  },
  "success": true
}
```

### Get avg_deaths
Retrieves the average number of deaths or can be filtered by country, region, and year.

Endpoint: /avg_deaths/

Method: GET

Parameters:

country (str): A country name.

region (str): A WHO region.

year (int): A 4-digit year.


Response:
```json
 {
  "avg_deaths": 23197.10989010989,
  "params": {
    "country": "Afghanistan",
    "region": "EMRO",
    "year": 2020
  },
  "success": true
}
```


|   #   | Folder Link | Assignment Description |
| :---: | ----------- | ---------------------- |
|   1   | [api.py](api.py) |  | has the main code of the project
|   2   | [extract_html.py](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/extract_html.py) | To extract the html content from the url
|   3   | [main.py](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/main.py) |The main code which has all the code including pygui to tabulate the html data
|   4   | [airport-codes.csv](https://github.com/RakeshRapalli6/4883-Software-Tools/blob/main/Assignments/A07/airport-codes.csv)| csv file with airport codes
|   5   | [output files](https://github.com/RakeshRapalli6/4883-Software-Tools/tree/main/Assignments/A07/Output%20files)| has output images 












