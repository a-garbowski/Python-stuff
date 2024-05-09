import random

loteria = [1, "a", 2, 3, 4, "b", "c", 5, 6, "d", 7, 8, 9, "e", 10]
lottery = tuple(loteria)
print(lottery)

winning_symbols = random.sample(lottery, 4)
print(f"Zwycięskie liczby i/lub litery to: {winning_symbols}")

my_ticket = [2, 3, "b", 5]
iterations = 0
while True:
    iterations += 1
    drawn_symbols = random.sample(lottery, 4)
    if drawn_symbols == winning_symbols:
        break

print(f"Aby dopasować numery na Twoim kuponie, potrzebne było {iterations} losowań.")
print(drawn_symbols)
