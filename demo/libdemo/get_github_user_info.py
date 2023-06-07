import requests

user = "gvanrossum"
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = resp.json()  # Convert JSON response to dict
# print(details['name'])
# print(details['company'])
# print(details['location'])

for key, value in details.items():
    print(f"{key:25} - {value}")
