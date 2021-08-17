import requests


BASE = "http://127.0.0.1:5000/"

# Retrivied data:
data = [{"name": "teste", "views": 1550, "likes": 10},
        {"name": "xuxa", "views": 160, "likes": 1610}, 
        {"name": "patata", "views": 180, "likes": 110},
        {"name": "carrossel", "views": 210, "likes": 16660}] 

for i in range(len(data)):
    # Inserting data into my API:
    response = requests.put(
        BASE + f"video/{str(i)}", data[i])
    print(response.json())

input()

# Deleting data:
response = requests.delete(BASE + "video/0")
print(response)

input()

# Quering data from API:
response = requests.get(BASE + "video/2")
print(response.json())
