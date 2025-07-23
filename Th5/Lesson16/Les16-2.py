class Turtle(object):
    x = 0
    y = 0
    s = 1
    
    def go_up(self):
        self.y += self.s
        print(f'Вы на позиции х={self.x} y={self.y}')

    def go_down(self):
        self.y -= self.s
        print(f'Вы на позиции х={self.x} y={self.y}')

    def go_left(self):
        self.x -= self.s
        print(f'Вы на позиции х={self.x} y={self.y}')

    def go_right(self):
        self.x += self.s
        print(f'Вы на позиции х={self.x} y={self.y}')

    def evolve(self):
        self.s += 1
        print(f'Вы ходите на {self.s} клеток')

    def degrade(self):
        if self.s > 0: 
            self.s -= 1
            print(f'Вы ходите на {self.s} клеток')
        else: print("Невозможно выполнить операцию")

    def count_moves(self, x2, y2):
        print(f'Вы на позиции х={self.x} y={self.y}')
        print(f'Вам нужно сходить минимум на {abs(y2 - self.y) + abs(x2 - self.x)} клеток')

t = Turtle()
command = ""
while command != "stop":
    command = input("Введите команду (up/down/left/rigth/evolve/degrade/count/stop): ").lower()
    if command == "stop":
        print("Программа завершена.")
        break
    elif command == "up":
        t.go_up()
    elif command == "down":
        t.go_down()
    elif command == "left":
        t.go_left()
    elif command == "right":
        t.go_right()
    elif command == "evolve":
        t.evolve()
    elif command == "degrade":
        t.degrade()
    elif command == "count":
       t.count_moves(int(input("Введите Х назначения: ")),int(input("Введите У назначения: ")))
    else:
        print("Неизвестная команда. Попробуйте ещё раз.")
