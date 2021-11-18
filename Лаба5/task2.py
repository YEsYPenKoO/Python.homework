print("Лабораторна робота №5: ВИКОРИСТАННЯ ФУНКЦІЙ", "Роботу виконала: Єсипенко Є.Ю. ,КМ-11", "Варіант номер 8. ", "Вирівнювання рядка s по правому краю до довжини l.", "", sep = "\n")


while True:
 def right(s,l):
    if len(s) >= l:
      return s
    res = s.rjust(l, ' ')
    return res

 s = input('Ввод: ')

 def length(smt):
    while True:
        try:
            x = int(input(smt))
            if x <= 0:
                raise Exception('Введене число має бути більше за нуль')
            return x
        except Exception as e:
            print(e)

 l = length(('Введіть довжину, за якою буде рівнятися введене значення: '))
 print(f'Результат: {right(s,l)}')

 answer= input('Хочете повторити? (так/ні):  ')
 if answer == "так":
    continue
 elif answer== "ні":
        break


    


