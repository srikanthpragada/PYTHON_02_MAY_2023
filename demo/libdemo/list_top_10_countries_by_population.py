import requests

resp = requests.get("https://restcountries.com/v3.1/all")

# Convert JSON array from response to list[dict]
countries = resp.json()

sorted_countries = sorted(countries, key=lambda c: c['population'], reverse=True)

for c in sorted_countries[:10]:
    name = c['name']['common']
    capital = c.get('capital', ["Unknown"])
    population = c['population']
    print(f"{name:50} {capital[0]:20} {population:10}")
