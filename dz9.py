


def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2), number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2), number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2), number_1 * number_2)
    elif operation == '/':
            try:
                print('{} / {} = '.format(number_1, number_2), number_1 / number_2)
            except ZeroDivisionError as e:
                print('Cannot be divided by 0')
    else:
        print('You have not typed a valid operator, please run the program again.')

def repeat():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    if calc_again == 'Y':
            calculate()
    elif calc_again == 'N':
            print('see you')
    else:
        repeat()
def welcom():
    print('''
    Welcom to Calculator!!
    ''')

welcom()
calculate()
repeat()