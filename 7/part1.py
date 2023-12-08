data = open("data.txt").readlines()
hands = []
sum = 0
def getType(card):
    card = [x for x in card]
    if all(x == card[0] for x in card):
        return 1
    elif card.count(card[0]) == 4 or card.count(card[1]) == 4: 
        return 2
    elif card.count(card[0]) == 3 or card.count(card[1]) == 3 or card.count(card[2]) == 3:
        if card.count(card[0]) == 2 or card.count(card[1]) == 2 or card.count(card[2]) == 2:
            return 3
        else:
            return 4
    elif card.count(card[0]) == 2 or card.count(card[1]) == 2 or card.count(card[2]) == 2 or card.count(card[3]) == 2:
        pairs = set()
        for i in card:
            if card.count(i) == 2:
                pairs.add(i)
        if len(pairs) == 2:
            return 5
        else:
            return 6
    else:
        return 7
for item in data:
    item = item.split(" ")
    hand = item[0]
    bid = item[1].strip("\n")
    hands.append([getType(hand), hand, bid])
hands.sort()
order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q","K", "A"]
for i in range(len(hands)):
    for j in range(len(hands) - 1):
        checked = False
        if hands[i][0] == hands[j][0]:
            for k in range(len(hands[i][1])):
                if order.index(hands[i][1][k]) < order.index(hands[j][1][k]):
                    hands[i], hands[j] = hands[j], hands[i]
                    checked = True
                if checked:
                    break
hands = hands[::-1]
for i in range(len(hands)):
    hands[i][0] = i + 1
    sum += hands[i][0] * int(hands[i][2])
print(hands, sum)
