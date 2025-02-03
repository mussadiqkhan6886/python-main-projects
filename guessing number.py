import random

computer = random.randint(1, 25)

guess_limit = 3
guess_count = 0

guess = False

while guess_count < guess_limit:
    user = int(input("Enter number you guessed: "))
    guess_count += 1
    print(f"Your guess count is : {guess_count } out of 3")
    if user == computer:
        print("\nCORRECT")
        print("YOU WIN")
        print(f"You guessed in {guess_count} guesses")
        guess_count += 1
        guess = True
        break
    if guess_count == guess_limit:
        print("End of guesses")
        break
    elif user > computer :
        print("Higher number")
    elif user < computer:
        print("Lower number")
    elif user != computer:
        print("Try Again")
    else:
        print("ERROR")     
    
if user != computer or guess_count == guess_limit:    
    print(f"The correct answer is {computer}")