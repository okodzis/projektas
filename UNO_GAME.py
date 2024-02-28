import random

# Define Card class
class Card:
    def __init__(self, color, rank):
        self.rank = rank
        if ctype[rank] == 'number':
            self.color = color
            self.cardtype = 'number'
        elif ctype[rank] == 'action':
            self.color = color
            self.cardtype = 'action'
        else:
            self.color = None
            self.cardtype = 'action_nocolor'

    def __str__(self):
        if self.color is None:
            return self.rank
        else:
            return self.color + " " + self.rank

# Define Deck class
class Deck:
    def __init__(self):
        self.deck = []
        for clr in color:
            for ran in rank:
                if ctype[ran] != 'action_nocolor':
                    self.deck.append(Card(clr, ran))
                    self.deck.append(Card(clr, ran))
                else:
                    self.deck.append(Card(clr, ran))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# Define Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.cardsstr = []
        self.number_cards = 0
        self.action_cards = 0

    def add_card(self, card):
        self.cards.append(card)
        self.cardsstr.append(str(card))
        if card.cardtype == 'number':
            self.number_cards += 1
        else:
            self.action_cards += 1

    def remove_card(self, place):
        self.cardsstr.pop(place - 1)
        return self.cards.pop(place - 1)

    def cards_in_hand(self):
        hand_str = ''
        for i, card_str in enumerate(self.cardsstr):
            hand_str += f' {i + 1}. {card_str}\n'
        return hand_str

    def single_card(self, place):
        return self.cards[place - 1]

    def no_of_cards(self):
        return len(self.cards)

# Function to choose who starts first
def choose_first():
    return random.randint(0, 3)

# Function to check if the game is won
def win_check(hand):
    return len(hand.cards) == 0

# Function to check if last card is an action card (game must end with a number card)
def last_card_check(hand):
    for c in hand.cards:
        if c.cardtype != 'number':
            return True
    return False

# Function to check if a card thrown by Player/PC is valid by comparing it with the top card
def single_card_check(top_card, card):
    if card.color == top_card.color or top_card.rank == card.rank or card.cardtype == 'action_nocolor':
        return True
    return False

# Function to check if PC has any valid card to throw
def full_hand_check(hand, top_card):
    for c in hand.cards:
        if c.color == top_card.color or c.rank == top_card.rank or c.cardtype == 'action_nocolor':
            return hand.remove_card(hand.cardsstr.index(str(c)) + 1)
    return 'no card'
