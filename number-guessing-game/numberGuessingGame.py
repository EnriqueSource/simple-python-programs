import random

secret_number = random.randint(1, 10)

while True:
  guess = int(input("Guess the number between 1 and 10: "))

  if guess == secret_number:
    print("Congratulation! You guessed the number!")
    break

  elif guess < secret_number:
    print("Too low! try again.")

  else:
    print("Too high! try again.")

