
# Task 1 Сделать функцию 
"""В задании принял решение сделать элементарную функцию , так как пытался придумать и написать что-то посложнее и в итоге несколько
раз сломал себе голову"""
def sum(x, y: int)-> int:
     c = x + y
     return c 
print(sum(3, 78))
 

# TASK 2 Сделать Lambda функцию
"""Тут также не стал усложнять решил сделать Lambda функцию на основе обычной"""
c = lambda x, y: x + y / 4 + (23**3) 
print(c(12, 23))



# TASK 3 Создать декорратор 
"""Изначальная цель была сделать один декоратор, после того как получилось 
его сделать захотелось поиграть со вложенностью функций. Сделал два """

def greetings_decorator(func):
    def wrapper(*args,**kwargs):
        print('Я декоратор, который начинается с этой секунды')
        func(*args, **kwargs)
        print('К сожалению мне тоже надо идти')
    return wrapper

def greetings_decorato_2(func):
    def wrapper(*args,**kwargs):
        print('Я тут тоже есть, вообще-то')
        func(*args,**kwargs)
        print('Мне пора,я ушел')
    return wrapper


"""Хотел сделать декоратор для прибавления 5-и к конечному результату,
 но у меня не сходились типы данных выдовало ошибку  """

def sum(x, y: int)-> int:
    c = x + y
    print(c)

sum = greetings_decorator(greetings_decorato_2(sum))
sum(234, 24)



