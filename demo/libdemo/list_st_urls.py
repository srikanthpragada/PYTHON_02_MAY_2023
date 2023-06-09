from bs4 import BeautifulSoup
import requests

website = "http://www.srikanthtechnologies.com"
resp = requests.get(website)
bs = BeautifulSoup(resp.text, 'html.parser')
count = 0
for a in bs.find_all("a"):
    href = a['href']
    if href == "#":
        continue

    if not href.startswith("http"):
        href = website + "/" + href
    count += 1
    print(href)

print(f"Count = {count}")


