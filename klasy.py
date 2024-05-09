from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        r_num = randint(1, self.sides)
        print(r_num)

    def rzut_koscia(self):
      for i in range(10):
          self.roll_die()

kosc = Die()
kosc.rzut_koscia()

print(f"\n")

xkosc = Die(10)
xkosc.rzut_koscia()

print(f"\n")

xxkosc = Die(20)
xxkosc.rzut_koscia()