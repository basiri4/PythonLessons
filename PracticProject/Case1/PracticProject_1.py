import datetime

def get_day(d, m, y):
    dt = datetime.date(y, m, d)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[dt.weekday()]

def is_visokos(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calc_vozrast(d, m, y):
    now = datetime.datetime.now()
    age = now.year - y
    if now.month < m:
        age = age - 1
    elif now.month == m:
        if now.day < d:
            age = age - 1
    return age

def print_tablo(d, m, y):
    # цифры звездочками
    n0 = ["***", "* *", "* *", "* *", "***"]
    n1 = ["  *", " **", "  *", "  *", "***"]
    n2 = ["***", "  *", "***", "*  ", "***"]
    n3 = ["***", "  *", "***", "  *", "***"]
    n4 = ["* *", "* *", "***", "  *", "  *"]
    n5 = ["***", "*  ", "***", "  *", "***"]
    n6 = ["***", "*  ", "***", "* *", "***"]
    n7 = ["***", "  *", "  *", "  *", "  *"]
    n8 = ["***", "* *", "***", "* *", "***"]
    n9 = ["***", "* *", "***", "  *", "***"]
    space = ["   ", "   ", "   ", "   ", "   "]

    nums = {'0': n0, '1': n1, '2': n2, '3': n3, '4': n4, '5': n5, '6': n6, '7': n7, '8': n8, '9': n9, ' ': space}
    
    date_str = str(d)
    if d < 10:
        date_str = "0" + str(d)
    
    month_str = str(m)
    if m < 10:
        month_str = "0" + str(m)
        
    full_str = date_str + " " + month_str + " " + str(y)
    
    for i in range(5):
        row = ""
        for ch in full_str:
            row = row + nums[ch][i] + "  "
        print(row)

try:
    day = int(input("Введите день: "))
    month = int(input("Введите месяц: "))
    year = int(input("Введите год: "))

    print("День недели:", get_day(day, month, year))
    
    if is_visokos(year) == True:
        print("Год високосный? Да")
    else:
        print("Год високосный? Нет")
        
    print("Вам лет:", calc_vozrast(day, month, year))
    print("Табло:")
    print_tablo(day, month, year)
except Exception:
    print("Ошибка ввода")