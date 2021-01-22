import random, time, os
class Card( object ):
  def __init__(self, name, value, suit, symbol):
    self.value = value
    self.suit = suit
    self.name = name
    self.symbol = symbol
    self.showing = False

  def __repr__(self):
    if self.showing:
      return self.symbol
    else:
      return "Card"

class Deck(object):
  def shuffle(self, times=1 ):
    random.shuffle(self.cards)
    print("Deck Shuffled")

  def deal(self):
    return self.cards.pop(0)

class StandardDeck(Deck):
  def __init__(self):
    self.cards = []
    suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
    values = {"Two":2,
              "Three":3,
              "Four":4,
              "Five":5,
              "Six":6,
              "Seven":7,
              "Eight":8,
              "Nine":9,
              "Ten":10,
              "Jack":11,
              "Queen":12,
              "King":13,
              "Ace":14 }

    for name in values:
      for suit in suits:
        symbolIcon = suits[suit]
        if values[name] < 11:
          symbol = str(values[name])+symbolIcon
        else:
          symbol = name[0]+symbolIcon
        self.cards.append( Card(name, values[name], suit, symbol) )

  def __repr__(self):
    return "Standard deck of cards:{0} remaining".format(len(self.cards))

class Player(object):
  def __init__(self):
    self.cards = []

  def cardCount(self):
    return len(self.cards)

  def addCard(self, card):
    self.cards.append(card)


class PokerScorer(object):
  def __init__(self, cards):
    # Number of cards
    if not len(cards) == 5:
      return "Error: Wrong number of cards"
    self.cards = cards

  def flush(self):
    suits = [card.suit for card in self.cards]
    if len( set(suits) ) == 1:
      return True
    return False

  def straight(self):
    values = [card.value for card in self.cards]
    values.sort()
    if not len( set(values)) == 5:
      return False 
    if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
      return 5
    else:
      if not values[0] + 1 == values[1]: return False 
      if not values[1] + 1 == values[2]: return False
      if not values[2] + 1 == values[3]: return False
      if not values[3] + 1 == values[4]: return False
    return values[4]

  def highCard(self):
    values = [card.value for card in self.cards]
    highCard = None
    for card in self.cards:
      if highCard is None:
        highCard = card
      elif highCard.value < card.value: 
        highCard=card

    return highCard

  def highestCount(self):
    count = 0
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) > count:
        count = values.count(value)

    return count

  def pairs(self):
    pairs = []
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 2 and value not in pairs:
        pairs.append(value)

    return pairs
        
  def fourKind(self):
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 4:
        return True

  def fullHouse(self):
    two = False
    three = False
    
    values = [card.value for card in self.cards]
    if values.count(values) == 2:
      two = True
    elif values.count(values) == 3:
      three = True

    if two and three:
      return True

    return False

def help():
        help_data = """
                            Rules:
           1.Standard table poker hands are used.
           2.You are dealt five starting cards.
           3.You can choose to hold or discard any or all of your cards.
           4.All cards you choose to discard will be replaced in a single random draw
           5.If your hand now matches any of the qualifying poker hands, you win the corresponding prize
                             Winnings:
           Jacks or better ..... 1X
           Two pairs ..... ..... 2X
           Three of a kind ..... 4X
           Straight ............ 6X
           Flush ............... 8X
           Full house .......... 10X
           Four of a kind ...... 12X
           Straight Flush ...... 14X
           Royal Flush ......... 16X"""

        print ("Rules of Video Poker : \n" + help_data)
        print()
        resume()

def resume():
  inputStr = input ("Type resume to resume the game : ")
  if inputStr == "resume":
    print("Game resumes.")
  else:
    inputStr = input ("Input Error:Type resume to resume the game : ")



def VideoPoker():
  os.system("cls")
  print("Welcome to Video Poker Game")
  print()
  time.sleep(1)
  print("Enter your name player:")
  nameInput = input()
  player = Player()
  print("For Rules and winnng type help or press any key to start the game,{0}:".format(nameInput))
  rules = input()
  if rules.lower() == "help":
    help()
  

  # Player bet
  bet = int(input("{},deposit money(10-100) :".format(nameInput)))
  while bet < 10 or bet > 100:
    bet = int(input("{},minimum deposit:10, maximum deposit:100 :".format(nameInput)))
  time.sleep(1)
  
  # Cost per hand
  handCost = int(input("{0},place a bet(1-10):".format(nameInput)))
  while handCost < 1 or handCost > 10:
    handCost = int(input("Invalid bet,Place a bet(1-10):"))   
  print("{1},each bet is {0} dollars".format(handCost,nameInput))
  time.sleep(1)
  

  end = False
  while not end:
    print()
    print("{0},your credit:{1} dollars".format(nameInput,bet))
    bet-= handCost
    print()
    time.sleep(1)


    ## Hand Loop
    deck = StandardDeck()
    deck.shuffle()
    print()
    time.sleep(1)

    # Deal Out
    for i in range(5):
      player.addCard(deck.deal())

    # Make them visible
    for card in player.cards:
      card.showing = True
    print(player.cards)
    time.sleep(1)

    validInput = False
    while not validInput:
      print()
      print("Which cards do you want to discard? ( ie. 1, 2, 3, 4, 5 )")
      print("*Just hit enter to hold all, type exit to quit, type help to know the rules and winnings multiplier:")
      inputStr = input()

      if inputStr == "exit":
        quit()
      elif inputStr == "help":
        help()
      try:
        inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]

        for inp in inputList:
          if inp > 6:
            continue 
          if inp < 1:
            continue 

        for inp in inputList:
          player.cards[inp-1] = deck.deal()
          player.cards[inp-1].showing = True

        validInput = True
      except:
        print()
        print(player.cards)
        print()
        print("Use commas to separate the cards you want to discard.")
        
    print(player.cards)
    time.sleep(2)

    
    
    #Score
    score = PokerScorer(player.cards)
    straight = score.straight()
    flush = score.flush()
    highestCount = score.highestCount()
    pairs = score.pairs()

    # Royal flush
    if straight and flush and straight == 14:
      print("Royal Flush!!!")
      print("You win 200 dollars.")
      bet += 200
      print()

    # Straight flush
    elif straight and flush:
      print("Straight Flush!")
      print("You win 150 dollars.")
      bet += 150
      print()

    # 4 of a kind
    elif score.fourKind():
      print("Four of a kind!")
      print("You win 125 dollars")
      bet += 125
      print()

    # Full House
    elif score.fullHouse():
      print("Full House!")
      print("You win 100 dollars")
      bet += 100
      print()

    # Flush
    elif flush:
      print("Flush!")
      print("You win 80 dollars")
      bet += 80
      print()

    # Straight
    elif straight:
      print("Straight!")
      print("You win 60 dollars")
      bet += 60
      print()

    # 3 of a kind
    elif highestCount == 3:
      print("Three of a Kind!")
      print("You win 40 dollars")
      bet += 40
      print()

    # 2 pair
    elif len(pairs) == 2:
      print("Two Pairs!")
      print("You win 20 dollars")
      bet += 20
      print()

    # Jacks or better
    elif pairs and pairs[0] > 10:
      print ("Jacks or Better!")
      print("You win 10 dollars")
      bet += 10
      print()
    else:
      print("No win")
      print()
    print("Do you want to cash out or continue ?")
    withdraw = input("press y to cash out or press any key to continue?: ")
    if withdraw.lower() == "y":
      print("{0},your withdraw amount: {1}".format(nameInput,bet))
      print("ThankYou for playing.See you next time! ")
      time.sleep(1)
      quit()
    player.cards=[]
    if bet <= 0:
      print("You loose all your bet. Game Over.")
      restart = input("do you want to restart y/n?")
      if restart.lower() == "n":
        quit()
        
      elif restart.lower() == "y":
        VideoPoker()
      


VideoPoker()
    



  
  


    
