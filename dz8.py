from dataclasses import dataclass

@dataclass
class Cars:
    brand: str
    model: str
    horsepower: int
car_1 = Cars('Audi', 'A3', 243)
car_2 = Cars('LADA', 'Granta', 98)
car_3 = Cars('Mazda', 'CX-9', 189)

@staticmethod
def plus_speeds(x,y,z):
    return x + y + z
#print(plus_speeds(243,98,189))
print(type(car_1))
#@classmethod
#def change_horsepower(cls,):
 #   return cls 

#print(Cars.brand())