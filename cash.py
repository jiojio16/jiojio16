from cs50 import get_float
while True:
#ask user for input
    cash = get_float("change owed:")
    if cash >= 0:
        break
# Convert cents to int
cents = round(cash * 100)
coins = 0
#quarters
while (cents >=25):
    coins += 1
    cents -= 25
#dimes
while (cents >= 10):
    coins += 1
    cents -= 10
#nickels
while (cents >= 5):
    coins += 1
    cents -= 5
#pennies
while (cents >= 1):
    coins += 1
    cents -= 1
print (coins)