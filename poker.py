
"""{Rank DeuceThreeFourFiveSixSevenEightNineTenJackQueenKingAce}"""
"""{Prime  2     3   5  7   11 13   17  19  23  29  31   37 41}"""
"""{card will b of type integer with the following setup:}"""
"""{integer is 4 bytes...ie 32 bits to play with}"""
"""{xxxAKQJT 98765432 hdscVVVV xxPPPPPP}"""
"""{x:= not used, VVVV binary of card rank(2=0 A=12) P:=prime hdsc:=suit }"""
"""{00010000 00000000 01001100 00101001 is Ad for example}"""
"""{ie A      not a #  d   12  prime 41 }"""
import cardDictionary
import deck
import tables
import searchIndex
flushes=tables.flushes
perm57=tables.perm57
unique5=tables.unique5
products=tables.products
values=tables.values

def isFlush(iCard1,iCard2,iCard3,iCard4,iCard5):
    isFlush = iCard1 & iCard2 & iCard3 & iCard4 & iCard5 & 61440
    return isFlush # isFlush returns 0 unless the bit corresponding to suit is identical 61440 is intrep of 1111*2^12}

def eval5cards(iCard1,iCard2,iCard3,iCard4,iCard5):

    
    q = (iCard1 | iCard2 | iCard3 | iCard4 | iCard5) >> 16
    
    # check for Flushes and StraightFlushes
    if (iCard1 & iCard2 & iCard3 & iCard4 & iCard5 & 61440):
        return flushes[q]
    
    # check for Straights and HighCard hands
    s = unique5[q]
    if (s):  return s
    
    #// let's do it the hard way
    q = (iCard1 &0xFF) * (iCard2 &0xFF) * (iCard3 &0xFF) * (iCard4 &0xFF) * (iCard5 &0xFF)
    q = searchIndex.search(q,products)
    
    return values[q]




def eval5hand(ahand):

    
    c1 = ahand[0]
    c2 = ahand[1]
    c3 = ahand[2]
    c4 = ahand[3]
    c5 = ahand[4]
    
    return eval5cards(c1,c2,c3,c4,c5)

def eval7hand(aHand):

    best = 9999
    subhand=[None]*5
    
    for i in range( 0, 21):
    
        for j in range(0,5):
            subhand[j] = aHand[ perm57[i][j] ]
        q = eval5hand(subhand)
        if (q < best):
            best = q

    return best

def valueDescriptor(val):
    
    if (val > 6185): return "HIGH_CARD"
    if (val > 3325): return "ONE_PAIR"
    if (val > 2467): return "TWO_PAIR"
    if (val > 1609): return "THREE_OF_A_KIND"
    if (val > 1599): return "STRAIGHT"
    if (val > 322):  return "FLUSH"
    if (val > 166):  return "FULL_HOUSE"
    if (val > 10):   return "FOUR_OF_A_KIND"
    return "STRAIGHT_FLUSH"


