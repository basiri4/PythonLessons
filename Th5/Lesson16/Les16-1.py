class Kassa(object):
    money = 0

    def top_up(self, prihod):
        self.money +=prihod

    def count_1000(self):
        print(f'В кассе осталось {self.money // 1000} тысяч')

    def take_away(self, minus):
        if self.money >= minus: self.money -= minus
        else: print("Недостаточно средств на счете")

k1 = Kassa()
k1.top_up(int(input("Сколько хотите положить на счёт: ")))
k1.take_away(int(input("Сколько хотите снять со счёта: ")))
k1.count_1000()



