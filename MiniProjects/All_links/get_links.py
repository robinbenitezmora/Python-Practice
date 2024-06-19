import request as rq
from bs4 import BeautifulSoup

url = imput('Enter Link: ')
if ('https' or 'http') in url:
    data = rq.get(url)
else:
    data = rq.get('https://' + url)

soup = BeautifulSoup(data.text, 'html.parser')
links = []

for link in soup.find_all('a'):
    links.append(link.get('href'))

# Writing the output to a file (myLinks.txt) instead of stdout
# You can change 'a' to 'w' to overwrite the files each time
with open('myLinks.txt', 'a') as saved:
    for link in links:
        saved.write(link + '\n')
print('Links saved to myLinks.txt')

