import random


class Card:
  def __init__(self, suit, rank):
    self.suit=suit
    self.rank=rank

  def __str__(self):
    return f"{self.rank['rank']} of {self.suit}"

class Deck:
  def __init__(self):
    self.cards=[]
    suits= ["spades","clubs","hearts","diamonds"]
    ranks= [
        {"rank":"A", "value":11},
         {"rank":"2", "value":2},
         {"rank":"3", "value":3},
         {"rank":"4", "value":4},
         {"rank":"5", "value":5},
         {"rank":"6", "value":6},
         {"rank":"7", "value":7},
         {"rank":"8", "value":8},
         {"rank":"9", "value":9},
         {"rank":"10", "value":10},
         {"rank":"J", "value":10},
         {"rank":"Q", "value":10},
         {"rank":"K", "value":10}
        ]
  
    for suit in suits:
      for rank in ranks:    
        self.cards.append(Card(suit, rank))
  
  def shuffle(self):
    if len(self.cards)>1:
      random.shuffle(self.cards)
  
  def deal(self,num):
    cardsDealt=[]
    for card in range(num):
      if len(self.cards)>0:        
        cardsDealt.append(self.cards.pop())
    return cardsDealt

class Hand:
  def __init__(self,dealer=False):
    self.cards=[]
    self.value=0
    self.dealer= dealer

  def addCard(self, cardList):
    self.cards.extend(cardList)
  def calcValue(self):
    self.value= 0
    hasAce = False
    for card in self.cards:
      cardValue= int(card.rank["value"])
      self.value+=cardValue
      if card.rank["rank"]=="A":
        hasAce = True

    if hasAce and self.value> 21:
      self.value -=10

  def getValue(self):
    self.calcValue()
    return self.value

  def isBlackJack(self):
    return self.getValue()==21

  def display(self, showAllDealerCards=False):
    
    print(f'''{"Dealer's" if self.dealer else "Your"} Hand''')
    for index, card in enumerate(self.cards):
      if index == 0 \
      and self.dealer \
      and not showAllDealerCards \
      and not self.isBlackJack():
        print("Hidden")
      else:
        print(card)

    if not self.dealer:
      print("Value: ", self.getValue())
    print()

class Game:
  def play(self):
    gameNum = 0
    gamesToPlay = 0
    while(gamesToPlay<=0):
      try:
        gamesToPlay = int(input("How many games do you wanna play?: "))
      except:
        print("You must enter a number: ")

    while gameNum < gamesToPlay:
      gameNum+=1

      deck = Deck()
      deck.shuffle()

      playerHand = Hand()
      dealerHand = Hand(dealer=True)

      for i in range (2):
        playerHand.addCard(deck.deal(1))
        dealerHand.addCard(deck.deal(1))
      print()
      print("*"*30)
      print(f"Game {gameNum} of {gamesToPlay}")
      print("*"*30)
      playerHand.display()
      dealerHand.display()

      if self.checkWinner(playerHand, dealerHand):
        continue
      choice = ''
      while playerHand.getValue()<21 and choice not in ["s", "stand"]:
        choice = input("Please choose 'Hit' or 'Stand': ").lower()
        print(choice)
        while choice not in ["h","s","hit","stand"]:
          choice = input("Please enter 'Hit/H' or 'Stand/S': ").lower()
          print(choice)
        if choice in ["hit","h"]:
          playerHand.addCard(deck.deal(1))
          playerHand.display()
        if self.checkWinner(playerHand, dealerHand):
          continue  

      playerHandValue= playerHand.getValue()
      dealerHandValue= dealerHand.getValue()

      while dealerHandValue <17:
        dealerHand.addCard(deck.deal(1))
        dealerHandValue = dealerHand.getValue()
      dealerHand.display(showAllDealerCards=True)
      if self.checkWinner(playerHand, dealerHand):
        continue
      print("Final Results")
      print("Your Hand: ", playerHandValue)
      print("Dealer's Hand: ", dealerHandValue)
      self.checkWinner(playerHand, dealerHand, True)
      print("\nThanks for playing!")
  def checkWinner(self, playerHand, dealerHand, gameOver = False):
    if not gameOver:
      if playerHand.getValue()>21:
        print("You busted!! Dealer wins! 😭")
        return True
      elif dealerHand.getValue()>21:
        print("Dealer busted!! You win! 😏")
        return True
      elif dealerHand.isBlackJack() and playerHand.isBlackJack():
        print("Y'all tied!! 🥱")
        return True
      elif playerHand.isBlackJack():
        print("You have a blackjack!! You win! 😏")
      elif dealerHand.isBlackJack():
        print("Dealer has a blackjack!! Dealer wins! 😭")
        return True
    else:
      if playerHand.getValue() > dealerHand.getValue():
        print("You win!! 😏")
      elif playerHand.getValue() == dealerHand.getValue():
        print("A tie!! 🥱")
      else:
        print("Dealer won!! 😭")
      return True
    return False
    
g= Game()
g.play()