#import json

#name = input('Введите имя: ')
#age = input('Введите возраст: ')
#with open ('data.json', 'w') as users:
 #   user_info = json.dumps(name)
  #  user_info = json.dumps(age)



import csv

with open('data.csv', 'a', newline='') as info_users:

    name = input('Inter your name: ')
    age = input('Inter your age: ')
    print('successful registrated')
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(info_users, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'name': name, 'age': age})
