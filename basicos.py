#Ejercicio 1

name = input("What's your name?: ")
age = input("What's your age?: ")
age = int(age)
aging = str(age + 100)

print("Hi " + name + " in 100 years you'll turn " + aging)

#Ejercicio 2
number = int(input("Hi, enter a number :"))

if number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd")

#Ejercicio 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x < 5:
        print(x)

