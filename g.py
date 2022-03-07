while True:
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    num_3 = input('\n 1: + \n 2: - \n 3: * \n 4: / \nВыберите ---> ')
    
    if num_3 == 0:
        break
    if num_3 == '1':
        print(num_1+num_2)
    if num_3 == '2':
        print(num_1-num_2)
    if num_3 == '3':
        print(num_1*num_2)
    if num_3 == '4':
        try:
            print(num_1/num_2)
        except ZeroDivisionError:
            print('на ноль делить нельзя! ')

