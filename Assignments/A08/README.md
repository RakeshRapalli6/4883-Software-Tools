
# COVID Data API

The COVID Data API is a Python FastAPI application that provides an interface to access COVID-19 data. It loads data from a CSV file containing COVID-19 statistics and offers endpoints to retrieve unique countries, WHO regions, and total deaths based on various filters.

## Installation

To run the COVID Data API, you need to have Python 3.x installed on your system. Follow these steps to set up the project:

1. Clone the repository to your local machine:
```bash
  git clone https://github.com/your_username/covid-data-api.git
  cd covid-data-api

```

2. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

3. Prepare the data file:
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
  "total": 1234,
  "params": {
    "country": "Country A",
    "region": "Region X",
    "year": 2023
  },
  "success": true
}

```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Credits

The COVID Data API is created by 'Name'. It uses the FastAPI framework and various Python libraries for data handling and processing.

