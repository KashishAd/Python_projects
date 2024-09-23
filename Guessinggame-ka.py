#name: Kashish Adlakha 
#UID: U31221034
#Description: The program is made to develop a guessing game where the user is asked to choose a number between 1 and 100. The user will then have 10 tries to guess the number.
Num= int(input("Please guess a number between 1 and 100: "))
def main():
    high = 0
    low = 0
    win = 0
    n = random.randint(1, 100)

    Num = int(input("Please guess a number between 1 and 100: "))
    if Num > n:
        message = "Too high, try again."
        high += 1
    elif Num == n:
        message = "You got it correct! Congratulations!"
        win += 1
    else:
        message = "Too low, try again."
        low += 1

    print(message)
    print("Number of times too high: ", high)
    print("Number of times too low: ", low)
    print("Total number of guesses: ", (high + low + win))
print(main(Num))
    