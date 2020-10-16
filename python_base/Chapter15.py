# 棋牌游戏

# 定义扑克牌、牌堆、玩家和游戏四个类

# 卡牌类,数值相同，花色比大小，索引越小，花色越大

class Card:
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, s, v):
        """
        s,v 都是整数
        :param s:
        :param v:
        """
        self.suit = s
        self.value = v

    def __it__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


# c1 = Card(0, 2)
# c2 = Card(1, 3)
# print(c1)
# print(c1 < c2)

# 牌堆 deck of cards
# 将所有元素随机排列--模拟洗牌操作
from random import shuffle


# li = [1,2,33,4,455,6]
# shuffle(li)
# print(li)

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(j, i))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


deck = Deck()
for card in deck.cards:
    print(card)


# 玩家Player

class Player:
    def __init__(self, name):
        self.wins = 0
        # 手牌
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("p1 Name :\n")
        name2 = input("p2 Name :\n")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} win this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Begining War!!!\n")
        while len(cards) >= 2:
            m = "q to quit Any " + "key to play"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("War is over. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!!!"


# begin the war!!!

if __name__ == '__main__':
    game = Game()
    game.play_game()
