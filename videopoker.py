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
           2.You need to make a deposit.(minimum-10credit,maximum-100credit)
           3.Each Hand Costs 5 credits.
           4.You are dealt five starting cards.
           5.You can choose to hold or discard any or all of your cards.
            5.1 Inorder to discard cards you need to enter numbers(1-5).seperated with commas in refrence to card number.
           6.All cards you choose to discard will be replaced in a single random draw.
           7.If your hand now matches any of the qualifying poker hands,you win the corresponding prize.

           Poker Hands              Winnings:
                                                         example ('-'followed by card and its suits denotes winning cards)
           Jacks or better .....        20         [10♡,5♡,Q♠,-K♣,-K♠]
           Two pairs ..... .....        40         [-10♡,5♡,-10♠,-K♣,-K♠]
           Three of a kind .....        60         [-Q♢, K♡, A♣,-Q♠,-Q♣]
           Straight ............        80         [-9♡,-10♡,-J♠,-Q♣,-K♠]
           Flush ...............        100        [-10♡,-5♡,-Q♡,-K♡,A♠]
           Full house ..........        120        [-Q♢,- A♡, A♣,-Q♠,-Q♣]
           Four of a kind ......        140        [-Q♢, Q♡, A♣,-Q♠,-Q♣]
           Straight Flush ......        160        [-2♣,-3♣,-4♣,-5♣,-6♣]   
           Royal Flush .........        200        [-A♣,-K♣,-Q♣,-J♣,-10♣] """

        print ("Rules and Winnings of Video Poker : \n" + help_data)
        print()
        resume()
        os.system("cls")
        print("Game resumes.")
        

def resume():
  inputStr = input ("Type resume to resume the game :")
  while "resume"  not in inputStr:
    inputStr = input ("Input Error:-type resume to resume the game :")

def VideoPoker():
  os.system("cls")
  print("Welcome to Video Poker Game")
  print()
  time.sleep(1)
 
  nameInput = input("Enter your name player:")
  while not nameInput:
    nameInput = input("Required input,Enter your name player: ")
  player = Player()
  rules = input("For Rules and Winnng Multipliers-type help or press Enter to start the game,{0}: ".format(nameInput))
  if rules.lower() == "help":
    os.system("cls")
    help()
  print("Game Startinng")
  time.sleep(1)
  os.system("cls")
 
  # Player bet
  isBet = False
  while not isBet:
    bet = input("{0},Deposit credits(10-100):".format(nameInput))
    if bet == "help":
      help()
    try:
      bet = int(bet)
      while bet < 10 or bet > 100:
        bet = int(input("{0},Minimum deposit:10,Maximum deposit:100:".format(nameInput)))
        break
      isBet = True
    except ValueError:
      print("{0},Credits are only numbers".format(nameInput))
  
  # Cost per hand is 5 credits
  handCost = 5
  print("{0},each hand costs you {1} credits.".format(nameInput,handCost))
  time.sleep(2)
  

  end = False
  while not end:
    bet = int(bet)
    bet-= handCost
    os.system("cls")


    ## Hand Loop
    deck = StandardDeck()
    deck.shuffle()
    print("{0},your credit:{1}".format(nameInput,bet))
    print()
    

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
      print("""Which cards do you want to discard? ( ie. 1, 2, 3, 4, 5 ) or \n-Just hit ENTER to hold all, -type exit to quit the game, -type help to know the rules and Winnings:""")
      inputStr = input()
      if inputStr.lower() == "exit":
        quit()
      elif inputStr.lower() == "help":
        os.system("cls")
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
        print("Use commas between the numbers to discard the cards,follow the question below.")
        
    print()
    print(player.cards)
    time.sleep(1)

    
    
    #Score
    score = PokerScorer(player.cards)
    straight = score.straight()
    flush = score.flush()
    highestCount = score.highestCount()
    pairs = score.pairs()

    # Royal flush
    if straight and flush and straight == 14:
      print("Royal Flush!!!")
      print("You win 200 credits.")
      bet += 200
      print()

    # Straight flush
    elif straight and flush:
      print("Straight Flush!")
      print("You win 160 credits.")
      bet += 160
      print()

    # 4 of a kind
    elif score.fourKind():
      print("Four of a kind!")
      print("You win 140 credits")
      bet += 140
      print()

    # Full House
    elif score.fullHouse():
      print("Full House!")
      print("You win 120 credits")
      bet += 120
      print()

    # Flush
    elif flush:
      print("Flush!")
      print("You win 100 credits")
      bet += 100
      print()

    # Straight
    elif straight:
      print("Straight!")
      print("You win 80 credits")
      bet += 80
      print()

    # 3 of a kind
    elif highestCount == 3:
      print("Three of a Kind!")
      print("You win 60 credits")
      bet += 60
      print()

    # 2 pair
    elif len(pairs) == 2:
      print("Two Pairs!")
      print("You win 40 credits")
      bet += 40
      print()

    # Jacks or better
    elif pairs and pairs[0] > 10:
      print ("Jacks or Better!")
      print("You win 20 crdits")
      bet += 20
      print()
    else:
      print("No win")
      print()
   
    if bet <= 0:
      print("You loose all your credits. Game Over.")
      while True:
        restart = input("Do you want to deposit more -type y for yes /n for no?")
        if restart.lower() == "n":
          quit()
        
        elif restart.lower() == "y":
          VideoPoker()
    
    print()
    print("Do you want to cash out or continue ?")
    withdraw = input("-press y to cash out or -press ENTER to continue:")
    if withdraw.lower() == "y":
      print("{0},you cashed out:{1}".format(nameInput,bet))
      print("ThankYou for playing.See you next time! ")
      time.sleep(1)
      quit()

   

    player.cards=[]

    
      


VideoPoker()
