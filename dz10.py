# Task сделать генератор геометрической прогрессии 
def geom_prg(number):
    for i in range(1, number):
        yield i * 3**(i-1) # формула геом прогрессии

g = geom_prg(8)
for i in g:
    print(i)





