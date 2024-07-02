'''
Aproach:
1. Extract data form given URL.
2. Scrape th data with the help of BeautifulSoup.
3. Convert the data into html code.
4. Find the required details and filter them.
5. Save the resutl in the String.
6. Pass the result to the notification object.
'''

import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def get_data(url):
    response = requests.get(url)
    return response.text

htmldata = get_data("https://www.weather.com/en-IN/weather/today/l/INXX0096:1:IN")

soup = BeautifulSoup(htmldata, 'html.parser')

current_temp = soup.find_all("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chances_rain = soup.find_all("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
temp = str(current_temp)
temp_rain = str(chances_rain)

result = "Current Temperature is: " + temp[91:93] + "°C" + "\n" + "Chances of Rain: " + temp_rain[91:93] + "%"

n.show_toast("Live Weather Notification", result, duration=10)

print("Notification displayed successfully!")
