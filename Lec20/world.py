import numpy as np

SEED_FUND = 50
WIN_PROBABILITY = 0.4

# Returns 1 for heads and 0 for tails
def coin_toss():
    outcome = np.random.random()
    if (outcome < WIN_PROBABILITY):
        return 1
    else:
        return 0



class Gambler(object):

    def __init__(self):
        self.balance = SEED_FUND

    def gamble(self, bet):
        toss = coin_toss()
        if (toss):
            self.balance += bet
        else:
            self.balance -= bet
    
