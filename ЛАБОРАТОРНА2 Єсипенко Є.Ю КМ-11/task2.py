print("Лабораторна робота номер 2: ПРОГРАМУВАННЯ ЦИКЛІЧНИХ АЛГОРИТМІВ")
print("Варіант номер 8. Організація циклу за допомогою оператора while")
print("Роботу виконала: Єсипенко Є.Ю. ,КМ-11")

import math
while True:
 while True:
        try:
            number = int(input("Input a number you want to expand: "))
            break
        except ValueError:
            print("Something went wrong..oops!")


 print("Theese are your factors: ")

 for i in range(2, int(math.sqrt(number)) + 1): 
    while (number % i == 0): 
        print(i)
        number //= i 

 if (number != 1): 
    print (number)

 answer= input('Do you want to do that again? If you do, type Yes, and if not, type No:  ')
 if answer == "Yes":
        continue
 elif answer== "No":
        break

print('Goodbye')



