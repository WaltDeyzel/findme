from bs4 import BeautifulSoup
import requests 
import webbrowser

find = "Handford"#str(input())
found = False
#while(found == False):
site = "https://en.wikipedia.org/wiki/Where%27s_Wally%3F"

page = requests.get(site)

soup = BeautifulSoup(page.content, 'html.parser')
texts = soup.findAll(text=True)
links = soup.find_all('a')

#webbrowser.open(site)
for text in texts:
    for word in text.split():
        if word == find:
            print('found')
            found = True
            break
    if(found):
        break

if found == False:
    print('Nope')