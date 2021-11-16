# print("Лабораторна робота №4: РЯДКИ", "Роботу виконала: Єсипенко Є.Ю. ,КМ-11", "Варіант номер 8. ", "За умовою завдання програма видаляє усі символи 'а' зі слів, довжина яких дорівнює 5", "", sep = "\n")


# a = True
# while (a == True):

#     b = True
#     while (b == True):
#         t = (input('Введіть будь-яке одне слово англійською мовою: ').lower())
#         if t.isalpha() and len(t) == 5:
#             q = t.replace('a', '')
#             b = False
#         else:
#             print('Помилка, слово повинно складатися лише із 5 англ. літер')
#             b = True

#     print('Ваше слово:', q)

#     answer = str.lower(input('Хочете запустити програму ще раз?(yes/no) '))
#     while (answer != 'yes') and (answer != 'no'):
#         answer = str.upper(input('Введене значення не відповідає вимогам, але можете спробувати ще раз(yes/no): '))
#     if answer == 'yes':
#         a = True
#     else:
#         a = False


from sympy import *
    
x = Symbol('x')
    
f = input("Enter the function: ")
    
f_der = Derivative(f, x)
f_der = f_der.doit() #do the derivative and assign it to variable
print(f_der)
    
f = lambdify(x, f)
f_derivative = lambdify(x, f_der) #convert it to function
    
userInput = float(input("Try critical point: "))
print("Your input: ", userInput)
    
result = f_der(userInput) #pass the point to the function and assign it to variable

print("Result: ", result)