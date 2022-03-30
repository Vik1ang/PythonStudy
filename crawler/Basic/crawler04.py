import requests

r = requests.get('https://api.github.com/events')
print(r.text)
print(r.json())
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r)

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r)