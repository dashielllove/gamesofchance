import random

money = 100

#this game is called flipcall

def flipcall(call, bet):
    num = random.randint(0, 1)
    if (call == "heads") and (num == 0):
        print("Congrats, you won " + str(bet) + "! ")
        return money + bet
    elif (call == "tails") and (num == 1):
        print("Congrats, you won " + str(bet) + "!")
        return money + bet
    else:
        print("Better luck next time, you lost " + str(bet) + ".")
        return money - bet