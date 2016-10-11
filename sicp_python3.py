import requests
from bs4 import BeautifulSoup
import html2text

url = 'http://www.composingprograms.com/'
r = requests.get(url)

raw_html = r.text
soup = BeautifulSoup(raw_html, 'lxml')
links = soup.select('a[href^="./pages/"]')

pages = []
for link in links:
    pages.append(url+link.get('href')[2:])

for link in pages:
    rq = requests.get(link)
    html = rq.text
    s = BeautifulSoup(html, 'lxml')
    contents = s.select('.inner-content')
    with open('sicp-python3.md', encoding='utf-8', mode='a') as sicp:
        sicp.write(html2text.html2text(str(contents[0]).replace('Â', '').replace('â', '').replace('../img', url+'img')))

