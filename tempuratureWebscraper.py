import requests
from bs4 import BeautifulSoup
import time


def getTempBlacksVa()->int:
    r = requests.get('https://weather.com/weather/today/l/37.23,-80.41?par=google')

    soup = BeautifulSoup(r.content, 'html.parser')

    temp = soup.find(attrs={'data-testid':'TemperatureValue'})

    temp = str(temp)

    temp = str(temp[91])+str(temp[92])

    temp = int(temp)

    return temp

#Loop to check temp every few minutes
while True:
    #currently set to 5 minutes:
    time.sleep(5*60)
    blackTemp = getTempBlacksVa()
    print(blackTemp)
    #TODO:
    #write int blackTemp to a file that

