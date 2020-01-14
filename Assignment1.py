# PART 1
# import json
import json

# open precipitation data
with open('precipitation.json', encoding='utf8') as file:
    precipitation_dict = json.load(file)

# Actions
# Code needed for Seattle: GHCND:US1WAKG0038
seattle_code = 'GHCND:US1WAKG0038'

# Create an empty list
value_month = [0]*12 # create a list of 12 0s as a starting point for each month

# Loop over dictionaries for Seattle
for measure in precipitation_dict:
    if measure['station'] == seattle_code:
    # split the dates to be able to select a month
        date = measure['date']
        date_split = date.split('-') 
        month = date_split[1]
    # count values for every month
        value_month[int(month)-1] += (measure['value']) # by doing -1, the index and month integer are the same
        
print(value_month)

# example of calculating it per month:
#         if month == '01':
#             value_january += (measure['value'])
# print(value_january)

# Save results to a json file
with open('precipitation_per_month_seattle.json', 'w', encoding='utf8') as file:
    json.dump(value_month, file)

# PART 2

# Calculate sum of precipitation over the whole year
total_precipitation = 0
for value in value_month:
    total_precipitation = total_precipitation + value
print(total_precipitation)

# Calculate relative precipitation per month
# relative precipitation = value/total_precipitation
relative_precipitation = [0]*12
for month in range(12):
    relative_precipitation[month] = value_month[month] / total_precipitation
print(relative_precipitation)

# Save results to a json file
with open('relative_precipitation_per_month_seattle.json', 'w', encoding='utf8') as file:
    json.dump(relative_precipitation, file)
     
     
precipitation_dictionary = {
"Seattle": {
	"station": "GHCND:US1WAKG0038", 
	"state": "WA", 
	"totalMonthlyPrecipitation": [value_month], 
	"relativeMonthlyPrecipitation": [relative_precipitation], 
	"totalYearlyPrecipitation": total_precipitation,
	}
}

with open('total_precipitation_dictionary.json', 'w', encoding='utf8') as file:
    json.dump(precipitation_dictionary, file)
