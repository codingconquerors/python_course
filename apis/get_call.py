import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}")