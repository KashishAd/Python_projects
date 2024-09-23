#Name: Kashish Adlakha
#UId: U31221034
#Description: This program mimics the game of magic 8 ball. It asks the user to input a question and then gives a response from the 20 statements stored in the code.

import random

def magic_eight_ball(n):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", 
        "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", 
        "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", 
        "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", 
        "Don't count on it.", "Outlook not so good.", "My sources say no.", "Very doubtful."
    ]
    print(responses[n])
    
def main():
    print("Welcome to the Magic 8 Ball! Ask a yes-or-no question and receive an answer.")
    q= input("What is your question?")
    x= random.randint(0,19)
    magic_eight_ball(x)
    a= input("Would you like to ask another question?")
    while a.lower()!="no":
        q= input("What is your question?")
        x=random.randint(0,19)
        magic_eight_ball(x)
        a= input("Would you like to ask another question?")

main()
