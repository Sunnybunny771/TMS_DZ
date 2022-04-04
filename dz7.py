
# Task 1. Решил выбрать и создать класс часов с атрибутами: "цвет, диаметр и форма"
class wathces:
    def __init__(self, diameter, color, form,):
        self.diametr = diameter
        self.color = color
        self.form = form
# данный класс будет иметь 4 метода "снять, повесить часы, включить и выключить"
    def hang_up(self):
        return 'Wathces hanged up!'
    def off(self):
        return 'Wathces OFF'
    def on(self):
        return 'Wathces ON'
    def remove(self):
        return 'Wathces removed!'
# второй класс наследник электричество
class electricity:
    def __init__(self, charge, discharged):
        self.charge = charge
        self.discharged = discharged

    def charge_up(self):
        return 'charged up!'
    def discharged(self):
        return 'discharged!'

# третий класс наследник электро часы
class electro_wathces(wathces, electricity):
    def __init__(self,diameter, color, form, color_of_numbers, number_font, size, charge, discharged):
        self.color_of_numbers = color_of_numbers
        self.number_font = number_font
        self.size = size
        super().__init__(diameter,color, form)
        super().__init__(charge, discharged)


# c одним методом "установки времени"  
    def install_time(self):
        return f'{self} time installed!'
    
# три объекта "наручные часы", "настенные часы" и "часы будильник"
wall_wathces = wathces(
    diameter = '12',
    color = 'white', 
    form = 'circle',
    )

alarm_wathces = wathces(
    diameter = '8',
    color = 'black', 
    form = 'square',
    )

hand_wathces = electro_wathces(
    size = '3',
    color_of_numbers = 'red',
    number_font = 'digital',
    diameter= '2',
    color = 'blue',
    form = 'digital',
    charge = '24%',
    discharged = '40%'    


)

#print(wall_wathces.diametr)
#print(wall_wathces.color)
#print(wall_wathces.form)

#print(wall_wathces.remove())
#print(wall_wathces.hang_up())

#print(alarm_wathces.diametr)
#print(alarm_wathces.color)
#print(alarm_wathces.form)

#print(hand_wathces.color_of_numbers)
#print(hand_wathces.number_font)
#print(hand_wathces.size)

#print(electro_wathces.hang_up(wathces))

#print(electro_wathces.install_time('10:23'))

#print(electro_wathces.remove(wathces))
#print(electro_wathces.off(wathces))

print(electricity.discharged)