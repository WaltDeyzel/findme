from bs4 import BeautifulSoup
import requests 
import webbrowser
from random import randint
import time

find = "Handford"#str(input())
found = False
link_count = 5

wiki = "/wiki/Where%27s_Wally%3F"
basis = "https://en.wikipedia.org"
while(link_count > 0):
    site = basis + wiki

    page = requests.get(site)

    soup = BeautifulSoup(page.content, 'html.parser')
    texts = soup.findAll(text=True)
    links = soup.find_all('a', href=True)

    #webbrowser.open(site)
    for text in texts:
        for word in text.split():
            if word == find:
                print('found', word)
                found = True
                break
        if(found):
            break

    random_links = []
    for link in links:
        if(str(link['href'])[0:6] == '/wiki/'):
            if(link['href'][6:14] !='Category' and link['href'][6:12] !='Where'):
                random_links.append(link['href'])
        
    index = randint(0, len(random_links))
    wiki = basis+random_links[index]
    print(wiki)
    webbrowser.open(wiki)
    time.sleep(3)
    link_count -= 1