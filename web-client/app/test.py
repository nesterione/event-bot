import requests
r = requests.get(url='http://api.events.nesterione.com/api/v0.1/events')
print( type(r.json()))

