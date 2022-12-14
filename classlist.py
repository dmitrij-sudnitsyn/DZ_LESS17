# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип списка нужно выбрать в зависимости от поставленной ниже задачи). 
# После чего нужно показать меню, в котором предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все вхождения).

class mList:
    def __init__(self,value,lastlist=None,nextlist=None):
        pass


# Задание 2 Реализуйте класс стека для работы со строками (стек строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■■ помещение строки в стек;
# ■■ выталкивание строки из стека;
# ■■ подсчет количества строк в стеке;
# ■■ проверку пустой ли стек;
# ■■ проверку полный ли стек;
# ■■ очистку стека;
# ■■ получение значения без выталкивания верхней строки из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необ-
# ходимую операцию.

class mStack:
    def __init__(self,a=0) -> None:
        self.__stack=[]
        self.MaxElem=a

    def add(self,value):
        if self.MaxElem!=0:
            if len(self.__stack)<self.MaxElem:
             self.__stack.append(value)   
            else:
             print("Добавление нового элемента не возжно вы достигли максимального значения размера стека")
        else:
         self.__stack.append(value)   

    def getCol(self):     
        return len(self.__stack)

    def out(self):
        for i in range(len(self.__stack)):
            print(self.__stack.pop()) 

        # if len(self.__stack)==0:
        #   return None
        # else:
        #   return self.__stack.pop()         

    def isNone(self):
        print(f"количество = {len(self.__stack)}")
        if len(self.__stack)==0:
            return True
        else:
            return False

    def isFull(self):            
        if len(self.__stack)==self.MaxElem:
            return True
        else:
            return False    

    def getlast(self):
        if len(self.__stack)>0:
            str=self.__stack.pop()
            self.__stack.append(str)
            return str

    def clear(self):
        # for i in len(self._stack):
          self.__stack.clear()


    def print(self):
        print(self.__stack)      
