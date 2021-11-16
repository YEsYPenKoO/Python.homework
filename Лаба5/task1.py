print("Лабораторна робота №5: ВИКОРИСТАННЯ ФУНКЦІЙ", "Роботу виконала: Єсипенко Є.Ю. ,КМ-11", "Варіант номер 8. ", "Написати функцію, яка обчислює площу трикутника зі сторонами x, y і z, якщо такий трикутник існує.", "", sep = "\n")



import math




# def perimetr(a, b):  
#   p=(a+b+c)/2 
#   res = math.sqrt(p*(p-a)*(p-b)*(p-c)) 
#   return res  

while True:
      
 print("Встановимо сторони гіпотетичного трикутника:")
 a=float(input('Введіть a = '))
 b=float(input('Введіть b= ')) 
 c=float(input('Введіть c= ')) 
 d=float(input('Введіть d= ')) 

  
 def sqrt(x, y, z):  #функція для обчислення площі трикутника
    p=(x+y+z)/2 
    res = math.sqrt(p*(p-x)*(p-y)*(p-z)) 
    res_r = round(res, 2)
    return res_r

 q=0
  
 print('')

 if a + b > c and a + c > b and b + c > a:
    q= q + 1
    
    print('Площа сторін a, b та c: ', sqrt(a, b, c))
    print('')

 if  c + b > d and b + d > c and d + c > b:
    q= q + 1
    
    print('Площа сторін b, c та d: ', sqrt(b, c, d))
    print('')

 if  d + c > a and a + d > c and a + c > d:
    q=q + 1
    
    print('Площа сторін a, c та d: ', sqrt(a, c, d))
    print('')

 if  a + b > d and a + d > b and d + b > a:
    q=q + 1
    
    print('Площа сторін a, b та d: ', sqrt(a, b, d))
    print('')

 if q>1:   
  print('Всього', q, 'варіанти площ')
 elif q==1:
    print('Всього 1 варіант площі') 
 else:
    print('Площ немає')

 answer= input('Хочете повторити? (так/ні):  ')
 if answer == "так":
       continue
 elif answer== "ні":
        break

