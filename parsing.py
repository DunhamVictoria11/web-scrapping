import requests
from bs4 import BeautifulSoup
import pandas as pd
page=requests.get('https://forecast.weather.gov/MapClick.php?lat=33.94880700000006&lon=-118.24650799999996#.XjFImusuc2w')
soup=BeautifulSoup(page.content,'html.parser')
week=soup.find(id='seven-day-forecast-list')
items=week.find_all(class_='tombstone-container') #getting a whole week 
period_name=[item.find(class_='period-name').get_text() for item in items] #put every element(day) to a list
short_desc=[item.find(class_='short-desc').get_text() for item in items]
temperature=[item.find(class_='temp').get_text()
weather_stuff=pd.DataFrame(
  {'period':period_name,
  'short-description':short_desc,
  'temperature':temperature}
)
#gather all data and put it into DataFrame
print(weather_stuff)
