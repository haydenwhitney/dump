# Hayden Whitney
# 2/19
# Blackjack (allows up to 7 players to play against the dealer)

import cards, games


class BlackjackCard(cards.Card):
    """A Blackjack Card"""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            value = BlackjackCard.RANKS.index(self.rank) + 1
            if value > 10:
                value = 10
        else:
            value = None
        return value


class BlackjackDeck(cards.Deck):
    """A Blackjack Deck"""
    def populate(self):
        for suit in BlackjackCard.SUITS:
            for rank in BlackjackCard.RANKS:
                card = BlackjackCard(rank, suit, True)
                self.add(card)


class BlackjackHand(cards.Hand):
    """A Blackjack Hand"""
    def __init__(self, name):
        super(BlackjackHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BlackjackHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        total = 0
        for card in self.cards:
            total += card.value
        contains_ace = False
        for card in self.cards:
            if card.value == BlackjackCard.ACE_VALUE:
                contains_ace = True
        if contains_ace and total <= 11:
            total += 10
        return total

    def is_busted(self):
        return self.total > 21


class BlackjackPlayer(BlackjackHand):
    """A Blackjack Player"""
    def hit(self):
        response = games.yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")


class BlackjackDealer(BlackjackHand):
    """A Blackjack Dealer"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BlackjackGame(object):
    """A Blackjack Game"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BlackjackPlayer(name)
            self.players.append(player)
        self.dealer = BlackjackDealer("Dealer: ")
        self.deck = BlackjackDeck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.hit():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
        if self.dealer.is_busted():
            for player in self.still_playing:
                player.win()
        else:
            for player in self.still_playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("Welcome to Blackjack!")
    names = []
    number = games.input_number("How many players? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Enter player name: ").title()
        names.append(name)
    game = BlackjackGame(names)
    again = None
    while again != "n":
        game.play()
        again = games.yes_no("Do you want to play again? ")


main()
input("Press the enter key to exit. ")
