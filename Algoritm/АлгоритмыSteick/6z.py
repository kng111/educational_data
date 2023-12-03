# сли ИМТ меньше  18.5, то считается, что человек весит ниже нормы
# больше 25, то считается, что человек весит больше нормы
list1 = []
while True:
    try:
        x = input()
        list1.append(x)
    except:
        break

mass = ((float(list1[0]) / (float(list1[1]) * float(list1[1]))))


if int(mass) > 25:
    print('Избыточная масса')
elif 17 <  int(mass)  <= 25:
    print('Оптимальная масса')
elif int(mass) < 18:
    print('Недостаточная масса')
print(mass)