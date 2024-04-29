import requests
import json

var_dict1 = dict(age=24, Name="Ally")  # создание словаря
print(var_dict1)

var_dict2 = {'age': 24, "Name": "Ally"}  # создание словаря
print(var_dict2)

var_dict3 = {}  # создание словаря
var_dict3["Age"] = 24
var_dict3["Name"] = "Ally"
print(var_dict3)

var_dict4 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": {
        "streetAddress": "Московское ш., 101, кв.101",
        "city": "Ленинград",
        "postalCode": 101101
    },
    "phoneNumbers": [
        "812 123-1234",
        "916 123-4567"
    ]
}
print(type(var_dict4))

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
json_data = response.content.decode()
print(json_data)
# print(response)

with open("data_json", "x") as outfile:
    json.dump({
        "Age": 100,
        "name": "mkyong.com",
        "messages": ["msg 1", "msg 2", "msg 3"]
    }, outfile)

with open('new_file1.json', 'a') as file:
    json.dump(json_data, file)
    # json.dumps()

# with open('src/dist/new_file1.json', 'r') as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
    # json.load()
    # json.loads()


