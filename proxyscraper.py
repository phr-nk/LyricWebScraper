import requests
from bs4 import BeautifulSoup

#this code gets a pool of random proxy servers in order to disguise scraping

def get_proxies():

    proxyresponse = requests.get('https://free-proxy-list.net')

    proxysoup = BeautifulSoup(proxyresponse.text, 'html.parser')

    tables = proxysoup.find('table', attrs={"id" :'proxylisttable'})

    proxies = set()

    for table in tables:
        for t in table.find_all('tr'):
            http = t.find('td',attrs={'class' : 'hx'})
            if http:
                if http.text == 'yes':
                    ip = t.find('td').get_text()#this should find all the IP's that are http
                    port = t.find_all('td')[1].get_text()
                    proxies.add(ip + ':' + port)
    return(proxies)
    
proxies = get_proxies()
print(proxies)
