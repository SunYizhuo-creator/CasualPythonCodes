import requests
import jieba
from bs4 import BeautifulSoup
from pyecharts.charts import WordCloud

url = "https://nocturne-spider.baicizhan.com/2020/09/02/coco/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)

html = response.text

soup = BeautifulSoup(html, "lxml")

content_all = soup.find_all("em")
wordList = []
for content in content_all:
    contentString = content.string
    words = list(jieba.cut(contentString))
    wordList += words

wordDict = {}
wordCloud = WordCloud()
for word in wordList:
    if len(word) == 1:
        continue
    if word in wordDict:
        wordDict[word] += 1

    else:
        wordDict[word] = 1
wordCloud.add(series_name="", data_pair=wordDict.items(), word_size_range=[30, 70], width=800, height=500)
wordCloud.render("dream.html")
print("success")
