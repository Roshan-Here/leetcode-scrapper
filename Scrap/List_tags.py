"""
Program to list tags into required json
"""

import csv,json

def list_tags_from_csv(csv_filename,json_file_name):
    required_json = {
        "tag_name" : "",
        "f_name" : ""
    }


    store_json = []
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for _ in csv_reader:
                # print(_) # ['slug', 'name']
                # break
                cpy_json = required_json.copy()
                cpy_json["tag_name"] = _[0]
                cpy_json["f_name"] = _[1]
                store_json.append(cpy_json)
        
        try:
            with open(json_file_name, 'w',encoding='utf-8') as jsonfile:
                json.dump(store_json, jsonfile, indent=4)
        except Exception as e:
            print(f"Error while storing data {e}")
        
        print("Done copying data into json file")
        
    except Exception as e:
        print(f"Error while opening file {e}")


csv_filename = '../tests/data/topicTags.csv'
json_file_name = './json/tags_list.json'

list_tags_from_csv(csv_filename,json_file_name)