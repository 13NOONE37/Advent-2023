file = open('input.txt','r')
lines = file.readlines()
num_of_hands = len(lines)

def is_five_of_kind(hand):
    chars = set(hand)
    if len(chars)==1:
        return True
    return False

def is_four_of_kind(hand):
    chars = list(set(hand))
    if len(chars)==2:
        counts = [
        hand.count(chars[0]),
        hand.count(chars[1]) 
        ]
        if 4 in counts and 1 in counts:
            return True
    return False

def is_full_house(hand):
    chars = list(set(hand))
    if len(chars)==2:
        counts = [
        hand.count(chars[0]),
        hand.count(chars[1]) 
        ]
        if 3 in counts and 2 in counts:
            return True
    return False

def is_three_of_kind(hand):
    chars = list(set(hand))
    if len(chars)==3:
        counts = [
        hand.count(chars[0]),
        hand.count(chars[1]),
        hand.count(chars[2])      
        ]
        
        if counts.count(1)==2 and 3 in counts:
            return True
    return False

def is_two_pair(hand):
    chars = list(set(hand))
    if len(chars)==3:
        counts = [
        hand.count(chars[0]),
        hand.count(chars[1]),
        hand.count(chars[2])      
        ]
        
        if 1 in counts and counts.count(2)==2:
            return True
    return False

def is_one_pair(hand):
    chars = list(set(hand))
    if len(chars)==4:
        counts = [
        hand.count(chars[0]),
        hand.count(chars[1]),
        hand.count(chars[2]),
        hand.count(chars[3])     
        ]
        
        if 2 in counts and counts.count(1)==3:
            return True
    return False

def is_high_card(hand):
    chars = set(hand)
    if len(chars)==5:
        return True
    return False

labels_strength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
hands_order = [is_five_of_kind,is_four_of_kind,is_full_house,is_three_of_kind,is_two_pair,is_one_pair,is_high_card]
hands_container=[[],[],[],[],[],[],[]]

def find_kind_of_hand(hand):
    if 'J' in hand:
        highest_container=[[],[],[],[],[],[],[]]
        for char in set(hand):
            if char=='J': continue
            replaced_hand = hand.replace('J',char)

            for i in range(0,len(hands_order)):
                if hands_order[i](replaced_hand):
                    hand_values = []
                    for char in replaced_hand:
                        hand_values.append(labels_strength.index(char))
                    highest_container[i].append((hand_values,i))

        highest_hand = 0

        for hands in highest_container:
            if len(hands)>0:
                hands=sorted(hands, key=lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
                highest_hand=hands[0][1]


                break
        return highest_hand

    else:
        for i in range(0,len(hands_order)):
            if hands_order[i](hand):
                return i

for line in lines:
    hand, bid = line.split(' ')
    bid = int(bid)
    index_of_container = find_kind_of_hand(hand)

    hand_values = []
    for char in hand:
        hand_values.append(labels_strength.index(char))
    hands_container[index_of_container].append({'hand':hand_values,'bid':bid,})


total=0
for hands in hands_container:
    sorted_hands = sorted(hands, key=lambda x: (x['hand'][0],x['hand'][1],x['hand'][2],x['hand'][3],x['hand'][4]))
    for hand in sorted_hands:
        total+=num_of_hands*hand['bid']
        num_of_hands-=1
        
print(f'The result is {total}')
file.close()