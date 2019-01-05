table_card = input()
hand_cards = input().split(" ")

a = ['D','C','S','H']
deck = set(a)
b = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
cards = set(b)
count = 0

for i in range(5):
    if hand_cards[i][0]==table_card[0] or hand_cards[i][1] == table_card[1]:
        count += 1
if count > 0:
    print("YES")
else:
    print("NO")
