import requests
from datetime import  datetime

#************************by using POST request we can send data to a server to create or process something.**************************

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "soeigfjsoiesdfpsfdigf"
USERNAME = "asteroid"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json = user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph2",
    "name": "Daily cycling",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)


#************************by using PUT request we can update the previous request**************************

# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{pixel_data["date"]}"
#
# pixel_update_config = {
#     "quantity": "2.2"
# }

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

#************************by using DELETE request we can delete the previous request**************************


# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{pixel_data["date"]}"

# response = requests.delete(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)