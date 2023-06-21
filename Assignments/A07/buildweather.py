import PySimpleGUI as sg
import csv

def loadAirportCodes():
    airport_codes = []
    with open('airport-codes.csv', newline='') as csvfile:
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

    sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")
    base_url = "https://wunderground.com/history"
    # Return the URL to pass to wunderground to get appropriate weather data
    url = f"{base_url}/{filter}/{code}/date/{year}-{month}-{day}"
    print(url)
    return url

if __name__ == "__main__":
  buildWeatherURL()


