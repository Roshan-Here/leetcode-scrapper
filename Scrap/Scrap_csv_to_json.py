import csv,json

json_format = {
    "QID":"",
    "title":"",
    "titleSlug":"",
    "difficulty":"",
    "acceptanceRate":"",
    "paidOnly"  :"",
    "topicTags" :"",
    "categorySlug" :"",
}

def csv_to_json(filename,json_file_name):
    """ 
    Convert Questions-csv to json format
    """
    json_data = []
    
    with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # this is how sample data looks.
            # ['1', 'Two Sum', 'two-sum', 'Easy', '52.761508793067065', 'False', 'array,hash-table', 'algorithms']
            # print(row)
            json_cpy = json_format.copy()
            json_cpy['QID'] = row[0] 
            json_cpy['title'] = row[1] 
            json_cpy['titleSlug'] = row[2] 
            json_cpy['difficulty'] = row[3] 
            json_cpy['acceptanceRate'] = row[4] 
            json_cpy['paidOnly'] = row[5] 
            json_cpy['topicTags'] = row[6] 
            json_cpy['categorySlug'] = row[7] 
            json_data.append(json_cpy)
            # break
    # print(json_data)

    # copying data to json file
    with open(json_file_name, 'w',encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)
    print("Done copying data into json file")

csv_filename = '../tests/data/questions.csv'
json_file_name = './json/questions.json'


csv_to_json(csv_filename,json_file_name)