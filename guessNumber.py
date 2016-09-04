import random
number = str(random.randint(1, 10))

print(number) # Show for testing

print("I bet you can't guess the number I am thinking of between 1 and 10?")
guess = str(input("Type in your guess. "))

print("You guessed " + guess + "...")

while number:
	if guess == number:
		print("Congratulations! You go it :)")
		break
	elif guess < number:
		guess = str(input("You're guess is too low. Try again. "))
	elif guess > number:
		guess = str(input("You're guess is too high. Try again. "))
	else:
		print("You're guess was invalid.")
