import random

suits = ["clubs", "diamonds", "hearts", "spades"]
ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "king", "queen", "jack", "ace"]
value = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "king": 10,
         "queen": 10, "jack": 10, "ace": 11}

# player_Value = 0
# dealer_Value = 0

player_Amount = 100

# create all deck card and assign its value


class CardAndValue:

    deck_card_Value = {}

    def __init__(self):

        # self.deck_card_Value = {}
        for suit in suits:
            for rank in ranks:
                if rank in value.keys():
                    temp = "" + suit + " of " + rank
                    self.deck_card_Value[temp] = value.get(rank)
        # print(self.deck_card_Value) # print all cards and its value

    # random card distribute to player and dealer
    @classmethod
    def deal(cls):
        # return cls.deck_card_Value.popitem()
        x = random.choice(list(cls.deck_card_Value.items()))
        cls.deck_card_Value.pop(x[0])
        return x


class BlackJack(CardAndValue):

    def __init__(self):

        while True:
            global bet_amount
            bet_amount = int(input("Enter bet amount: "))

            if bet_amount <= player_Amount:
                break
            else:
                print("Please enter valid amount!!!")
                print("You have total ", player_Amount, " chips")

        # Dealing two card to dealer and two card to player
        super().__init__()
        player_Hand.append(super().deal())
        player_Hand.append(super().deal())
        dealer_Hand.append(super().deal())
        dealer_Hand.append(super().deal())

    @classmethod
    def calculate_Value(cls, player):
        add = 0
        ace_count = 0
        for i in player:
            if i[1] < 11:
                add += i[1]
            else:
                ace_count += 1

        for i in range(ace_count):
            if add > 10:
                add += 1
            elif add <= 10:
                add += 11
            if add >= 21:
                break
        return add

    @classmethod
    def showCard(cls):
        print("-"*30)
        print("Player cards are: ")
        for x in player_Hand:
            print("\t", x[0])

        print("Dealer cards are: ")
        if len(dealer_Hand) > 2:
            for x in dealer_Hand:
                print("\t", x[0])
        else:
            print("\t Card is Hidden")
            print("\t", dealer_Hand[1][0])
        print("-" * 30)

    @classmethod
    def gamePlay(cls):

        cls.showCard()

        while cls.calculate_Value(player_Hand) < 21:

            player_input = input("Would you like to Hit or Stand!!!\nPlease enter 'h' for Hit and 's' for Stand: ")
            if player_input[0].lower() == 'h':
                player_Hand.append(super().deal())
                cls.showCard()
            elif player_input[0].lower() == 's':
                print("Players Stand, Now Dealer play")
                break
            else:
                print("Please enter valid input!!!")
                continue
            # print(player_Hand)

        while cls.calculate_Value(dealer_Hand) < 17:
            dealer_Hand.append(super().deal())

        # print dealer & player card
        # print(player_Hand)
        # print(dealer_Hand)
        cls.showCard()
        global player_Amount

        if cls.calculate_Value(player_Hand) > 21:
            print("player busts")
            player_Amount -= bet_amount
        elif cls.calculate_Value(dealer_Hand) > 21:
            print("dealer bust")
            player_Amount += bet_amount
        elif cls.calculate_Value(player_Hand) == 21:
            print("player win")
            player_Amount += bet_amount
        elif cls.calculate_Value(dealer_Hand) == 21:
            print("dealer win")
            player_Amount -= bet_amount
        elif cls.calculate_Value(dealer_Hand) > cls.calculate_Value(player_Hand):
            print("dealer win")
            player_Amount -= bet_amount
        elif cls.calculate_Value(dealer_Hand) < cls.calculate_Value(player_Hand):
            print("player win")
            player_Amount += bet_amount
        print("Player amount: ", player_Amount)
        print("_" * 50)


while True:

    if player_Amount == 0:
        print("You have no enough chips")
        print("Thanks for playing!!!")
    else:
        print("\t\t\tWelcome to BlackJack")
        print("-"*50)
        player_Hand = []
        dealer_Hand = []
        bet_amount = 0

        game = BlackJack()
        game.gamePlay()
        new_game = input("Would you like to play again!!!\n Please enter 'y' for Yes or 'n' for Exit: ")
        if new_game[0].lower() == 'n':
            print("Thanks for playing")
            break
