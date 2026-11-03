#name1, name2, name3 = input("Enter three names: ").split(" ")
#print(f"Name1: {name1}")
#print(f"Name2: {name2}")
#print(f"Name3: {name3}")

number = 5.26459884
print(f"Formatted number: {number:.2f}")


year = 2023
quantity = 3
price = 450
print(f"I have {quantity} footballs for {price} pounds in the year {year}.")

sentence = "I have bought 3 footballs for 450 pounds in the year 2023."
print(sentence[0])

sentence = "I have bought 3 footballs."
print(len(sentence))

import datetime
today = datetime.date.today()
print("Current date:", today)

import random
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

import random
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
number = random.randint(num1, num2)
print("Random number:", number)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
total = num1 + num2
print("The total is:", total)