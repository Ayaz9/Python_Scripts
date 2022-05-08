''' 
This script helps us to find out current time in requested countries. 
#1 - first we import requests and json modules
#2 - we then register in https://api.timezonedb.com so that we can use their APIs for the list of countries
#3 - post pulling the data, we store Country names, Zone names, Current time and GMT info to separate lists
#4 - based on the user input, we find all available zone names with their current time and GMT
'''
import requests, json
from datetime import datetime

# Requesting data
url = "http://api.timezonedb.com/v2.1/list-time-zone?key=ZKXCERCSU4ZN&format=json"
response = requests.get(url).text
json_data = json.loads(response)
country_zones = json_data["zones"] 

country_list = []  # Country names
zonename_list = []  # Zone names
time_list = []  # Time stamps
gmt_list = []  # GMT 

# Iterating "countryName", "zoneName", "timestamp", "gmtOffset" and saving them to different lists
for keys_values_times in country_zones: 
    country_list.append(keys_values_times['countryName'])
    zonename_list.append(keys_values_times['zoneName'])
    time_list.append(datetime.utcfromtimestamp(int(keys_values_times['timestamp'])).strftime('%Y-%m-%d %H:%M:%S'))
    gmt_list.append(keys_values_times["gmtOffset"] / 3600)

while True:
    user_input = input('Enter country name (e.g. Poland) \n')
    all_index = [i for i, x in enumerate(country_list) if x == user_input]
    if len(all_index) == 0:
        print('Oooopss, the entered country name is not correct')
    else:
        print(f'Found {len(all_index)} result(s) for "{user_input}". Details are in below : \n') 
        for ind in all_index: 
            find_zone = zonename_list[ind]
            find_time = time_list[ind]
            gmt = gmt_list[ind]
            print(f'\
        Zone Name: {find_zone}\n\
        Current Time: {find_time} \n\
        GMT {gmt} \n')
