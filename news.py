import requests
from bs4 import BeautifulSoup
import time
import pandas

url = "https://news.google.com/search?q=corporate%20news&hl=en-US&gl=US&ceid=US%3Aen"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}

# Introduce a delay of 2 seconds before sending the request
time.sleep(2)


response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

itemlist_1 = soup.find_all("div", class_="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc")
itemlist_2 = soup.find_all("div", class_="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf")

itemlist = itemlist_1 + itemlist_2

list_rest=[]

for item in itemlist:
    dataframe={}
    nameOfClass = item.find("div",class_="xrnccd")
    dataframe['Company_Name'] = nameOfClass.find('a',class_="wEwyrc").text.strip()    
    dataframe['News'] = nameOfClass.find('a',class_="DY5T1d RZIKme").text.strip()
    dataframe['Date'] = nameOfClass.find('time')['datetime']
    list_rest.append(dataframe)

df=pandas.DataFrame(list_rest)
df.to_csv("Corporate_News.csv",index=False)
print('Corporate_News.csv stored successfully')
