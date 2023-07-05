
from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
import csv

description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""

app = FastAPI(
    description=description,
)

# Load data from the CSV file and store it in the "db" list
db = []
with open('data.csv', 'r') as file:
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


def getCases(country=None, region=None, year=None):
    """
    Retrieves the total cases based on the given filters.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        int: The total number of cases.
    """
    total_cases = 0
    for row in db:
        if (country is None or country.lower() == row[2].lower()) and \
                (region is None or region == row[3]) and \
                (year is None or (year == int(row[0][:4]))):
            total_cases += int(row[4])
    return total_cases


def getMaxDeaths(country=None, region=None, year=None):
    """
    Retrieves the maximum number of deaths based on the given filters.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        int: The maximum number of deaths.
    """
    max_deaths = 0
    for row in db:
        if (country is None or country.lower() == row[2].lower()) and \
                (region is None or region == row[3]) and \
                (year is None or (year == int(row[0][:4]))):
            deaths = int(row[5])
            if deaths > max_deaths:
                max_deaths = deaths
    return max_deaths


def getMinDeaths(country=None, region=None, year=None):
    """
    Retrieves the minimum number of deaths based on the given filters.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        int: The minimum number of deaths.
    """
    min_deaths = float('inf')
    for row in db:
        if (country is None or country.lower() == row[2].lower()) and \
                (region is None or region == row[3]) and \
                (year is None or (year == int(row[0][:4]))):
            deaths = int(row[5])
            if deaths < min_deaths:
                min_deaths = deaths
    return min_deaths


def getAvgDeaths(country=None, region=None, year=None):
    """
    Retrieves the average number of deaths based on the given filters.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        float: The average number of deaths.
    """
    total_deaths = 0
    count = 0
    for row in db:
        if (country is None or country.lower() == row[2].lower()) and \
                (region is None or region == row[3]) and \
                (year is None or (year == int(row[0][:4]))):
            total_deaths += int(row[5])
            count += 1
    if count == 0:
        return 0
    return total_deaths / count


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


@app.get("/cases/")
async def cases(
    country: str = Query(None, description="A country name."),
    region: str = Query(None, description="A WHO region."),
    year: int = Query(None, description="A 4 digit year.")
):
    """
    Retrieves the total case count or can be filtered by country, region, and year.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        dict: Dictionary containing the total case count and filter parameters.
    """
    try:
        total_cases = getCases(country, region, year)
        return {
            "total": total_cases,
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


@app.get("/max_deaths/")
async def max_deaths(
    country: str = Query(None, description="A country name."),
    region: str = Query(None, description="A WHO region."),
    year: int = Query(None, description="A 4 digit year.")
):
    """
    Retrieves the maximum number of deaths or can be filtered by country, region, and year.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        dict: Dictionary containing the maximum number of deaths and filter parameters.
    """
    try:
        max_death_count = getMaxDeaths(country, region, year)
        return {
            "max_deaths": max_death_count,
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


@app.get("/min_deaths/")
async def min_deaths(
    country: str = Query(None, description="A country name."),
    region: str = Query(None, description="A WHO region."),
    year: int = Query(None, description="A 4 digit year.")
):
    """
    Retrieves the minimum number of deaths or can be filtered by country, region, and year.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        dict: Dictionary containing the minimum number of deaths and filter parameters.
    """
    try:
        min_death_count = getMinDeaths(country, region, year)
        return {
            "min_deaths": min_death_count,
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


@app.get("/avg_deaths/")
async def avg_deaths(
    country: str = Query(None, description="A country name."),
    region: str = Query(None, description="A WHO region."),
    year: int = Query(None, description="A 4 digit year.")
):
    """
    Retrieves the average number of deaths or can be filtered by country, region, and year.

    Args:
        country (str, optional): A country name. Defaults to None.
        region (str, optional): A WHO region. Defaults to None.
        year (int, optional): A 4-digit year. Defaults to None.

    Returns:
        dict: Dictionary containing the average number of deaths and filter parameters.
    """
    try:
        avg_death_count = getAvgDeaths(country, region, year)
        return {
            "avg_deaths": avg_death_count,
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


if __name__ == "__main__":
    import uvicorn
    from api import app 
    uvicorn.run("api:app", host="127.0.0.1", port=8080, log_level="info", reload=True)

