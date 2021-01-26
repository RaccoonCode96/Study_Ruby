import requests
from bs4 import BeautifulSoup
r = requests.get('https://codingeverybody.github.io/scraping_sample/1.html')
print(r.text)
# 패키지 다운 받았음
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title)
print(soup.title.string)

print()

print("Title : {0}".format(soup.title.string))
articles = soup.findAll('div', {'class': 'em'})
# print(articles)
# print(articles[0])
# print(articles[0].text)
print("Articles : {0}".format(articles[0].text))

print()

r = requests.get('https://codingeverybody.github.io/scraping_sample/2.html')
soup = BeautifulSoup(r.text, 'html.parser')
print("Title : {0}".format(soup.title.string))
articles1 = soup.findAll('div', {'class': 'strong'})
print("Articles : {0}".format(articles1[0].text))
