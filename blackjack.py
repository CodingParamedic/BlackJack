import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

'''
card object
'''

class Card():
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + ' of ' + self.suit

'''
deck object
'''

class Deck():
	def __init__(self):

		self.deck = []

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):

		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n' + card.__str__()

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()

'''
hand object
'''

class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_cards(self,card):
		self.cards.append(card):
		self.value += values[card.rank]

	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

'''
chips object
'''

class Chips:

	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

'''
taking bets
'''

def take_bet(chips):

	while True:
		try:
			chips.bet = int(input("Place your bet. "))
		except ValueError:
			print("None of that. Place your bet. ")
		else:
			if chips.bet > chips.total:
				print("You only have ",chips.total)
			else:
				break

'''
deal
'''

def hit(deck,hand):

	hand.add_card(deck.deal())
	hand.adjust_for_ace()

'''
hit or stand
'''

def hit_or_stand(deck,hand):

	global playing

	while True:

		x = input("Hit or Stand? Press H or S: ")

		if x[0].lower() == 'h':
			print("Hit!")
			hit(deck,hand)

		elif x[0].lower() == 's':
			print("Player stands. Dealer turn.")
			player = False

		else:
			print("Try again")
			continue
		break

'''
display cards
'''

def show_some(player,dealer):
	'''
	Dealer
	'''
	print("\n Dealer's Hand: ")
	print("First Card Hidden")
	print(dealer.cards[1])

	'''
	player
	'''
	print("\n Player's Hand:")
	for card in player.cards:
		print(card)

def show_all(player.dealer):
	'''
	dealer
	'''
	for card in dealer.cards:
		print(card)
	print(f"Dealer's hand is: {dealer.value}.")
	'''
	player
	'''
	for card in player.cards:
		print(card)
	print(f"Player's hand is: {player.value}.")

'''
win conditions
'''

def player_busts(player,dealer,chips):
	chips.lose_bet()
	print("Player Busts.")

def player_wins(player,dealer,chips):
	chips.win_bet()
	print("Player Wins.")

def dealer_busts(player,dealer,chips):
	chips.win_bet()
	print("Dealer Busts.")

def dealer_wins(player,dealer,chips):
	chips.lose_bet()
	print("Dealer Wins.")

def push(player,dealer):
	print("Tie. Push.")

'''
game logic (God help me)
'''

while True:
	print("Welcome to Blackjack!")

	deck = Deck()
	deck.shuffle()

	'''
	hand setup
	'''

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	'''
	chips
	'''

	player_chips = Chips()

	'''
	bet
	'''

	take_bet(player_chips)

	'''
	cards
	'''

	show_some(player_hand,dealer_hand)

	while playing:

		hit_or_stand(deck,player_hand)

		show_some(player_hand,dealer_hand)

		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)

			break

	if player_hand.value <= 21:

		while dealer_hand.value <17:
			hit(deck,dealer_hand)

		show_all(player_hand,dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)

		else:
			push(player_hand,dealer_hand)

	print("\n Player Chips are at: {}.".format(player_chips.total))

	new_game = input("Play Another Hand? y/n")

	if new_game[0].lower() == 'y':
		playing = True
		continue

	else:
		print("Thanks for Playing!")
		break
