import random


money = 100


def roulette(call, bet):
    number = random.randint(1, 38):
    zero = 37
    double_zero = 38
    row_bet = 37 or 38
    if number == call:
        print("congrats!  you win " + (35 * (bet)) + "!")
        return (money + (35 * bet))
    elif row_bet == call and number == row_bet:
        print("congrats! you win " + (17 * (bet)) + "1")
        return (money + (17 * bet))
    elif number < 37 and number % 2 != 0 and call == "odds":
        print("congrats! you win! +" + str(bet))
        return money + bet
    elif number < 37 and number % 2 == 0 and call == "even":
        print("congrats! you win! +" + str(bet))
        return money + bet
    else:
        print("try again! you lose " + str(bet) + "!")
        return money - bet

#example: 

roulette("even", 10)