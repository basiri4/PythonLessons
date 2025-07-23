class Transport:

   def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage


Autobus = Transport("Renaul Logan", 180, 12)

print(f"Название автомобиля: {Autobus.name} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}")

# class Human(object):
#     name = "Ivan"
#     heigth = 175
#     age = 25

#     def __init__(self, n, h, a):
#         self.name = n
#         self.heigth = h
#         self.age = a

#     def hello_there(self):
#         print(f'Hello there! My name is {self.name} and i am {self.age} years old')

#     def older(self):
#         self.age += 5
#         print(f'I am now {self.age} years old! WTF?')


# hum1 = Human("Babka", 171, 33)
# hum2 = Human("Dedka", 168, 31)

# print(hum1.age)
# print(hum2.age)
# print(hum1.heigth)
# print(hum2.heigth)
# print(hum1.name)
# print(hum2.name)

# hum1.hello_there()
# hum1.older()

