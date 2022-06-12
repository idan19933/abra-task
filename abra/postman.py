import requests
import json

url = "http://127.0.0.1:8000/chat/"

payload = json.dumps({
  "id": 10,
  "subject": "ss",
  "message": "ss",
  "creation_date": "2022-06-09T11:44:00Z",
  "sender": 1,
  "receiver": 3
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


