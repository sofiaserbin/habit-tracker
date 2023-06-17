import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "3094i309ujrfiundk3"
USERNAME = "sofiaserbina"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
update_endpoint = f"{graph_endpoint}/graph1"
delete_endpoint = f"{graph_endpoint}/graph1/{today.strftime('%Y%m%d')}"

update_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many  pages have you read today? "),
}

response=requests.post(url=update_endpoint, json=update_config, headers=headers)
# response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
