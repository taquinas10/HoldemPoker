cardVector=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
cardSuit=["0","c","s","0","d","0","0","0","h"]

def getCard(iNumber):
    return cardVector[iNumber]
def getSuit(iNumber):
    return cardSuit[iNumber]
def getPrimeBits(iCard):
    return iCard & 63
def getValueBits(iCard):
    return (iCard>>8) & 15
def getSuitBits(iCard):
    return (iCard>>12) & 15

def getStringCard(iCard):
    return getCard(getValueBits(iCard))+getSuit(getSuitBits(iCard))
