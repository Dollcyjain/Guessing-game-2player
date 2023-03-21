from random import randint

print("***Welcome the two player guessing game***")
n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
print("Player 1:")
ans = randint(n1, n2)
guesses_of_p1 = 1
while True:
    guess = int(input("Enter your guess: "))
    if guess > ans:
        print("Your guess is greater than the actual answer. Please guess the smaller one.")
        guesses_of_p1 += 1
    elif guess < ans:
        print("Your guess is less than the actual answer. Please guess the greater one.")
        guesses_of_p1 += 1
    else:
        print(f"You guessed it right!!\nYou took total {guesses_of_p1} number of guesses to guess the answer.")
        break
print("Player 2:")
ans = randint(n1, n2)
guesses_of_p2 = 1
while True:
    guess = int(input("Enter your guess: "))
    if guess > ans:
        print("Your guess is greater than the actual answer. Please guess the smaller one.")
        guesses_of_p2 += 1
    elif guess < ans:
        print("Your guess is less than the actual answer. Please guess the greater one.")
        guesses_of_p2 += 1
    else:
        print(f"You guessed it right!!\nYou took total {guesses_of_p2} number of guesses to guess the answer.")
        break

print(f"Number of guesses taken:\n\t1. Player 1: {guesses_of_p1}\n\t2. Player 2: {guesses_of_p2}")
if guesses_of_p1 < guesses_of_p2:
    print("Congratulations Player 1!!\nYou are the Winner!!")
elif guesses_of_p1 > guesses_of_p2:
    print("Congratulations Player 2!!\nYou are the Winner!!")
else:
    print("Ohh!! It's a tie. It happens very rarely, you know.")
