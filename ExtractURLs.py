import requests
from string import punctuation
from bs4 import BeautifulSoup 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
import time

#Create Lists having URLs of all dates of a Month  
#----------------------------------------

List_of_BP_URLs=[] 
def CreatURL(PG_URL,Month, EndRange):
  
  for day in range(1,EndRange):
      if day<10:
        day="0"+str(day)
      else:
        day=str(day)
      FP_CMP_URL=PG_URL+Month+day+"/"
      List_of_BP_URLs.append(FP_CMP_URL)
  
#Function to Etract all the URLs of a News on a page
def ExtractLinks_FP(dt, URL):
    Req=requests.get(URL)
    cntnt=Req.text
    #print(cntnt)
    NewSoup=BeautifulSoup(cntnt, 'html.parser')
    data=NewSoup.find_all('a', attrs={'class':'story__link'})
    for Sub_Link in data:
        Sub_Link_URL=Sub_Link.get('href')
        if Sub_Link_URL.startswith('http'):
            with open("Back_Pages_URLs.csv","a", encoding="utf-8", newline="") as All_CSV:
              All_WRTR=csv.writer(All_CSV)
              All_WRTR.writerow([dt, Sub_Link_URL, Sub_Link.get_text()])
            with open("All_Pages_URLs.csv","a", encoding="utf-8", newline="") as All_CSV1:
              All_WRTR1=csv.writer(All_CSV1)
              All_WRTR1.writerow([dt, Sub_Link_URL, Sub_Link.get_text()])
def ExtractSubLinks (EndRange):
  First_URL=""
  for day in range(1,EndRange):
      First_URL=List_of_BP_URLs[day-1]
      URL_date=First_URL[-11:-1]
      ExtractLinks_FP(URL_date, First_URL)
      time.sleep(0.5)
  List_of_BP_URLs.clear()
#,"https://www.dawn.com/newspaper/lahore/","https://www.dawn.com/newspaper/islamabad/","https://www.dawn.com/newspaper/peshawar/"
All_pages_URLs=["https://www.dawn.com/newspaper/back-page/"]
for Page_URL in All_pages_URLs:
  """Mnth="2019-01-"
  DaysRange=32
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs For Jan Extracted")
  time.sleep(20)
  Mnth="2019-02-"
  DaysRange=29
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for Feb Extracted")
  time.sleep(30)
  Mnth="2019-03-"
  DaysRange=32
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for March Extracted")
  time.sleep(30)
  Mnth="2019-04-"
  DaysRange=31
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for April Extracted")
  time.sleep(30)
  Mnth="2019-05-"
  DaysRange=32
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for May Extracted")
  time.sleep(30)
  Mnth="2019-06-"
  DaysRange=31
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for June Extracted")
  time.sleep(30)
  Mnth="2019-07-"
  DaysRange=32
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for July Extracted")
  time.sleep(30)
  Mnth="2019-08-"
  DaysRange=32
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for Aug Extracted")
  time.sleep(30)"""
  Mnth="2019-09-"
  DaysRange=31
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for Sep Extracted")
  time.sleep(30)
  Mnth="2019-10-"
  DaysRange=32
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for Oct. Extracted")
  time.sleep(30)
  Mnth="2019-11-"
  DaysRange=31
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for Nov Extracted")
  time.sleep(30)
  Mnth="2019-12-"
  DaysRange=32
  CreatURL(Page_URL,Mnth, DaysRange)
  ExtractSubLinks(DaysRange)
  print("All URLs for Dec Extracted")

  