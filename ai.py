def getEquity(payouts, stacks, player_index, total=None, payout_index=None):
    """ Returns the equity for a specified player based on stack size and payouts. """
    if total == None:
        total = sum(stacks)
        payout_index = 0
        stacks = list([float(stack) for stack in stacks])
        if stacks[player_index] == 0:
            #If hero's stack is 0, they come in "last place" of all
            #remaining. However if we are ITM, that doesn't = 0....!
            if len(stacks) > len(payouts):
                return 0.
            else:
                return float(payouts[len(stacks) - 1])

    equity = stacks[player_index] / total * payouts[payout_index]
    if payout_index < len(payouts) - 1: #payout_index is 0-based
        for i, stack in enumerate(stacks):
            if i != player_index and stack > 0:
                stacks[i] = 0.
                equity += getEquity(payouts, stacks, player_index, total - stack, payout_index + 1) * stack / total
                stacks[i] = stack

    return equity

def getEquities(payouts, stacks):
    """ Return list of all equities for each player defined in stacks. """
    for i in range(len(stacks)):
        yield getEquity(payouts, list(stacks), i)

def action(hero,pot,communityCards,payout,players):
    a=[]
    indexP=players.index(hero)
    for player in players:
        a.append((player>>15) & 16383)
    e=getEquity(payout, a, indexP)
    if pushValue(indexP,hero,pot,communityCards,a)>e:
        return a[indexP]
    else:
        return 0

def firstIn():
    return 1
def secondIn():
    return 1

def pushValue(i,hero,pot,cards,chipVector):
    heroHand=[(hero[1]>>8)& 255,(hero[2]>>8) & 255]
    if firstIn():
        return 1
    elif secondIn():
        return 1
    else:
        if (heroHand[0] & 15)==(heroHand[1] & 15) and heroHand[0] & 15 >=9:
            return 1




if __name__ == '__main__':
    payouts = (0.5, 0.5)
    stacks = (200, 400, 200, 100)
    for i, eq in enumerate(getEquities(payouts, stacks)):
        print ("Player ",i,": stack ",stacks[i]," equity ",eq)


