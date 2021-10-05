print("Лабораторна робота номер 2: ПРОГРАМУВАННЯ ЦИКЛІЧНИХ АЛГОРИТМІВ")
print("Варіант номер 8. Організація циклу за допомогою оператора for Організація циклу за допомогою оператора while")
print("Роботу виконала: Єсипенко Є.Ю. ,КМ-11")

while True:
    print("Input x: ")
    while True:
        try:
            x = float(input())
            break
        except ValueError:
            print("Something went wrong, type smting else: ")

    print('input n:')
    while True:
        try:
            n = int(input())
            break
        except ValueError:
            print("Something went wrong, type smting else: ")

    result = 0
    for i in range(1, n+1):
        result += 1 / x**2 + i 
        result_round=round(result, 2)

        
    print("Here is the result: ", result_round)


    answer= input('Do you want to do that again? If you do, type Yes, and if not, type No:  ')
    if answer == "Yes":
        continue
    elif answer== "No":
        break

print('Goodbye')



