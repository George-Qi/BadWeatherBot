import requests

url = "https://community-open-weather-map.p.rapidapi.com/forecast"

querystring = {"q":"jinan, China", "lang":"zhcn"}

headers = {
    'x-rapidapi-key': "947e8891camsha0d6bcf0c8062e4p114536jsnfdeac00c4288",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)