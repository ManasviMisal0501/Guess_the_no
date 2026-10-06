import random

number = random.randint(1, 100)
print("Welcome to the Guess The Number Game!!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts.")

attempts = 0
while attempts < 7:
    try:
        print(f"Attempt {attempts + 1}/7")
        num = int(input("Enter a number : "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    attempts += 1

    if num > number:
        print("You are too High!!")
    elif num < number:
        print("You are too low!!")
    else:
        print("Congratulations You Won!!")
        print(f"You guessed the number in {attempts} attempts.")
        break
else:
    print(f"Sorry! You ran out of attempts. The number was {number}.")
