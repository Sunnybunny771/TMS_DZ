
# Task 1. Решил выбрать и создать класс часов с атрибутами: "цвет, диаметр и форма"
class Watches:
    def __init__(self, diameter, color, form):
        self.diametr = diameter
        self.color = color
        self.form = form
        
# данный класс будет иметь 4 метода "снять, повесить часы, включить и выключить"
    def hang_up(self):
        return 'watches hanged up!'
    def off(self):
        return 'watches switched OFF'
    def on(self):
        return 'watches switched ON'
    def remove(self):
        return 'watches removed!'
# второй класс наследник электричество
class Electricity:
    def __init__(self):
        pass
        

    def charge_up(self):
        return 'charged up!'
    def discharged(self):
        return 'discharged!'

# третий класс наследник электро часы
class Electro_watches(Watches, Electricity):
    def __init__(self, color_of_numbers, number_font, size, diameter, color, form):
        self.color_of_numbers = color_of_numbers
        self.number_font = number_font
        self.size = size
        super().__init__(diameter, color, form)
        


# c одним методом "установки времени"  
    def install_time(self):
        return f'{self} time installed!'
    
# три объекта "наручные часы", "настенные часы" и "часы будильник"
wall_watches = Watches(
    diameter = '12',
    color = 'white', 
    form = 'circle'
    )

alarm_wathces = Watches(
    diameter = '8',
    color = 'black', 
    form = 'square'
    )

hand_wathces = Electro_watches(
    size = '3',
    color_of_numbers = 'red',
    number_font = 'digital',
    diameter = '2',
    color = 'green',
    form = 'circle',
)

print(Electro_watches.charge_up(hand_wathces))
print(Electro_watches.off(hand_wathces))