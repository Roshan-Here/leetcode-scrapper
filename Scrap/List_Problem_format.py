import json
from leetscrape import GetQuestion

def fall_guy(json_file_name,required_json_file_name):
    """
    -read json file
    -filter non paid items
    -find all the question details
    -find all the examples
    -add all data into required_json fomat
    -append data to an arary
    -add the completed data to required json file
    """
    with open(json_file_name, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)

    filtered_items = [item for item in json_data if item["paidOnly"] == "False"]
    complete_data = []
    error_data_list = []
    Error_Fetching_data_list = []
    for items in filtered_items:
        titelslug = items["titleSlug"]
        try:
            # print(titelslug)
            question = GetQuestion(titleSlug=titelslug).scrape()
            # time.sleep(1)
            Qid = question.QID
            Title = question.title
            difficulty = question.difficulty
            tags = question.topics
            # q = str(question)
            required_json_data = {
                "id":Qid,
                "Title": Title,
                "slug": titelslug,
                "difficulty": difficulty,
                "tags": tags
            }
            # print(required_json_data)
            complete_data.append(required_json_data)
            print(f'Appended {titelslug}')
            # break
        except Exception as e:
            Error_Fetching_data_list.append(titelslug)
            print(f"Err while fetching data : {e}")
    try:
        with open(required_json_file_name, 'w',encoding='utf-8') as jsonfile:
            json.dump(complete_data, jsonfile, indent=4)
    
    except Exception as e:
        print("Eroor while coping data to json")
        
    print(f"Done : Error_Fetching_data_list : {Error_Fetching_data_list}")

json_file_name = './json/questions.json'
required_json_file_name = './json/List_Table_format.json'

fall_guy(json_file_name,required_json_file_name)
