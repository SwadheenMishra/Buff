import requests

d = requests.get("https://192.168.2.176").text

print(d)
