# Requests Module in Python
# pip install requests
import requests

# Get Request
response = requests.get(
    "https://codewithharry.com/")
# print(response.headers)
# print(response.text)


# Post Request
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "name": "Suraj",
    "age": 21,
    "body": "I am a good programmer"
}
headers = {
    "content-type": "application/json", "charset": "UTF-8"
}
resp = requests.post(url, headers=headers, json=data)
print(resp.text)
