# import json 



# filename = '12345.json'
# entry = {'carl': 33}

# with open(filename, 'r') as file:
#     data = json.load(file)

# data.append(entry)

# with open(filename, 'w') as file:
#     json.dump(data, file)



# import json
# import requests

# url = "https//api.punkapi.com/v2/beers"

# s = requests.get(url)

# data = json.loads(s.text)



# beer_list = []

# for beer in data:
#     name = beer['name']
#     tagline = beer['tagline']
#     abv = beer['abv']

#     beer_item = {
#         "name" : name,
#         "tagline" : tagline,
#         "abv" : abv}
#     beer_list.append(beer_item)

# print(beer_list)

from for_date_time import date
import json

sample = {
  "name": "AVGO",
  "time": "06.39.29__PM",
  "price": 1227.0,
  "percentage_change": 2.25
}


f = open(f"test_{date()}.json", "a")
f.write(sample)
f.close()

#open and read the file after the appending:
f = open(f"test_{date()}.json", "r")
print(f.read())