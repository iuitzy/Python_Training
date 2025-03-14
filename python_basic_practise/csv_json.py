import csv 
import json 

csv_file = 'data.csv'
json_file = 'data_transform.json'

def read_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
    
def write_json(data,json_file):
    with open (json_file, 'w') as file:
        json.dump(data, file, indent=4)
        print ("data sucessfully transfered")

def convert_csv_to_json(csv_file,json_file):
    data = read_csv(csv_file)
    write_json(data,json_file)

convert_csv_to_json(csv_file,json_file)