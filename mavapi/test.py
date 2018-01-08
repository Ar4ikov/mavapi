import requests
data = {'access_token': '26ueJCO8-SkAw-KZj2-nrzJ-0E4vhOW9O8Pa', 'mav_id': '16'}
a = requests.post('https://mav-server.ru/api?getUser', data=data)
a = a.text
print(a)