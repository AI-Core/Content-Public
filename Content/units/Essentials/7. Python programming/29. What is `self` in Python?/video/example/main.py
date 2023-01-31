class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduce(self):
        print(f"I am {self.name} and I'm level {self.level}")

    def play(self):
        self.level += 1


player = Player('Harry', 100)
player.introduce()
player.play()
print('name:', player.name)
print('level:', player.level)

player2 = Player('Tamim', 101)
player3 = Player('Kiki', 300)
player3.play()
