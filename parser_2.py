import requests
import json

# url = "https://jsonplaceholder.typicode.com/posts/1"
url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)
# http ответ, content - данные, status code(200)
content = response.content
# print(type(content))
json_data = content.decode()
# print(type(json_data))
# print(json_data)
# # чтобы превратить строку в json объект сюреализация
userIdes = json.loads(json_data)
# print(type(userIdes))
# print(userIdes[0:2:])
# print(type(json.loads(json_data)))

for userId in userIdes:
    # print(userId)
    # менеджер контекста
    with open(f'src/dist/data_{userId["id"]}.json', 'w') as file:
        json.dump(userId, file)

    with open('temp/data_%s.json' % userId['id'], 'w') as file:
        # записывает объект в файл
        json.dump(userId, file)
    #     json.dumps(userId)


file_name = 'temp/data_4.json'

with open(file_name, 'r') as file:
    # читает объект напрямую с файла
    json_new_data = json.load(file)
    print(json_new_data)
    print(type(json_new_data))
    # json_data1 = json.loads(file.read())
    # print(json_data1)

