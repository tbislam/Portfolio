#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
randomten = randint(1,10)
# For Testing: print(aRandomNumber)
i=0
print("Hello, which range do you want to start with?")
print("For 1-10, click a")
print("For 1-20, click s")
print("For 1-30, click d")

answer = input("Choose a range")

if answer == "a":
	while i<3:
		guess = input("Guess a number between 1 and 10 (inclusive): ")
		if not guess.isnumeric(): # checks if a string is only digits 0 to 9
			print("That's not a positive whole number, try again!")
		else:
			guess = int(guess) # converts a string to an integer
			print(i)
			i+=1
		if guess == randomten:
			print("Congrats you got it!")
		if guess >= randomten:
			print("Nope, that is too high")
		if guess <= randomten:
			print("Nope, that is too low")

	if i == 3:
		print("The correct number was", randomten)


while i<3:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer
		print(i)
		i+=1
	if guess == aRandomNumber:
		print("Congrats you got it!")
	if guess >= aRandomNumber:
		print("Nope, that is too high")
	if guess <= aRandomNumber:
		print("Nope, that is too low")
		break
if i == 3:
	print("The correct number was", aRandomNumber)
