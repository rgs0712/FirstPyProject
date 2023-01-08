import requests

from config.Configuration import Configuration

c = Configuration('LOCAL')


response = requests.get(c.url)

print(response.text)

print(c.url)
print(c.user)
print(c.password)
