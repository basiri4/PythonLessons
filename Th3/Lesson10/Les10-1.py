pets = dict()
pet = input("Имя питомца: ")
type = input("Тип питомца: ")
age = int(input("Возраст питомца: "))
owner = input("Имя владельца: ")

pets[pet] = {'Тип питомца':type,'Возраст питомца':age,'Имя владельца':owner}

if (age % 10 == 1):
    year = "год"  
elif (age % 10 > 1) and (age % 10 <= 4) and ((age < 11) or (age > 14)): 
    year = "года"
else: year = "лет"

for k in pets.keys():
    print("Это", pets[k]['Тип питомца'], "по кличке", f'"{k}".', "Возраст питомца:", pets[k]['Возраст питомца'], year + ".", "Имя владельца:", pets[k]['Имя владельца'])
