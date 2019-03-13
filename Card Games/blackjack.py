# Hayden Whitney
# 2/19
# Blackjack


class Card(object):
    """This class will build a single card. To build a card call Card() and pass in a rank and suit.
    Ex: card = Card(random.choice(Card.RANKS), random.choice(Card.SUITS))"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit, is_face_up):
        self.rank = rank
        self.suit = suit
        self.is_face_up = is_face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "🂠"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):
    """This class will build a hand out of the cards already made. To build a hand append your cards to a """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """Derived from the Hand class. Use deck = Deck() to access the class. The Deck class allows you to
    populate the deck with all 52 individual cards by using deck.populate(). The Deck class can
    also shuffle the deck by using up deck.shuffle()."""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit, False)
                self.add(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards.")


class UnprintableCard(Card):
    """A card that won't reveal its rank or suit when printed."""
    def __str__(self):
        return "🂠"


if __name__ == "__main__":
    print("You ran this module directly and did not 'import' it")
    input("\n\nPress the enter key to exit.")
