import os,json,time,re
from leetscrape import GetQuestion

def clean_data(text, label):
    return re.sub(fr'^\*\*{label}\**:?\s*', '', text, flags=re.IGNORECASE).strip()
     
def doing_crazy_shit(text, title_slug):
    """ To find the Example of each text

    Args:
        text (string): Statemet to extract data from
        title_slug (string): Title-slug of text data

    Returns:
        array : containg each examples
    """
    patterns = [
        re.compile(
            r"\*\*Example \d+:\*\*\s*"
            r"!?\[.*?\]\(.*?\)?\s*"
            r"```\s*"
            r"\*\*Input\**:?\s*(.*?)\s*"
            r"\*\*Output\**:?\s*(.*?)\s*"
            r"(?:\*\*Explanation\**:?\s*(.*?))?\s*"
            r"```",
            re.DOTALL
        ),
        re.compile(
            r"\*\*Example \d+:\*\*\s*"
            r"```"
            r"\s*\*\*Input\**:?\s*(.*?)"
            r"\s*\*\*Output\**:?\s*(.*?)"
            r"(?:\s*\*\*Explanation\**:?\s*(.*?))?"
            r"\s*```",
            re.DOTALL
        ),
        re.compile(
            r"\*\*Example \d+:\*\*\s*"
            r"(\*\*Input\**:?[\s\S]*?)"
            r"(\*\*Output\**:?[\s\S]*?)"
            r"(\*\*Explanation\**:?[\s\S]*?)?"
            r"(?=\*\*Example|\Z)",
            re.DOTALL
        )
    ]
        
    for pattern in patterns:
        matches = pattern.findall(text)
        if matches:
            examples = []
            for match in matches:
                input_text = clean_data(match[0], 'Input')
                output_text = clean_data(match[1], 'Output')
                explanation_text = clean_data(match[2], 'Explanation') if len(match) > 2 and match[2] else None
                
                example = {
                    'Input': input_text,
                    'Output': output_text,
                    'Explanation': explanation_text
                }
                examples.append(example)
            return examples
    print(f"No examples found for Titleslug: {title_slug}")
    # exit()
    return []


def find_description(ques):
    """
        description part
    """
    lines = ques.strip().split('\n')

    # Find the index of the line starting with '**Example'
    example_start_index = lines.index(next(line for line in lines if line.startswith('**Example')))

    # Extract the problem description lines and remove asterisks
    problem_description = '\n'.join(line.strip('*') for line in lines[1:example_start_index])
    return problem_description


def fall_guy(json_file_name,required_json_file_name,Error_json_data_fname):
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
            Title = question.title
            difficulty = question.difficulty
            # q = str(question)
            ques = f"""{question}"""
            problem_description = find_description(ques)
            example_data = doing_crazy_shit(ques, titelslug)
            if not example_data:
                print(f'############# Not Appending {titelslug} ############ ')
                error_data_list.append(titelslug)
                continue
            required_json_data = {
                "Title": Title,
                "slug": titelslug,
                "description": problem_description,
                "difficulty": difficulty,
                "examples": example_data
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
        
        with open(Error_json_data_fname, 'w',encoding='utf-8') as jsonfile:
            json.dump(error_data_list, jsonfile, indent=4)
    
    except Exception as e:
        print("Eroor while coping data to json")
        
    print(f"Done : Error_Fetching_data_list : {Error_Fetching_data_list}")

json_file_name = './json/questions.json'
required_json_file_name = './json/required_format.json'
Error_json_data_fname = './json/Error_data.json'

fall_guy(json_file_name,required_json_file_name,Error_json_data_fname)


########### final errored list while fetching
# Done : Error_Fetching_data_list : ['merge-intervals', 'longest-increasing-subsequence', 'string-compression', 'maximum-length-of-repeated-subarray', 'consecutive-characters', 'left-and-right-sum-differences', 'find-the-losers-of-the-circular-game', 'neighboring-bitwise-xor', 'minimum-sum-of-values-by-dividing-array', 'find-subarray-with-bitwise-and-closest-to-k']