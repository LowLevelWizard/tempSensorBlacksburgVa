import requests
from bs4 import BeautifulSoup
import time
import os


def getTempBlacksVa()->int:
    r = requests.get('https://weather.com/weather/today/l/37.23,-80.41?par=google')

    soup = BeautifulSoup(r.content, 'html.parser')

    temp = soup.find(attrs={'data-testid':'TemperatureValue'})

    temp = str(temp)

    temp = str(temp[91])+str(temp[92])

    temp = int(temp)

    return temp

def tempToText(temp):
    #setting up file system:
    
    cwd = os.getcwd()
    #to be changed later
    cwd = os.path.join(cwd, "code", "python", "tempBlacksBurgVa", "updatingFile", "temp.txt")
    file = open(cwd, "w")
    file.write(str(temp))
    file.close()




#Initial Checkup:
blackTemp = getTempBlacksVa()
print(blackTemp)
tempToText(blackTemp)

#Loop to check temp every few minutes
while True:
    #currently set to 5 minutes:
    time.sleep(10)
    blackTemp = getTempBlacksVa()
    print(blackTemp)
    #TODO:
    #write int blackTemp to a file that the webserver can see
    tempToText(blackTemp)


