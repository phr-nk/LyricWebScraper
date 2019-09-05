import requests
from bs4 import BeautifulSoup
import traceback
from itertools import cycle



#this code gets a pool of random proxy servers in order to disguise scraping
url =  'https://httpbin.org/ip'

def get_proxies():

    proxyresponse = requests.get('https://free-proxy-list.net')

    proxysoup = BeautifulSoup(proxyresponse.text, 'html.parser')

    tables = proxysoup.find('table', attrs={"id" :'proxylisttable'})

    #proxies = []
    proxies = set()

    for table in tables:
        for t in table.find_all('tr'):
            http = t.find('td',attrs={'class' : 'hx'})
            elite = t.find_all('td',attrs={'':''})[4:5] #find if it is an elite proxy
            if len(elite) == 0: #see if it is an empty list
                break

            if http:
                if http.text == 'yes' and elite[0].text == 'elite proxy': #determine if it is http and an elite proxy
                    ip = t.find('td').get_text()#this should find all the IP's that are http
                    port = t.find_all('td')[1].get_text()
                    #proxies.append(ip + ':' + port)
                    proxies.add(ip + ':' + port)
                    
    return(proxies)

proxies = get_proxies()
proxy_pool = cycle(proxies)


#print(proxies)

for i in range(1,11):
    #get proxy from pool
    proxy = next(proxy_pool)
    print('Request #%d'%i)
    try:
        response = requests.get(url, proxies={'https': proxy,'http' : proxy})
        print(response.json())
    except:
        print("Skipping. Connection Error")
  
