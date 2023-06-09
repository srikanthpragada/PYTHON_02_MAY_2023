from bs4 import BeautifulSoup
import requests

website = "http://www.srikanthtechnologies.com"
resp = requests.get(website)
bs = BeautifulSoup(resp.text, 'html.parser')

table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")

for row in rows[1:]:
    cols = row.find_all("td")
    name = cols[1].text
    stdate = cols[3].text
    print(f"{name:50}  {stdate:10}")

