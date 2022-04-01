# Task 1

name = str(input('Введите имя: '))
age = int(input('Введите возраст: '))
if age < 18:
    print('Ваш возраст не подходит')
    
else:

    print('Добро пожаловать ' + name)

# Task 2 

while True:
    name = str(input('Введите имя: '))
    age = int(input('Введите возраст: '))
    if age < 18:
        print('Ваш возраст не подходит')
    
    else:
        print('Добро пожаловать ' + name)

# Task 3. 

print('Твоя задача угадать число методом тыка от 1 до 100 за наименьшее число попыток, удачи')
while True:
    number = int(input('Введите число: '))
    if number == 73:
        print('БИНГО!!!')
        break
    elif 1 <= number <= 30:
        print('Совсем холодно')
        
    elif 31 <= number <= 60:
        print('тепло') 

    elif 61 <= number <=72:
        print('Очень горячо')

    elif 74 <= number <= 85:
        print ('тепло')
    else:
        print('холодно')