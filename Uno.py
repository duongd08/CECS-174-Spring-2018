from random import *

#original decks
red = ['0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','switch', 'cancel','switch', 'cancel', '+2','+2']
blue = ['0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','switch', 'cancel','switch', 'cancel', '+2','+2']
green = ['0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','switch', 'cancel','switch', 'cancel', '+2','+2']
yellow = ['0','1','2','3','4','5','6','7','8','9','1','2','3','4','5','6','7','8','9','switch', 'cancel','switch', 'cancel', '+2','+2']
wild = ['null','null','null','null','null','null','null','null']

cards = [red,blue,green,yellow] #dont need

playerDeck = [0]*7
computerDeck = [0]*7
playDeck = [0]
#Takes cards from original decks and randomly 
#assigns to a deck without replacement or repeaters
def main():
        print('\t\t\tWelcome to the Game:')
        print('\t\t\t\tUNO')
        print('-------------------------------------------------------------------')
        print('Rules:')
        print('-Your goal is to get to zero cards before the computer')
        print('-Match the color or number to the top of the deck')
        print('-Switch and cancel are treated as skip cards')
        print('-------------------------------------------------------------------')
        assignDeck(playerDeck)
        assignDeck(computerDeck)
        start_card(playDeck)
        print("")
        print("Your Deck: ")
        print(playerDeck)
        print("")
        print("Top of Game Deck")
        print(playDeck[0])
        print("")
        # finish the game when length of one 
        count=0
        rotate = 1# make the count stop somewhere
        while rotate > 0 :
            playerTurn(playDeck,playerDeck)
            if len(playerDeck) > 0:
                rotate = rotate*-1
                count = count+1
            else:
                break
            while rotate < 0 :
                print("")
                print("------------------------------------------------------------")
                print("         OPPONENT'S TURN")
                print("")
                computerTurn(playDeck, computerDeck)# have to make computerTurn() and replace here
                if len(computerDeck)>0:
                    rotate = rotate*-1
                    count = count+1
                else:
                    break
        if len(playerDeck) == 0:
            print("")
            print("You Win!")
        else:
            print("")
            print("The Computer Won!")

def start_card(deck):
    assignDeck(deck)
    getColor(deck, 0)
    if getArgument(deck,0) == 'switch' or getArgument(deck,0) == '+2' or getArgument(deck,0) == 'cancel' or getArgument(deck,0) == 'wild':
        start_card(deck)

def assignDeck(deck): 
    for i in range (0,len(deck)):
        a = randint(1,29)
        if a==1 or a==1 or a==2 or a==3 or a==4 or a==5 or a==6 or a==7 :  
            r = randint(0,len(red)-1)
            stringr = red[r]
            deck[i] = "red",stringr
            del red[r]
        elif a==8 or a==9 or a==10 or a==11 or a==12 or a==13 or a==14 :
            b = randint(0,len(blue)-1)
            stringb = blue[b]
            deck[i] = "blue",stringb
            del blue[b]             
        elif a==15 or a==16 or a==17 or a==18 or a==19 or a==20 or a==21 :
            g = randint(0,len(green)-1)
            stringg = green[g]
            deck[i] = "green",stringg
            del green[g]
        elif a==22 or a==23 or a==24 or a==25 or a==26 or a==27 or a==28 :
            y = randint(0,len(yellow)-1)
            stringy = yellow[y]
            deck[i] = "yellow",stringy
            del yellow[y]
        else:
            w = randint(0, len(wild)-1)
            stringw = wild[w]
            deck[i] = "wild",stringw
            del wild[w]
            
#return color of desired card index in desired deck
def getColor(deck, index): 
    if index>=len(deck) or index<0:
        print("ERROR: Index out of bounds please try again")
        newIndex = int(input("Enter a new index: "))
        getColor(deck, newIndex)
    else:
        c = str(deck[index])
        if c[2] == 'r':
            return "red"
        if c[2] == 'b':
            return "blue"
        if c[2] == 'g':
            return "green"
        if c[2] == 'y':
            return "yellow"
        if c[2] == 'w':
            return "wild"

def getArgument(deck,index):
    x = getColor(deck,index) #following if statements find what color it is (already defined)
    if x =='red': #need to know color to know how far index needs to go to find first letter of the second argument of the card
        b = str(deck[index]) # = desired index for the color you want fo find
        y = b[9] # = first character of the second argment of the card
    elif x =='blue':
        b = str(deck[index])
        y = b[10]
    elif x =='green':
        b = str(deck[index])
        y = b[11]
    elif x == 'yellow':
        b = str(deck[index])
        y = b[12]
    else:
        y == 'null'
    if y== '0':
        return '0'
    elif y== '1':
        return '1'
    elif y=='2':
        return '2'
    elif y=='3':
        return '3'
    elif y=='4':
        return '4'
    elif y=='5':
        return '5'
    elif y=='6':
        return '6'
    elif y=='7':
        return '7'
    elif y=='8':
        return '8'
    elif y=='9':
        return '9'
    elif y=='s':
        return 'switch'
    elif y=='c':
        return 'cancel'
    elif y=='+':
        return '+2'
    else:
        return 'wild'

def playerWild (yourDeck, gameDeck, index):
    newColor = input("Enter desired color: ")
    newCard = newColor
    gameDeck.insert(0,newCard)
    del yourDeck[index] 

def playerTurn(gameDeck, yourDeck):
    global card
    print("")
    print("------------------------------------------------------------")
    print("         YOUR TURN         ")
    print("NOTE: if you have no available card, type: draw (lowercase)")
    print("")
    x = input("wild, color or draw: ")
    if x == "draw":
        print("")
        draw(yourDeck)
        print("You have drawn a card to your deck")
        print("Your updated deck:")
        print("")
        print(yourDeck)
        return
    if x == "wild":  #Here is Wild
        ToF = -1
        for i in range(len(yourDeck)):
            if x == getColor(yourDeck, i):
                ToF = 0
                playerWild(yourDeck, gameDeck, i)
                break
        if ToF == -1:
            print("ERROR: incorrect input!  Please try again in selecting a wild card/color and remember input should be all lowercase: ")
            playerTurn(gameDeck, yourDeck)
            return
        else:
            print("")
            print("Your updated deck:")
            print("")
            print(yourDeck)
            print("")
            print("Top of the game deck: ")
            print(gameDeck)
            return

    if x != 'red' and x!= 'blue' and x!= 'green' and x!= 'yellow':
        x = input("ERROR: incorrect input!  Please try again in selcting a color and remember input should be all lowercase: ") 
    y = input("argument: ")
    if y!= '0' and y!= '1' and y!='2' and y!='3' and y!='4' and y!='5' and y!='6' and y!='7' and y!='8' and y!='9' and y!='switch' and y!='cancel' and y!='+2' and y!='wild':
        y = input("ERROR: incorrect input!  Please try again in selecting an argument and remember input should be all lower case: ")
    if x != getColor(gameDeck, 0) and y != getArgument(gameDeck, 0):
        print("ERROR: This card cannot be placed. Try again.")
    if x == getColor(gameDeck, 0) or y == getArgument(gameDeck, 0):       
        index = 1000
        for i in range(0, len(yourDeck)):
            if getArgument(gameDeck, 0) == 'wild':
                getColor(yourDeck,i)==x and getArgument(yourDeck,i)==y
            if getColor(yourDeck,i)==x and getArgument(yourDeck,i)==y:
                if y == 'switch' or y == 'cancel':
                    index=i
                    card = str(yourDeck[i])
                    gameDeck.insert(0,card)
                    del yourDeck[index]
                    print("")
                    print("You chose: ", card)
                    print("")
                    print("Your Deck: ")
                    print(playerDeck)
                    print("")
                    print("Top of Game Deck")
                    print(gameDeck[0])
                    print("")
                    print("The computer turn has been skipped")
                    print("")
                    playerTurn(gameDeck, yourDeck)
                    break
                if y == '+2':
                    draw(computerDeck)
                    draw(computerDeck)
                    index=i
                    card = str(yourDeck[i])
                    gameDeck.insert(0,card)
                    del yourDeck[index]
                    print("")
                    print("You chose: ", card)
                    print("")
                    print("Your Deck: ")
                    print(playerDeck)
                    print("")
                    print("Top of Game Deck")
                    print(gameDeck[0])
                    print("")
                    print("The computer has gained 2 cards and its turn has been skipped.")
                    print("")
                    playerTurn(gameDeck, yourDeck)
                    break
                else:
                    index=i
                    card = str(yourDeck[i])
                    gameDeck.insert(0,card)
                    del yourDeck[index]
                    print("")
                    print("You chose: ", card)
                    print("")
                    print("Your Deck: ")
                    print(playerDeck)
                    print("")
                    print("Top of Game Deck")
                    print(gameDeck[0])
                    print("")
                    break
        if index==1000:
            print("ERROR: incorrect input!  This card does not exist please try again")
            playerTurn(gameDeck, yourDeck)
    
def computerTurn(gameDeck, otherDeck):
    global card
    a = 0
    for i in range(0, len(otherDeck)):
        if getColor(otherDeck,i) == 'wild':
            a = randint(1,4)
            if a == 1:
                wildComCard = "red", "null"
            elif a == 2:
                wildComCard = "blue", "null"
            elif a == 3:
                wildComCard = "green", "null"
            else:
                wildComCard = "yellow", "null"
            print("The computer chose a wild card!")
            print("")
            print("")
            gameDeck.insert(0, wildComCard)
            del otherDeck[i]
            print("Your Deck: ")
            print(playerDeck)
            print("")
            print("Top of Game Deck")
            print(gameDeck[0])
            print("")
            return
        if getColor(otherDeck,i)== getColor(gameDeck, 0) or getArgument(otherDeck,i)== getArgument(gameDeck, 0):
            if getArgument(otherDeck,i)== 'switch' or getArgument(otherDeck,i)== 'cancel':
                print("The computer chose: " , otherDeck[i])
                print("")
                print("")
                gameDeck.insert(0,otherDeck[i])
                del otherDeck[i]
                print("Your Deck: ")
                print(playerDeck)
                print("")
                print("Top of Game Deck")
                print(gameDeck[0])
                print("")
                print("Your turn has been skipped")
                print("")
                print("------------------------------------------------------------")
                print("\t\tOPPONENT'S TURN")
                print("")
                a = 1
                computerTurn(gameDeck, otherDeck)
                break
            if getArgument(otherDeck,i)== '+2':
                draw(playerDeck)
                draw(playerDeck)
                print("The computer chose: " , otherDeck[i])
                print("")
                print("")
                gameDeck.insert(0,otherDeck[i])
                del otherDeck[i]
                print("Your Deck: ")
                print(playerDeck)
                print("")
                print("Top of Game Deck")
                print(gameDeck[0])
                print("")
                print("You have gained 2 cards and your turn has been skipped")
                print("")
                print("------------------------------------------------------------")
                print("\t\tOPPONENT'S TURN")
                print("")
                a = 1
                computerTurn(gameDeck, otherDeck)
                break
            else:
                print("The computer chose: " , otherDeck[i])
                print("")
                print("")
                gameDeck.insert(0,otherDeck[i])
                del otherDeck[i]
                print("Your Deck: ")
                print(playerDeck)
                print("")
                print("Top of Game Deck")
                print(gameDeck[0])
                print("")
                a = 1
                break
    if a ==0:
        print("The computer has no playable card and has drawn a card to its deck.")
        print("")
        print("")
        draw(otherDeck)
        print("")
        print("Your Deck: ")
        print(playerDeck)
        print("")
        print("Top of Game Deck")
        print(gameDeck[0])
        print("")
        print(" ")


def draw (deck):
    a = randint(1,29)
    if a==1 or a==1 or a==2 or a==3 or a==4 or a==5 or a==6 or a==7 :
        deck.append(0)
        r = randint(0,len(red)-1)
        stringr = red[r]
        deck[len(deck)-1] = "red",stringr
        del red[r]
    elif a==8 or a==9 or a==10 or a==11 or a==12 or a==13 or a==14 :
        deck.append(0)
        b = randint(0,len(blue)-1)
        stringb = blue[b]
        deck[len(deck)-1] = 'blue',stringb
        del blue[b]             
    elif a==15 or a==16 or a==17 or a==18 or a==19 or a==20 or a==21 :
        deck.append(0)
        g = randint(0,len(green)-1)
        stringg = green[g]
        deck[len(deck)-1] = 'green',stringg
        del green[g]
    elif a==22 or a==23 or a==24 or a==25 or a==26 or a==27 or a==28 :
        deck.append(0)
        y = randint(0,len(yellow)-1)
        stringy = yellow[y]
        deck[len(deck)-1] = 'yellow',stringy
        del yellow[y]
    else:
        deck.append(0)
        w = randint(0, len(wild)-1)
        stringw = wild[w]
        deck[len(deck)-1] = 'wild',stringw
        del wild[w]



main()
