import json

name = input('Inter name: ')
age = input(' inter age: ')
users_data =[]
dict = [
    {
'name': name,
'age': age
}
]
users_data.append(dict)
with open('data.json', 'w') as users_file:
    json.dump(users_data, users_file)

print(users_data)