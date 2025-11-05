print "Hello world"
print "Hello I'm github"


#З 21.10 по 24.10

#Num 1
#name = input("Введіть ваше ім'я: ")
#age = input("Введіть ваш вік: ")
#print("Привіт {name}, тобі {age}!")


#Num 2
#age = int(input("Введіть ваш вік: "))
#if age > 18:
    #print("Вхід дозволено!")
#else:
    #print("Вхід заборонено!")


#Num3
#import random
#secret_number = random.randint(1, 10)
#print("Гра 'Вгадай число'!")
#print("Я загадав число від 1 до 10. Спробуй вгадати!")

#while True:
#   guess = int(input("Введи число: "))
#    if guess == secret_number:
#       print("Вітаю ,Ти вгадав число!")
#       break


#Num4
#start = int(input("Введіть число 'з': "))
#end = int(input("Введіть число 'по': "))
#print("Числа від {start} до {end}:")
#for num in range(start, end + 1):
  #  print(num)


#Num5
#a = float(input("Введіть перше число (a): "))
#b = float(input("Введіть друге число (b): "))
#operation = input("Вкажіть дію (+, -, *, /): ")
#if operation == "+":
#    result = a + b
#elif operation == "-":
#    result = a - b
#elif operation == "*":
#    result = a * b
#elif operation == "/":
 #   if b != 0:
 #       result = a / b
#    else:
 #       result = "Ділення на нуль!"
#else:
 #   result = "Неправильна дія!"
#print("Результат:", result)



#ДОМАШКА НОМЕР 2
class Product:
    def __init__(self, name, price, available=True):
        self.name, self.price, self.available = name, price, available

class Cart:
    def __init__(self):
        self.items = []

    def add(self, p):
        if p.available: self.items.append(p)
    def total(self):
        return sum(i.price for i in self.items)
    def show(self):
        for i in self.items: print(f"{i.name} — {i.price} грн")

p1 = Product("Мишка", 500)
cart = Cart()
cart.add(p1)
cart.show()
print("Разом:", cart.total(), "грн")




