pets = dict()

def get_suffix(age):
    if (age % 10 == 1):
        return "год"  
    elif ((age % 10 > 1) and (age % 10 <= 4)) and ((age < 11) or (age > 14)): 
        return "года"
    else: return "лет"

def create():
    pet = input("Имя питомца: ")
    if pet in pets:
        print("Питомец с таким именем уже есть.")
        return
    type = input("Тип питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")

    pets[pet] = {
        'Тип питомца': type,
        'Возраст питомца': age,
        'Имя владельца': owner
    }
    print(f'Питомец "{pet}" добавлен.')

def read():
    pet = input("Введите имя питомца: ")
    if pet not in pets:
        print("Такого питомца нет в базе.")
        return
    info = pets[pet]
    year = get_suffix(info['Возраст питомца'])
    print(f'Это {info["Тип питомца"]} по кличке "{pet}". Возраст питомца: {info["Возраст питомца"]} {year}. Имя владельца: {info["Имя владельца"]}')

def update():
    pet = input("Введите имя питомца, которого хотите обновить: ")
    if pet not in pets:
        print("Такого питомца нет в базе.")
        return
    type = input("Новый тип питомца: ")
    age = int(input("Новый возраст питомца: "))
    owner = input("Новое имя владельца: ")

    pets[pet] = {
        'Тип питомца': type,
        'Возраст питомца': age,
        'Имя владельца': owner
    }
    print(f'Данные питомца "{pet}" обновлены.')

def delete():
    pet = input("Введите имя питомца для удаления: ")
    if pet not in pets:
        print("Такого питомца нет в базе.")
        return
    del pets[pet]
    print(f'Питомец "{pet}" удалён из базы.')

def list_pets():
    if not pets:
        print("База пустая.")
        return
    for k in pets.keys():
        age = pets[k]['Возраст питомца']
        year = get_suffix(age)
        print("Это", pets[k]['Тип питомца'], "по кличке", f'"{k}".', "Возраст питомца:", age, year + ".", "Имя владельца:", pets[k]['Имя владельца'])
    print()
command = ''
while command != "stop":
    command = input("Введите команду (create/read/update/delete/list/stop): ").lower()
    if command == "stop":
        print("Программа завершена.")
        break
    elif command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        list_pets()
    else:
        print("Неизвестная команда. Попробуйте ещё раз.")