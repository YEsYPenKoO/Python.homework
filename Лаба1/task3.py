print("Лабораторна номер 1: Програмування лінійних алгоритмів та розгалуджених процесів")
print("Варіант номер 8. Обчислення конкретної функції, в залежності від введеного значення х")
print("Роботу виконала: Єсипенко Є.Ю. ,КМ-11")



print ("Введіть число")
print ("")
q = True
while q:
   x = str(input())
   if (not x.isdigit()  and not x[0]=="-"):
# перевіряємо чи є введене значення числом за допомогою атребут isdigit, та узгоджуємо існування мінуса перед числом


       print ("Аби програма працювала, введіть число")
       print ("")

   elif (x[0]=="-"):
    # тепер вказуємо умову для від'ємного значення числа

       q = False
   elif (x=="0"):
    # задаємо умову для випадку рівності з нулем

       q = False
   elif (x.isdigit()):
       q = False
       

print ("Дякую")
print ("")

# далі йде розгалуження відносно значенню X

x = int(x) 
# x це число, за нашою перевіркою, тому int

if (x<=2):
   y=x*x+4*x+5
   print ("Відповідь на рівняння буде: ", y)
# перший варіант розв'язку

if (x>2):
   y=1/(x*x+4*x+5)
   print ("Відповідь на рівняння буде: ", y)
# другий варіант розв'язку


