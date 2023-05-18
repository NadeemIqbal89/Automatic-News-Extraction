import requests
from string import punctuation
from bs4 import BeautifulSoup 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
import time
from pandas import *

with open("News/FailURLs.csv") as file_obj:

    reader_obj = csv.reader(file_obj)
    row_count=0
    for row in reader_obj:
       row_count=row_count+1
       if row_count%25==0:
           time.sleep(60)
       NewsId=row[0]
       date=row[1]
       link=row[2]
       Title=row[3]
       try:
            myReq=requests.get(link)
            sp=BeautifulSoup(myReq.content, "html.parser")
            outDiv=sp.find('div', class_='template__main')
            story=outDiv.find('div', class_='story__content')
            text=""
            for p_tag in story.find_all('p'):
                text=text+" "+p_tag.get_text()
            with open("News/Terror/Terror_News.csv", "a",newline="") as FP_CSV:
                CSV_WRTR=csv.writer(FP_CSV)               
                CSV_WRTR.writerow([NewsId, date, link, Title, text])
                print("Writing text for the URL: ", link)

            
       except Exception as ex:

            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            with open("News/FailURLs1.csv","a", newline="") as Fail_CSV:
                Fail_CSV_WRTR=csv.writer(Fail_CSV)
                Fail_CSV_WRTR.writerow([NewsId,date, link,Title,message])
       continue   
print("All News Extracted")