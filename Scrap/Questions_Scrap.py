from leetscrape import GetQuestionsList
import os

def scrape_leetcode_to_csv():
    """
        Scrap all the questions as csv
    """
    ls = GetQuestionsList()
    ls.scrape()  # Scrape the list of questions
    os.makedirs("../tests/data/")
    ls.to_csv(directory="../tests/data/")
    print("to csv done.")    
    
scrape_leetcode_to_csv()