from bs4 import BeautifulSoup
import requests 
import webbrowser
from random import randint
import time

find = str(input(" Find ? :"))
found = False
link_count = 0
limit = 1000
words_looked_up = 0

wiki = "/wiki/Where%27s_Wally%3F"
basis = "https://en.wikipedia.org"

def cleanWord(word):
    word = word.lower()
    word = word.replace('%', '')
    word = word.replace(',', '')
    word = word.replace('.', '')
    word = word.replace('?', '')
    word = word.replace(':', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    return word

def linkFilter(link):
    if(link[6:14] =='Category'):
        return False
    if(link[6:11] =='Where'):
        return False
    if(link[6:10] == 'Help'):
        return False
    if(link[6:15] == 'Wikipedia'):
        return False
    if(link[6:13] == 'Special'):
        return False
    if(link[6:10] == 'User'):
        return False                    
    if(link[6:10] == 'File'):
        return False
    if(link[6:12] == 'Portal'):
        return False 
    if(link[6:9] == 'ISO'):
        return False 
    if(link[6:9] == 'URL'):
        return False  
    if(link[6:15] == 'Copyright'):
        return False                             
    else:
        return True

backup = []

while(link_count < limit and found == False):
  
    site = basis + wiki
    time.sleep(1)
    #REQUEST PAGE
    page = requests.get(site)

    soup = BeautifulSoup(page.content, 'html.parser')
    #FIND ALL TEXT ON SCREEN
    texts_on_screen = soup.findAll(text=True)
    #FINE ALL LINKS ON SCREEN.
    links = soup.find_all('a', href=True)
    
    for sentence in texts_on_screen:
        for word in sentence.split():
            words_looked_up += 1
            if(cleanWord(word) == find):
                found = True
                time.sleep(1)
                webbrowser.open(site)
                print('found', word)
                print(link_count, 'Links later...', words_looked_up)
                break
        if(found):
            break
    if found:
        break

    random_links = []
    #FILTER LINKS TO BE JUST WIKI PAGES
    for link in links:
        if(str(link['href'])[0:6] == '/wiki/'):
            if(linkFilter(link['href'])):
                random_links.append(str(link['href']))
    if(len(random_links) == 0):
        random_links = backup
    else:
        backup = random_links

    #SELECT RANDOM LINK IN RANDOM LINKS LIST
    index = randint(0, len(random_links))
    #THAT LINK IS THE NEW WIKIPEDIA PAGE
    try:
        wiki = random_links[index]
    except:
        print("No links found", site, len(random_links))
        break
    #DISPLAY WIKI AND NUMBER OF LINKS ON PAGE
    print(wiki, len(random_links))
    
    link_count += 1

if(found == False):
    print('The word clearly does not exist')
print('DONE')

