import requests

resp = requests.get("https://restcountries.com/v3.1/all")

# Convert JSON array from response to list[dict]
countries = resp.json()

for c in sorted(countries, key=lambda c: c['name']['common']):
    name = c['name']['common']
    capital = c.get('capital', ["Unknown"])
    population = c['population']
    print(f"{name:50} {capital[0]:20} {population:10}")
