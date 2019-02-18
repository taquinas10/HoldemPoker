
import random
import tables
listPrimes=tables.listPrimes
def makeDeck ():

    n = 0
    deck=[None]*52
    for i in range (0,4):
        
        iSuit=(2**i)<<12
        
        for j in range(0, 13):
            deck[n] = listPrimes[j] | (j << 8) | iSuit | (1 << (16+j))
            n+=1
    return deck

def shuffle(deck):
    return random.shuffle(deck)

