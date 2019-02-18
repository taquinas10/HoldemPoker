import poker
import deck
import tables
import grafics
import cardDictionary


d=deck.makeDeck()
e=9999
i=0
tries=1000
results={"HIGH_CARD":0,"ONE_PAIR":0,"TWO_PAIR":0,"THREE_OF_A_KIND":0,"STRAIGHT":0,"FLUSH":0,"FULL_HOUSE":0,"FOUR_OF_A_KIND":0,"STRAIGHT_FLUSH":0}
for i in range(0,tries):
    deck.shuffle(d)
    if i%10000==0:
        print (i,"finished")
    for j in range(0,7):
        aHand=[d[0+j*7],d[1+j*7],d[2+j*7],d[3+j*7],d[4+j*7],d[5+j*7],d[6+j*7]]
        e=poker.eval7hand(aHand)
        results[poker.valueDescriptor(e)]+=1


for key in results:
    print("RESULTS",key,results[key])
    print("EXPECTED:",key,tables.prob[key]*tries*7)


###test grafics
def graficsTest():
    print ("graficsTest")
    ddeck=[]
    hand=[]
    for i in range(0,52):
        ddeck.append(grafics.graficCard(d[i]))
    for i in range(0,2):
        grafics.addHoleCard(ddeck[i])
        hand.append(d[i])
        print(cardDictionary.getStringCard(d[i]))
    for i in range(0,5):
        grafics.addCommunityCard(ddeck[i+2])

        hand.append(d[i+2])
        print(cardDictionary.getStringCard(d[i+2]))
    e=poker.eval7hand(hand)
    results[poker.valueDescriptor(e)]+=1
    print("RESULTS",poker.valueDescriptor(e))
    grafics.main()

#graficsTest()