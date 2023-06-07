
import requests

resp = requests.get("http://worldtimeapi.org/api/timezone/Asia/Dubai")
print(resp.status_code)
result = resp.json()    # Convert JSON response to dict
print(result['datetime'])
