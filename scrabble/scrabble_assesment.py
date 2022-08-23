# Calculate the score for a word. The score is the sum of the points for the letters that make up a word. For example: GUARDIAN = 2 + 1 + 1 + 1 + 2 + 1 + 1 + 1 = 10.
point_dict = {
}

def add_letter_to_dic(letters,value):
    for letter in letters:
        point_dict[letter] = value

add_letter_to_dic('EAIONRTLSU',1)
add_letter_to_dic('DG',2)
add_letter_to_dic('BCMP',3)
add_letter_to_dic('FHVWY',4)
add_letter_to_dic('K',5)
add_letter_to_dic('JX',8)
add_letter_to_dic('QZ',10)

def calculate_points_for_word(word): ## Guardian -- > G U A R D I A N
    upper_case_word = word.upper()
    word_lst = list(upper_case_word)
    counter = 0 
    for letter in word_lst:
        counter += point_dict[letter]
    return counter

# print(calculate_points_for_word('Guardian'))

bag = 'E'*12 + 'A'*9 + 'I'*9 + 'O'*8 + 'N'*6 + 'R'*6 + 'T'*6 + 4*('LSUD')+ 3*'G' + 2*('BCMPFHVWY') + 1* ('KJXQZ')
bag_list = list(bag)

import random

random.shuffle(bag_list)

player_hand = []

while len(player_hand)!= 7:
    player_hand.append(bag_list[0])
    bag_list.pop(0)

print(player_hand)


## Checking all permutation 

permutation = []

is_valid = False
#possible_word_list = [ahda ,faaufifd ,band ]
while not is_valid:
# for word in possible_wordlist
#   if word in dict 


## While loop 



    if word in word_dict:
        is_valid = True
    else:
        is_valid = False


# Assign seven tiles chosen randomly from the English alphabet to a player's rack.

# In the real game, tiles are taken at random from a 'bag' containing a fixed number of each tile. Assign seven tiles to a rack using a bag containing the above distribution.

# Find a valid word formed from the seven tiles. A list of valid words can be found in dictionary.txt.

# Find the longest valid word that can be formed from the seven tiles.

# Find the highest scoring word that can be formed.



# Find the highest scoring word if any one of the letters can score triple.
