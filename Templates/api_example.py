import requests as re

id = "84600bca7507293656495e8972aec659"
payload = {'q':'Newcastle Upon Tyne, UK', 'units':'metric', 'appid':id}

def query_weather(payload,endpoint):
    #endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = re.get(endpoint, params=payload)

    return response

endpoint = "http://api.openweathermap.org/data/2.5/weather"

response = query_weather(payload,endpoint)

if response.status_code == 200:
    print(response.text)
else: 
    response = query_weather(payload,endpoint)

#print(response.url)
#print(response.status_code) 
#print(response.text) 

def jsonify(response):
    json_response = response.json()
    return json_response


json_response = jsonify(response)
print("\n")
print("The temperature is",json_response['main']['temp'], "degrees celsius.")
temp = json_response['main']['temp']

if temp < 10:
    print("Start boiler!")
else: 
    print("Keep boiler off.")

import pprint
#pprint.pprint(json_response)
# prints in a prettier pattern

#print("the temp in {} is {}".format("London",query_weather("London,UK")))