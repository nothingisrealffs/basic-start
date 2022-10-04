import requests
from bs4 import BeautifulSoup
import re
page = requests.get(
    "https://www.newegg.com/p/pl?d=msi+rtx+3070")
soup = BeautifulSoup(page.content, 'html.parser')

all_links = []
false_links = []

links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    y = re.search("^https://www.newegg.com/msi",href)
    if y:
        false_links.append(href)
    else:
        pass
    if href == '':
        pass
    else:
        y = re.search("^https://www.newegg.com/msi",href)
        all_links.append({href:y})
#print(all_links)
for x in false_links:
    print(x)
