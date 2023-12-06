import requests
from datetime import datetime

USERNAME = "alexandrecorcos"
TOKEN = "adsfjaslkdf765dsf7a"
GRAPH_ID = "graph1"

now = datetime.now()
TODAY = now.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_running_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}



graph_update = {
    "quantity": "5"
}

choice = input("What you want to do? (I)nsert/(U)pdate/(D)elete: ").lower().strip()

if choice == "insert" or choice == "i":

    graph_insert = {
        "date": TODAY,
        "quantity": input("How many kilometers did you run today? ")
    }

    response = requests.post(url=graph_running_endpoint, json=graph_insert, headers=headers)
    print(response.text)
elif choice == "update" or choice == "u":
    graph_update = {
        "quantity": input("How many kilometers did you run today? ")
    }

    response = requests.put(url=graph_update_endpoint, json=graph_update, headers=headers)
    print(response.text)
elif choice == "delete" or choice == "d":
    response = requests.delete(url=graph_update_endpoint, json=graph_update, headers=headers)
    print(response.text)
else:
    print("Choose a valid option")


# POST
# response = requests.post(url=graph_running_endpoint, json=graph_insert, headers=headers)
# print(response.text)

# UPDATE
# response = requests.put(url=graph_update_endpoint, json=graph_update, headers=headers)
# print(response.text)

# DELETE
# response = requests.delete(url=graph_update_endpoint, json=graph_update, headers=headers)
# print(response.text)