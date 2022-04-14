# Task сделать генератор геометрической прогрессии 
def geom_prg(q):
    for i in range(1,9):
        yield i * q**(i-1) # формула геом прогрессии

g = geom_prg(3)
for i in g:
    print(i)





