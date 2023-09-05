import PART1

air_quality = PART1.read_data("air_quality.csv")
uhf = PART1.read_uhf("uhf.csv")
maps_id = air_quality[0]
maps_date = air_quality[1]
maps_zipcode = uhf[0]
maps_borough = uhf[1]

# Highest and lowest pollution measurement ever recorded in 10027
measurements = []
list_10027_ids = maps_zipcode['10027']
for id_10027 in list_10027_ids:
    list_measurement_tuples = maps_id[id_10027]
    for measurement_tuple in list_measurement_tuples:
        pollution = float(measurement_tuple[3])
        measurements.append(pollution)
highest = max(measurements)
lowest = min(measurements)
print(f"The highest and lowest pollution measurements ever recorded in 10027 are {highest} mcg/m^3 and {lowest} mcg/m^3 respectively.")
print("")

# Worst pollution in 2019
list_2019 = []
for date in maps_date:
    date_splitted = date.split('/')
    if date_splitted[2] == "2019": 
        list_2019.append(maps_date[date])   
        
worst_pollution = 0
worst_UHF_ID = 0

for measurements in list_2019:
    for ele in measurements:
        if float(ele[3]) > worst_pollution:
            worst_pollution = float(ele[3])
            worst_UHF_ID = ele[0]
print(f"UHF ID {worst_UHF_ID} had the worst pollution in 2019.")
print("")

# Average pollution in Manhattan in 2008 and 2019
list_manhattan_2019 = []
for measurements in list_2019:
    for ele in measurements:
        if ele[0] in maps_borough['Manhattan']:
            list_manhattan_2019.append(float(ele[3]))
average_2019 = sum(list_manhattan_2019)/len(list_manhattan_2019)
print("The average air pollution in Manhattan in 2019 was {:.2f} mcg/m^3.".format(average_2019))
print("")

list_2008 = []
for date in maps_date:
    date_splitted = date.split('/')
    if date_splitted[2] == "2008":
        for measure3 in maps_date[date]:
            list_2008.append(measure3)
            
list_manhattan_2008 = []
for element2 in list_2008:
    if element2[0] in maps_borough['Manhattan']:
        list_manhattan_2008.append(float(element2[3]))
average_2008 = sum(list_manhattan_2008)/len(list_manhattan_2008)
print("The average air pollution in Manhattan in 2008 was {:.2f} mcg/m^3.".format(average_2008)) 
print("")

# Additional questions about the dataset:
# Question 1: Which NYC neighborhood had the best air quality in June of 2012?
air_quality_2012 = []
for ele in maps_date:
    date = ele.split('/')
    if date[0] == "6" and date[2] == "2012": 
        air_quality_2012.append(maps_date[ele])
        
pollution_values = []    
for ele in air_quality_2012:
    for measurements in ele:
        pollution = float(measurements[3])
        pollution_values.append(pollution)
        
sorted_pollution_values = sorted(pollution_values, key = float)
for ele in air_quality_2012:
    for measurements in ele:
        if float(measurements[3]) == sorted_pollution_values[0]:
            neighborhood = measurements[1]
            pollution = float(measurements[3])
print(f"The NYC neighborhood with the best air quality in June of 2012 is {neighborhood} with {pollution} mcg/m^3.")
print("")

# Question 2: Which borough is the zip code 11221 located in? How many total zipcodes are in this borough?
if len(maps_zipcode['11221']) == 1:
    uhf_id = maps_zipcode['11221'][0]
    for borough, ids in maps_borough.items():
        if uhf_id in ids: 
            borough_name = borough
            
all_zipcodes = []
for ele in maps_borough:
    if ele == borough_name:
        uhfs = maps_borough[ele]
        
for uhf in uhfs:
    for zipcode, ids in maps_zipcode.items():
        if uhf in ids:
            all_zipcodes.append(zipcode)
total_zipcodes = len(all_zipcodes)

print(f"The zip code 11221 is located in {borough_name}. There are {total_zipcodes} total zipcodes in {borough_name}.")
