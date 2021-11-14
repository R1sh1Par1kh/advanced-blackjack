# main.py
import random
import time

input("Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this game, Jack, Queen, and King are each worth 10 and the Ace is worth 1 or 11.\n\nThe dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!\n\nPress Enter to start playing.")

#dictionary for the values of all the cards
hand = []
cards = {11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}

#print your current hand you are going to send it a list of cards prints out with proper name
def printHand(hand):
  x = []
  for item in hand:
    if item > 10:
      x.append(cards[item])
    else:
      x.append(item)
  print(x)
  

subtractedAce = True
# take in a list of cards and then going to return the sum (this is where check if Ace is 1 or 11)
def calcHandValue(hand):
  global subtractedAce
  subtractedAce = True
  added = 0
  for item in hand:
    if item == 14:
     added += 11
    elif item > 10:
      added += 10
    else:
      added += item
    if 14 in hand and added > 21 and subtractedAce:
      added -= 10
      subtractedAce=False
  return added

#set the cards they start 
while True:  
  hand = []
  for i in range(2):
    hand.append(random.randint(2, 14))
  #list add 2 cards
  while calcHandValue(hand) < 21:
    print("Here is your hand:")
    printHand(hand)
    print()
    risk = input("Type H to hit or S to stay: ")
    if risk == "H":
      hand.append(random.randint(2,14))
    elif risk == "S":
      break
    else:
      print("Your input is invalid! Try H or S :)\n")
  dhand = []    
  #busted and dealer hand
  if calcHandValue(hand) > 21:
    print("____________________________________")
    print("You busted!\n")
    print("Here was your ending hand: ")
    printHand(hand)
    print()
  elif calcHandValue(hand) == 21:
    print("Congrats, that's an automatic win! You hit blackjack :)")
    printHand(hand)
  else: 
    print("Dealer's turn!\n")
    for i in range(2):
      dhand.append(random.randint(2,14))
    print("Here is the dealer's hand: ")
    printHand(dhand)
    while calcHandValue(dhand) < 17:
      time.sleep(2)
      dhand.append(random.randint(2,14))
      time.sleep(2)
      print("Here is the dealer's hand: ")
      printHand(dhand)
      time.sleep(2)
    if calcHandValue(dhand) > calcHandValue(hand) and calcHandValue(dhand) <= 21:
      print("You lose! Here were your hands: ")
      printHand(dhand)
      printHand(hand)
    elif calcHandValue(dhand) != calcHandValue(hand):
      print("You won! Here were your hands: ")
      printHand(dhand)
      printHand(hand)
    else:
      print("You tied with the Dealer! Here were your hands: ")
      printHand(dhand)
      printHand(hand)

  endchoice = input("Press enter to play again or Q to quit: ")
  if endchoice == "Q":
    break
