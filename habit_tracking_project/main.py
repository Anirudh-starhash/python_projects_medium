import requests
from datetime import datetime

pixela_end_point="https://pixe.la/v1/users"
username="anirudh123"
token="ygfuh78iuyfdch"

user_params={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_end_point,json=user_params)
# print(response.text)

graph_end_point=f"{pixela_end_point}/{username}/graphs"

graph_params={
    "id":"graph1",
    "name":"Cycling graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":token
}

# response=requests.post(url=graph_end_point,json=graph_params,headers=headers)
# print(response.text)

pixel_creation_end_point=f"{graph_end_point}/{graph_params["id"]}"

# today=datetime.now()
today=datetime(year=2024,month=5,day=20)
print(today.strftime("%Y%m%d"))
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"15"
}

# response=requests.post(url=pixel_creation_end_point,json=pixel_data,headers=headers)
# print(response.text)

update_end_point=f"{pixel_creation_end_point}/{today.strftime('%Y%m%d')}"
delete_end_point=f"{pixel_creation_end_point}/{today.strftime('%Y%m%d')}"

update_pixel={
    'quantity':'9.5'
}
response=requests.put(url=update_end_point,json=update_pixel,headers=headers)
print(response.text)

# response=requests.delete(url=delete_end_point,headers=headers)
# print(response.text)
