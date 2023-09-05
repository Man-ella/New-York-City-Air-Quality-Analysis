import csv

def read_data(filename):
  """
  should return two dictionaries (i.e. a tuple with two elements, 
  each of them a dictionary).

  1) A dictionary mapping each UHF geographic IDs to a lists of measurement tuples.
  2) A dictionary mapping each date (as a string) to a list of measurement tuples.
  """ 
  geographic_ids_dict = {}
  dates_dict = {}
  with open(filename,'r', encoding='utf-8-sig') as data_file:
      tuple_list = []
      reader = csv.reader(data_file)
      for line in reader:
          data_tuple = tuple(line)
          tuple_list.append(data_tuple)
      for a, b, c, d in tuple_list:
          if not a in geographic_ids_dict:
              geographic_ids_dict[a] = [(a, b, c, d)]
          else:
              geographic_ids_dict[a].append((a, b, c, d))
      for a, b, c, d in tuple_list:
          if not c in dates_dict:
              dates_dict[c]= [(a, b, c, d)]
          else:
              dates_dict[c].append((a, b, c, d))
      result = (geographic_ids_dict, dates_dict)
      return result

def measurement_to_string(measurement):
  """
  format a single measurement tuple as a string. For example: 
  "6/1/09 UHF 205 Sunset Park 11.45 mcg/m^3"
  """
  geo_id = measurement[0]
  geo_description = measurement[1]
  date = measurement[2]
  value = measurement[3]
  result = f"{date} UHF {geo_id} {geo_description} {value} mcg/m^3"
  return result

def read_uhf(filename):
  """
  should return two dictionaries: 
  1) A dictionary mapping each zip code to a list of UHF geographic IDs 
  2) A dictionary mapping each borough name to a list of UHF geographic IDs.
  """
  zip_code_dict = {}
  borough_dict = {}
  with open(filename,'r', encoding='utf-8-sig') as data_file:
      tuple_list = []
      reader = csv.reader(data_file)
      for line in reader:
          data_tuple = tuple(line)
          tuple_list.append(data_tuple)
      for ele in tuple_list:
          idx = 3
          while idx <= (len(ele) - 1):
              if ele[idx] not in zip_code_dict:
                 zip_code = ele[idx]
                 zip_code_dict[zip_code] = [ele[2]]
                 idx += 1
              else:
                  zip_code = ele[idx]
                  zip_code_dict[zip_code].append(ele[2])
                  idx += 1
      for ele in tuple_list:
          borough_name = ele[0]
          if borough_name in borough_dict:
              borough_dict[borough_name].append(ele[2])
          else:
              borough_dict[borough_name] = [ele[2]]
      result = (zip_code_dict, borough_dict)                             
      return result
  
def main():
    status = True
    
    while status == True:
        air_quality = read_data("air_quality.csv")
        uhf = read_uhf("uhf.csv")
        method = input("Search by zipcode, UHF ID, borough or date: ")
        search = input(f"Enter the {method}: ")
        
        if method == "zipcode":
            zipcode_ids_list = uhf[0][search]
            for zipcode_id in zipcode_ids_list:
                measurement_tuple_list = air_quality[0][zipcode_id]
                for measurement in measurement_tuple_list:
                    print(measurement_to_string(measurement))
        
        elif method == "borough":
            borough_ids_list = uhf[1][search]
            for borough_id in borough_ids_list:
                measurement_tuple_list1 = air_quality[0][borough_id]
                for measurement1 in measurement_tuple_list1:
                    print(measurement_to_string(measurement1))
                    
        elif method == "UHF ID":
            measurement_tuple_list2 = air_quality[0][search]
            for measurement2 in measurement_tuple_list2:
                print(measurement_to_string(measurement2))
                
        elif method == "date":
            measurement_tuple_list3 = air_quality[1][search]
            for measurement3 in measurement_tuple_list3:
                print(measurement_to_string(measurement3))
                
        epoch = input("Type 'yes' to continue search or 'no' to end search: " )
        if epoch == "no":
            status = False
       
if __name__ == "__main__":
    main()