import random, time
def help():
        help_data = """
           1.Standard table poker hands are used*
           2.You are dealt five starting cards.
           3.You can choose to hold or discard any or all of your cards.
           4.All cards you choose to discard will be replaced in a single random draw
           5.If your hand now matches any of the qualifying poker hands, you win the corresponding prize
           Winnings:
           Jacks or better ..... +5 points
           Two pairs ..... +10 points
           Three of a kind ..... +15 points
           Straight ..... +20 points
           Flush .... +25 points
           Full house .... +40 points
           Four of a kind .... +125 points
           Straight Flush ....+250 points
           Royal Flush .... +2000 points"""

        print ("Rules of Video Poker : \n" + help_data)
        print()
        inputStr = input ("Type resume to resume the game : ")
        if inputStr == " resume ":
            print("Game resumes.")
            


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
  def __init__(self, name):
    self.cards = []
    self.name = name
  
  def __repr__(self):
    return self.player

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


def VideoPoker():
  nameInput = input ("Enter your name :")
  player = Player(nameInput)

  # Intial Amount
  points = 100

  # Cost per hand
  handCost = 5

  end = False
  while not end:
    print( "{1} have {0} points".format(points,str(nameInput)) )
    

    points-= 5

    ## Hand Loop
    deck = StandardDeck()
    deck.shuffle()

    # Deal Out
    for i in range(5):
      player.addCard(deck.deal())

    # Make them visible
    for card in player.cards:
      card.showing = True
    print(player.cards)

    validInput = False
    while not validInput:
      print("Which cards do you want to discard? ( ie. 1, 2, 3 )")
      print("*Just hit return to hold all, type exit to quit, type help to know the rules")
      inputStr = input()

      if inputStr == "exit":
        end=True
        break
      elif inputStr == "help":
          help()
          break



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
        print("Input Error: use commas to separated the cards you want to hold")

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
      print("You win +2000 points")
      points += 2000

    # Straight flush
    elif straight and flush:
      print("Straight Flush!")
      print("You win +250 points")
      points += 250

    # 4 of a kind
    elif score.fourKind():
      print("Four of a kind!")
      print("You win +125 points")
      points += 125

    # Full House
    elif score.fullHouse():
      print("Full House!")
      print("You win +40 points")
      points += 40

    # Flush
    elif flush:
      print("Flush!")
      print("You win +25 points")
      points += 25

    # Straight
    elif straight:
      print("Straight!")
      print("You win +20 points")
      points += 20

    # 3 of a kind
    elif highestCount == 3:
      print("Three of a Kind!")
      print("You win +15 points")
      points += 15

    # 2 pair
    elif len(pairs) == 2:
      print("Two Pairs!")
      print("You win +10 points")
      points += 10

    # Jacks or better
    elif pairs and pairs[0] > 10:
      print ("Jacks or Better!")
      print("You win +5 points")
      points += 5

    player.cards=[]
    if points == 0:
      print("You loose all your points. Game Over.")
      end = True
      break


VideoPoker()
    



  
  


    