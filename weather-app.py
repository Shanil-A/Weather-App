import requests
city=input("Enter the city name : ")
api_key="9d1a1925637f4acc602823ad55b09abc"
url="https://api.openweathermap.org/data/2.5/weather"
params={
    "q":city,
    "appid":api_key,
    "units":"metric"
}
response=requests.get(url,params=params)
if response.status_code==200:
    data=response.json()
    temperature=data["main"]["temp"]
    condition=data["weather"][0]["description"]
    city_name=data["name"]
    print("\nWeather Report")
    print("\n")
    print("City : ",city_name)
    print("Temperature : ",temperature," C")
    print("Condition : ",condition)
else:
    print("Error: City not found or API problem")