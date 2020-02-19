import requests
from bs4 import BeautifulSoup

url = "https://www.hindustantimes.com/top-news/"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

count = 0

newData = soup.findAll("a",{"class" : "wclink2"})
    
for i in range(len(newData)):
    count = count + 1
    print("\n",count,"-",newData[i].text,"\n")
                                                          

