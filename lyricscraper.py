import requests
from bs4 import BeautifulSoup
from csv import writer

songlist = []
songLinks = []
artAlbums = {}

#gets user input for a specific artist and decompiles it in order to request the link
artist = input("Enter an Artist: ")

firstL = artist[0]
artist = artist.replace(" ", '')
artist.lower()


artresponse = requests.get('https://www.azlyrics.com/'+firstL+"/"+artist+'.html')
soup1 = BeautifulSoup(artresponse.text, 'html.parser')
albums = soup1.find_all(class_='album')

for al in albums:
    if al.find('b') == None:
        break
    artAlbums.update({al.find('b').get_text() : []}) #create a dictionary for each album
print (artAlbums)


#goes to the album div and adds all song links to a list 
for link in soup1.find_all('div', attrs={'id' : 'listAlbum'}):
    for a in link.find_all('a'):
        songLinks.append('https://www.azlyrics.com' + a.get('href')[2:])

#print(songLinks)


#this ended up locking me out of the site becuase of too many requests, use with caution or vpn
'''for link in songLinks: #for each link
    response = requests.get(link) #request the link
    soup2 = BeautifulSoup(response.text,'html.parser')
    posts = soup2.find_all(class_='col-xs-12 col-lg-8 text-center')
    for post in posts:
        lyrics = post.find_all('div')[6].get_text()
        print(lyrics)'''
         






#with open('posts.csv','w') as csv_file:
 #   csv_writer = writer(csv_file)
  #  headers = ['Title', 'Link']
   # csv_writer.writerow(headers)





