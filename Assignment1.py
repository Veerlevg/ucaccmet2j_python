# import json
import json

# open precipitation data
with open('precipitation.json', encoding='utf8') as file:
    precipitation_dict = json.load(file)

# Actions
# Code needed for Seattle: GHCND:US1WAKG0038
seattle_code = 'GHCND:US1WAKG0038'

# Create an empty list
value_month = [0]*12 # create a list of 12 0s

# Loop over dictionaries for Seattle
for measure in precipitation_dict:
    if measure['station'] == seattle_code:
    # split the dates to be able to select a month
        date = measure['date']
        date_split = date.split('-') 
        month = date_split[1]
    # count values for every month
        value_month[int(month)-1] += (measure['value'])
        
print(value_month)

# example of calculating it per month:
#         if month == '01':
#             value_january += (measure['value'])
# print(value_january)

# Save results to a json file
with open('precipitation_per_month_seattle.json', 'w', encoding='utf8') as file:
    json.dump(value_month, file)