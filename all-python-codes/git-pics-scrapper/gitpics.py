# I hope you read through the readme file, if you did not please go back and check through it.

import requests
from bs4 import BeautifulSoup as bs

# input for a github user
github_user = input('Enter a github user: ')
# concatenate the input with github url
url = 'https://github.com/'+github_user
#Request for the url
r = requests.get(url)
#use BeautifulSoup to clean and parse the url
soup = bs(r.content, 'html.parser')
#parse and seatch of the url that renders the github profile image
profile_img = soup.find('img', {'alt' : 'Avatar'})['src']
#print out the image. The print out would only give you the url to the github profile image
print(profile_img)
