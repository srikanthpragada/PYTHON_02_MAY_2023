import requests

code = input("Enter country code :")

resp = requests.get(f"https://restcountries.com/v3.1/alpha/{code}")
if resp.status_code == 404:
    print("Sorry! Invalid Country Code!")
    exit(1)

if resp.status_code != 200:
    print("Sorry! Couldn't get details!")
    exit(2)

country = resp.json()[0]

print(f"Name          {country['name']['common']}")
capitals = country.get('capital', ['Unknown'])
caps = ",".join(capitals)

print(f"Capital       {caps}")
print(f"Region        {country['region']}")

langs = ",".join(country['languages'].values())

print(f"Languages     {langs}")
print(f"Area          {country['area']}")
print(f"Population    {country['population']}")
density = country['population'] / country['area']
print(f"Density       {density:4.0f}")
