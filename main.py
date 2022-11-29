# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип списка нужно выбрать в зависимости от поставленной ниже задачи). 
# После чего нужно показать меню, в котором предложить пользователю набор пунктов:

# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения).
import os
import sys
from classlist import mStack


def mMenu():
    print("1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).")
    print("2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления).")
    print("3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца).")
    print("4. Проверить есть ли значение в списке.")
    print("5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения).")
    print("6. Выход ")
    m=input("Введите значение ")
    return m


# ■■ помещение строки в стек;
# ■■ выталкивание строки из стека;
# ■■ подсчет количества строк в стеке;
# ■■ проверку пустой ли стек;
# ■■ проверку полный ли стек;
# ■■ очистку стека;
# ■■ получение значения без выталкивания верхней строки из стека.

def mMenStack():
    print("1. помещение строки в стек")
    print("2. выталкивание строки из стека")
    print("3. подсчет количества строк в стеке")
    print("4. проверку пустой ли стек")
    print("5. проверку полный ли стек")
    print("6. очистку стека")    
    print("7. получение значения без выталкивания верхней строки из стека")        
    print("8. Выход ")
    m=input("Введите значение: ")
    return m

lst=mStack()
lst.add("Дима")
lst.add("Витя")
# lst.add("Коля")
# lst.add("RRRR")
# lst.print()
# print(lst.getlast())
# lst.print()
# # print("Введите список ")
os.system("cls")  
# os.system('clear')
# m=mMenStack()    
while True:
 os.system("cls") 
 m=mMenStack()    
 if int(m)==1:
   str=input("Введите строку: ") 
   lst.add(str)
   lst.print()
   input("Для продолжения введите любую клавишу")
 elif int(m)==2:
   print(lst.out())
   lst.print()
   input("Для продолжения введите любую клавишу")
 elif int(m)==3:
   print(lst.getCol()) 
   lst.print()
   input("Для продолжения введите любую клавишу")
 elif int(m)==4:
#    print(lst.isNone()) 
   if lst.isNone():
    print("Стек пустой") 
    lst.print()   
   else:
    print("Стек не пуст")  
    lst.print()
    input("Для продолжения введите любую клавишу" )   
 elif int(m)==5:
    if lst.isFull():
        print("Стек полон")      
        lst.print()    
    input("Для продолжения введите любую клавишу"  )    
 elif int(m)==6:
     lst.clear()
     lst.print()
     input("Для продолжения введите любую клавишу" )
 elif int(m)==7:
    lst.print()
    print(f"Верхнее значение  {lst.getlast()}")     
    lst.print()
    input("Для продолжения введите любую клавишу"  ) 
 elif int(m)==8:
  os.system('CLS') 
  quit()
