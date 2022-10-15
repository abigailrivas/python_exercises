#Ejercicio 1

from winsound import PlaySound


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

#Ejercicio 4
number = int(input("Enter a number: "))
listOfNumbers = range(1, number + 1)
listOfDivisors = []

print("This are its divisors: ")
for x in listOfNumbers:
    if number % x == 0:
        listOfDivisors.append(x)

print("This are its divisors: " + str(listOfDivisors))

#Ejercicio 5 con repetidos permitido
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for x in a:
    if x in b:
        print(x)

#Ejercicio 6
string = input("Enter a string: ")
palindrome = True

for i in range(len(string)):
    if string[i] != string[len(string) - 1 - i]:
        palindrome = False

if palindrome == True:
    print("It's a palindrome!")
else:
    print("It's not a palindrome! :C")

#Ejercicio 7
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 == 0]

#Ejercicio 8
#To define which one beats which
rules = {"rock": "scissors", "scissors" : "paper", "paper": "rock"}

def RPS(input1,input2):
    winner1 = False
    for x in rules:
        if x == input1 and rules.get(input1) == input2:
            winner1 = True
            break
    if winner1 == True:
        print("Player 1 won!")
    else:
        print("Player 2 won!")

stop = "play"

while stop != "stop":
    input1 = input("Player 1, enter your play: ")
    input2 = input("Player 2, enter your play: ")
    RPS(input1,input2)
    stop = input("Enter 'stop' to exit or 'play' to do it again: ")

#Ejercicio 9
import random

num = random.randint(1,9)
guess = int(input("I have a number between 1 and 9, which one is it? "))

if abs(num - guess) == 0:
    print("You guessed!")
elif num > guess:
    print("Too low")
else:
    print("Too high")

#Ejercicio 10
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = [x for x in a if x in b]

print(common)

#Ejercicio 11