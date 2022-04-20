
# Основная функция вычисления 
def calculate():
    print('''
    Welcom to Calculator!!
    ''')
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
                print('цуецупцпецпуцпац')
        else:
            print('You have not typed a valid operator.')
            break
                #  для повторного вычисления 
    while True:
        calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
        if calc_again == 'Y':
                    calculate()
                    break
        elif calc_again == 'N':
                    print('See you')
                    break    
        else:
            print('You have to use only Y or N')
            continue

calculate()
