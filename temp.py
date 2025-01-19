import requests
import json

url = "https://dleitiop.xyz/h2h/p2p"
m_token = "e727eeefef11b6249b043f9d9de253d7"
body = {
    "merchant_id": 160,    
    "merchant_token": "e727eeefef11b6249b043f9d9de253d7",  
    "ip": "34753",   
    "amount": "10",  
    "merchant_order": "45361",   
    "callback_url": "https://callback_url/",                                                  
}
z = json.dumps(body)
headers = {"Content-Type": "application/json"}

# print(z)
temp = requests.post(url=url,data=json.dumps(body),headers=headers)
print(temp == "arr")
# z=temp.json()
# print(z['status'])
# print(temp.json())