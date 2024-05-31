import random
number = random.randint(1, 10)
guess = int(input("Take a guess: "))    
while guess != number:
    if guess > number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    
print("You guessed it! The number was", number)
input("\n\nPress the enter key to exit.")
