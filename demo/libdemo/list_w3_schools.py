from bs4 import BeautifulSoup
import requests

website = "https://www.w3schools.com"
resp = requests.get(website)
bs = BeautifulSoup(resp.text, 'html.parser')
count = 0
for a in bs.find_all("a"):
    href = a['href']
    if href == "#":
        continue

    if not href.startswith("http"):
        if not href.startswith("/"):
            href = website + "/" + href
        else:
            href = website + href

    count += 1
    print(href)

print(f"Count = {count}")
