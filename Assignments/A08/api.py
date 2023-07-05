from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
import csv
import os

description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""

app = FastAPI(
    description=description,
)

# Get the absolute path of the directory containing this Python file
directory = os.path.dirname(os.path.abspath(__file__))

# Load data from the CSV file and store it in the "db" list
db = []
csv_file_path = os.path.join(directory, 'data.csv')
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    db = list(reader)

def getUniqueCountries():
    """
    Retrieves a list of unique countries from the loaded data.

    Returns:
        List[str]: A list of unique country names.
    """
    countries = set()
    for row in db:
        countries.add(row[2])
    return list(countries)


def getUniqueRegions():
    """
    Retrieves a list of unique WHO regions from the loaded data.

    Returns:
        List[str]: A list of unique WHO regions.
    """
    regions = set()
    for row in db:
        regions.add(row[3])
    return list(regions)


def getDeaths(country=None, region=None, year=None):
    """
    Retrieves the total deaths based on the given filters.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        int: The total number of deaths.
    """
    total_deaths = 0
    for row in db:
        if (country is None or country.lower() == row[2].lower()) and \
                (region is None or region == row[3]) and \
                (year is None or (year == int(row[0][:4]))):
            total_deaths += int(row[5])
    return total_deaths


@app.get("/")
async def docs_redirect():
    """
    Redirects to the documentation page.
    """
    return RedirectResponse(url="/docs")


@app.get("/countries/")
async def countries():
    """
    Retrieves a list of unique countries.

    Returns:
        dict: Dictionary containing the list of countries.
    """
    return {"countries": getUniqueCountries()}


@app.get("/regions/")
async def regions():
    """
    Retrieves a list of unique WHO regions.

    Returns:
        dict: Dictionary containing the list of regions.
    """
    return {"regions": getUniqueRegions()}


@app.get("/deaths/")
async def deaths(
        country: str = Query(None, description="A country name."),
        region: str = Query(None, description="A WHO region."),
        year: int = Query(None, description="A 4 digit year.")
):
    """
    Retrieves the total death count or can be filtered by country, region, and year.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        dict: Dictionary containing the total death count and filter parameters.
    """
    try:
        total_deaths = getDeaths(country, region, year)
        return {
            "total": total_deaths,
            "params": {
                "country": country,
                "region": region,
                "year": year
            },
            "success": True,
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


import uvicorn
from api import app 

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8080, log_level="info", reload=True)
