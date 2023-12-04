data = open("data.txt").readlines()

deckSum = 0
for card in data:
    card = card.split(":")[1].strip().split("|")
    cardSum = 0
    matching = 0
    for num in card[0].split(" "):
        for yourNum in card[1].split(" "):
            if yourNum.isdigit() and num.isdigit():
                if int(yourNum) == int(num):
                    matching += 1
    if matching:
        cardSum += 1
        for i in range(matching - 1): cardSum *= 2
    deckSum += cardSum
print(deckSum)
