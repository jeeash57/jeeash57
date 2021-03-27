import requests
from bs4 import BeautifulSoup as bs

#cite: YouTuber @ CodeWithTomi

Github_user = input('PLease input GitHub user:')
url = 'https://github.com/'+Github_user
response = requests.get(url)
identity = bs(response.content, 'html.parser')
profile_image = identity.find('img', {'alt': 'Avatar'})
print(profile_image)

