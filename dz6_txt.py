name = input('Имя: ')
age = input('Возвраст: ')
text = f' Hi, {name}, are you {age} years old?'

with open('story.txt', 'w') as story:
    story.write(text)



with open('story.txt') as storry:
    for line in storry:
        print(line)


