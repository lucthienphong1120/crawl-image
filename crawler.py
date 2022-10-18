import requests
import bs4 as bs
import urllib.request
import wget
import urllib.parse

banner = """
######## ######## ##     ## ########          #### ##     ##    ###     ######   ######## 
   ##    ##        ##   ##     ##              ##  ###   ###   ## ##   ##    ##  ##       
   ##    ##         ## ##      ##              ##  #### ####  ##   ##  ##        ##       
   ##    ######      ###       ##    #######   ##  ## ### ## ##     ## ##   #### ######   
   ##    ##         ## ##      ##              ##  ##     ## ######### ##    ##  ##       
   ##    ##        ##   ##     ##              ##  ##     ## ##     ## ##    ##  ##       
   ##    ######## ##     ##    ##             #### ##     ## ##     ##  ######   ######## 
"""

print(banner)

search = input('Enter the search term: ')

search = urllib.parse.quote(search)

url = 'https://yandex.com/images/search?text=' + search

opener = urllib.request.build_opener()
opener.add_headers = [{'User-Agent' : 'Mozilla/5.0'}]
urllib.request.install_opener(opener)

raw = requests.get(url).text
soup = bs.BeautifulSoup(raw, 'html.parser')

imgs = soup.find_all('img')

links = []

for img in imgs:
    src = img.get('src')
    # print(src)
    if ('?' not in src or ':' not in src):
        # if ('jpg' in src.lower() or 'png' in src.lower()): query in imgur
        if len(links) >= 10: # query with large system
            break;
        imglink = requests.compat.urljoin(url, src)
        links.append(imglink)

for id, link in enumerate(links):
    # print(id, link)
    name = 'images/' + str(id) + '.png'
    wget.download(link, out=name)

