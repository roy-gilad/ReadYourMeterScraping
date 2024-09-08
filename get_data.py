import requests
import time
token = requests.post(
    url="https://eu-customerportal-api.harmonyencoremdm.com/consumer/login",
    json= {"email":"nadavgil18@gmail.com","pw":"AAAaaa111","deviceId":"270566787934916747718271777073275455358"},
    verify=True,

    headers={"Content-Type":"application/json", "path":"/consumer/login"}
    )

# token = token.json()["token"]
print(token.json()["token"])
time.sleep(5)
data = requests.get(
    url = "https://eu-customerportal-api.harmonyencoremdm.com/consumption/daily/179/2024-09-01/2024-09-07",
    verify=True,
    headers={"X-Access-Token": token.json()["token"]}

)

print(data.json()[-1])