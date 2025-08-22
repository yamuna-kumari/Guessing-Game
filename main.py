import random
def guessingGame():
    random_num = random.randint(1, 100)
    attempt = 0
    MaxAttempt = 5
    
    while attempt < MaxAttempt:
        try:
            guess = int(input("Enter a number between 1 to 100:"))
            
        except ValueError:
            print('please enter a valid number')
            continue
        
        attempt = attempt + 1
        if guess < random_num:
            print("The number is too low")
            
        elif guess > random_num:
            print("the number is too high")
            
        else:
            print("Match")
            break
    else:
        print(f"game over! The number was {random_num}")
        
guessingGame()