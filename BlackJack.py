def main():
#Deck:
    deck=["A(Hearts)","J(Hearts)","K(Hearts)","Q(Hearts)","2(Hearts)","3(Hearts)","4(Hearts)","5(Hearts)","6(Hearts)","7(Hearts)","8(Hearts)","9(Hearts)","10(Hearts)","A(Diamonds)","J(Diamonds)","K(Diamonds)","Q(Diamonds)","2(Diamonds)","3(Diamonds)","4(Diamonds)","5(Diamonds)","6(Diamonds)","7(Diamonds)","8(Diamonds)","9(Diamonds)","10(Diamonds)","A(Spades)","J(Spades)","K(Spades)","Q(Spades)","2(Spades)","3(Spades)","4(Spades)","5(Spades)","6(Spades)","7(Spades)","8(Spades)","9(Spades)","10(Spades)","A(Clubs)","J(Clubs)","K(Clubs)","Q(Clubs)","2(Clubs)","3(Clubs)","4(Clubs)","5(Clubs)","6(Clubs)","7(Clubs)","8(Clubs)","9(Clubs)","10(Clubs)"]
    value={"A(Hearts)":10,"J(Hearts)":10,"K(Hearts)":10,"Q(Hearts)":10,"2(Hearts)":2,"3(Hearts)":3,"4(Hearts)":4,"5(Hearts)":5,"6(Hearts)":6,"7(Hearts)":7,"8(Hearts)":8,"9(Hearts)":9,"10(Hearts)":10,"A(Diamonds)":10,"J(Diamonds)":10,"K(Diamonds)":10,"Q(Diamonds)":10,"2(Diamonds)":2,"3(Diamonds)":3,"4(Diamonds)":4,"5(Diamonds)":5,"6(Diamonds)":6,"7(Diamonds)":7,"8(Diamonds)":8,"9(Diamonds)":9,"10(Diamonds)":10,"A(Spades)":10,"J(Spades)":10,"K(Spades)":10,"Q(Spades)":10,"2(Spades)":2,"3(Spades)":3,"4(Spades)":4,"5(Spades)":5,"6(Spades)":6,"7(Spades)":7,"8(Spades)":8,"9(Spades)":9,"10(Spades)":10,"A(Clubs)":10,"J(Clubs)":10,"K(Clubs)":10,"Q(Clubs)":10,"2(Clubs)":2,"3(Clubs)":3,"4(Clubs)":4,"5(Clubs)":5,"6(Clubs)":6,"7(Clubs)":7,"8(Clubs)":8,"9(Clubs)":9,"10(Clubs)":10}
    import random
    random.shuffle(deck)
#Function Bank:
    def deal(n):
        while len(AIDealer_hand)!=n:
            AIDealer_hand.append(deck[0])
            del deck[0]
            if len(AIDealer_hand)==n:
                print("Dealer has:", AIDealer_hand)
        while len(Player_hand)!=n:
            Player_hand.append(deck[0])
            del deck[0]
            if len(Player_hand)==n:
                print(Player_user_name,"has:", Player_hand)
#Allow Player1 to view rules or skip to start a game:
    print("Let’s play Blackjack!")
    view_rules = input("Would you like to view the rules? Please type yes or no and press enter.")
    while view_rules!= "yes" and view_rules!="no":
        view_rules = input("Error: player must type 'no' or 'yes'")
    if view_rules=="yes":
        print("This is how this game of Blackjack works! There will be two players: you and the dealer. The main goal of Blackjack is to get a hand of cards that will add up to 21 but will not exceed it. Now, this ain’t no traditional game of Blackjack - instead of using all 4 suits this game only uses 1 suit. So we will only have one set of cards from A to King(including numbered cards). In this version of Blackjack all cards not numbered (i.e Ace, Jack, Queen, King) will have a value of 10. In this game the Dealer wins whenever there’s a tie and as long as the Dealer has less than 21 it will continue  to hit (you better not lose). Both you and Dealer will be able to see what cards you both have, and then you will be given the option to either hit or stand. When you hit, you are asking for another card, of which its value will add on to the sum. If your new card brings your sum up to 21, you may choose to stand (which you should since getting 21 is the whole point of the game). If you go over 21, the game will end immediately and declare you as the loser. If you do not go over 21 and you will be given again the chose to hit or stand. If you choose to stand the Dealer will be given its turn and will choose to hit until it reaches or surpasses 21. Once it reaches 21, the game will end and declare the Dealer the winner, however if the Dealer surpasses 21 the game will declare you the winner.Good luck partner!")
    if view_rules=="no":
        print("Let's start!")
#Allow Player1 to input desired username:
    Player_user_name=input("Please insert Username:")
#declare hand variables:
    AIDealer_hand=[]
    Player_hand=[]
#Declare len variable:
    n=2
#Assign the variable names for the sum of cards for both players:
    AI_Dealer_CardSum=sum(map(value.get,AIDealer_hand))
    Player_CardSum=sum(map(value.get,Player_hand))
#Allow Player1 to make a bet:
    bet = int(input("Place your Bet:"))
    winning_amount=bet*2
    if bet>=1000:
        print ("WOAH THERE HIGH ROLLER")
    if bet<1000:
        print ("That’s a little punk bet.")
#Deal the cards to both Player1 and AI_Dealer:
    deal(n)
#Determine the results of the deal:
    while Player_CardSum==21 and Player_CardSum!=AI_Dealer_CardSum:
         print(Player_user_name,"wins:",winning_amount)
         break
    while Player_CardSum<21 and AI_Dealer_CardSum<21:
         Player_Answer = input("would you like to hit or stay?:")
         if Player_Answer=="stay"and Player_CardSum<=AI_Dealer_CardSum:
             print("Dealer wins:",winning_amount,"FIATCOINS")
             break
         elif Player_Answer=="stay" and AI_Dealer_CardSum<Player_CardSum:
             print(Player_user_name,"wins:",winning_amount,"FIATCOINS")
             break
         if Player_Answer=="hit":
             print("Dealing...")
             n+=1
             deal(n)
             AI_Dealer_CardSum=sum(map(value.get,AIDealer_hand))
             Player_CardSum=sum(map(value.get,Player_hand))
    while Player_CardSum<21 and AI_Dealer_CardSum>21:
        print(Player_user_name,"wins:",winning_amount,"FIATCOINS")
        break
    else:
        print("Dealer wins:",winning_amount,"FIATCOINS")

main()
