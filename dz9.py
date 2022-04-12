
class MyError(Exception):
    print('You have to use only Y or N')

# Основная функция вычисления 
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction 
* for multiplication
/ for division
Type:
''')
    while True:
        try:
            number_1 = int(input('Enter your first number: '))
            number_2 = int(input('Enter your second number: '))
        except ValueError: # отлавливаем ошибку типа данных
            print('You have to use only numbers!')
            continue
        if operation == '+':
            print('{} + {} = '.format(number_1, number_2), number_1 + number_2)
            break
        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2), number_1 - number_2)
            break
        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2), number_1 * number_2)
            break
        elif operation == '/':
            try:
                print('{} / {} = '.format(number_1, number_2), number_1 / number_2)
                break
            except ZeroDivisionError as e: # отлавливаем ошибку деления на 0
                print('Cannot be divided by 0')
        else:
            print('You have not typed a valid operator.')
            break
# Функция для повторного вычисления 
def repeat():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    if calc_again == 'Y':
                calculate()
    elif calc_again == 'N':
                print('See you')    
    else:
        print('You have to use only Y or N')
        repeat()
            
# Функция приветсвия 
def welcom():
    print('''
    Welcom to Calculator!!
    ''')

welcom()
calculate()
repeat()