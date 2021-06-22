import requests
from datetime import datetime

#weather API
api_key = '9c8cd52e6e26d1747e24839322e6f3ed'

PlaceName = input("Enter the city name: ")

API = "https://api.openweathermap.org/data/2.5/weather?q="+PlaceName+"&appid="+api_key
API_Link = requests.get(API)
API_Data = API_Link.json()

#create variables to store and display data
TempratureCity = ((API_Data['main']['temp']) - 273.15)
TempratureDescription = API_Data['weather'][0]['description']
TempratureHumidity = API_Data['main']['humidity']
WindSpeed = API_Data['wind']['speed']
DateTime = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-----------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(PlaceName.upper(), DateTime))
print ("-----------------------------------------------------------------")

print ("Current temperature is : {:.2f} deg C".format(TempratureCity))
print ("Current weather desc   : ",TempratureDescription)
print ("Current Humidity       : ",TempratureHumidity, '%')
print ("Current wind speed     : ",WindSpeed ,'kmph')

with open("weather_info.txt", "a") as ptr:
    ptr.write("Country Name Is             : "+PlaceName)
    ptr.write(("\nCurrent Temperature Is   : {:.2f} Deg C".format(TempratureCity)))
    ptr.write("\nCurrent Weather Desc Is   : "+str(TempratureDescription))
    ptr.write("\nCurrent Humidity Is       : "+str(TempratureHumidity)+'%')
    ptr.write("\nCurrent Wind Speed Is     : "+str(WindSpeed)+'kmph')
    ptr.write("\n------------------------------------------------------------\n\n")

print("Data is Saved in File..")
print("Congrats, Your Assignment Is Complete..")