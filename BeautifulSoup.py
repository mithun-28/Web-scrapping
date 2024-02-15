from bs4 import BeautifulSoup
import requests

url = 'https://theselfless.org/sustainable-home/' # Enter url of the desired website
response = requests.get(url)
print(response)


data = response.text # Getting Source code of the web page

soup = BeautifulSoup(data,'html.parser') # Parsing the html document to Beautiful Soup

# Extracting all the links in the web page

links = []
tags = soup.find_all('a')
for tag in tags:
    links.append(tag.text)
print(links)

print("---"*30)


# Extracting all the h1 tags from the web page 

head1 = []
h1 = soup.find_all('h1')
for h in h1:
    head1.append(h.text)
print(head1)

print("---"*30)

# Extracting all the h3 tags from the web page 

head3 = []
h3 = soup.find_all('h3')
for h in h3:
    head3.append(h.text)
print(head3)
