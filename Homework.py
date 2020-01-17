#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# a = 0
# for i in range(1,6):
#     print(i,a, sep=')')
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# b = 0
# for i in range (0,10):
#    print('Enter any number in range from 0 to 9 ')
#    a = input()
#    a = int(a)
#    if a == 5:
#        b += 1
# print ('You entered number "5" for',b,'times')
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# mult = 1
# for i in range(2,11):
#     mult *=i
# print(mult)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# number = 8264
# mult_number = 0
#
# while number>0:
#      mult_number += number%10
#      number = number//10
# print(mult_number)

'''
Задача 7
Найти произведение цифр числа.
'''
# number1 = 2222
# mult_number1 = 1
#
# while number1>0:
#      mult_number1 *= number1%10
#      number1 = number1//10
# print(mult_number1)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number2 = 253413
# while integer_number2>0:
#     if integer_number2%10 == 5:
#         print('Yes')
#         break
#     integer_number2 = integer_number2//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# integer_number3 = 253493
# c = integer_number3%10
#
# while integer_number3>0:
#     integer_number3 = integer_number3//10
#     if integer_number3%10 > c:
#         c = integer_number3%10
# print (c)

'''
Задача 10
Найти количество цифр 5 в числе
'''
# integer_number10 = 555534879
# i10 = 0
#
# while integer_number10>0:
#     if integer_number10%10 == 5:
#         i10 +=1
#     integer_number10 = integer_number10//10
#
# print (i10)