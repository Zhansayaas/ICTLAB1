# 138
# import random
#
#
# def get_bingo_card():
#     gridSize = 5
#
#     bingo_card = {}
#     randRange = range(1, 15)
#     values = random.sample(randRange, gridSize)
#     bingo_card['B'] = values
#
#     values = []
#     randRange = range(16, 30)
#     values = random.sample(randRange, gridSize)
#     bingo_card['I'] = values
#
#     values = []
#     randRange = range(31, 45)
#     values = random.sample(randRange, gridSize)
#     bingo_card['N'] = values
#
#     values = []
#     randRange = range(46, 60)
#     values = random.sample(randRange, gridSize)
#     bingo_card['G'] = values
#
#     values = []
#     randRange = range(61, 75)
#     values = random.sample(randRange, gridSize)
#     bingo_card['O'] = values
#
#     return bingo_card
#
#
# def print_bingo_card(card):
#     head = ['B', 'I', 'N', 'G', 'O']
#     print('\t'.join(head))
#
#     for i in range(0, 5):
#         tmplist = []
#         for h in head:
#             tmplist.append(str(card[h][i]))
#         print('\t'.join(tmplist))
#
#
# print_bingo_card(get_bingo_card())

# 139
# def check_bingo(card):
#     head = ['B', 'I', 'N', 'G', 'O']
#     # check vertical line
#     for h in head:
#         sum = 0
#         for i in card[h]:
#             sum = sum + i
#         if sum == 0:
#             return True
#
#     # check horizontal line
#     for i in range(0, 5):
#         sum = 0
#         for h in head:
#             sum = sum + card[h][i]
#         if sum == 0:
#             return True
#
#     # check diagonal line
#     sum = card['B'][0] + card['I'][1] + card['N'][2] + card['G'][3] + card['O'][4]
#     if sum == 0:
#         return True
#     # check another diagonal line
#     sum = card['B'][4] + card['I'][3] + card['N'][2] + card['G'][1] + card['O'][0]
#     if sum == 0:
#         return True
#
#     return False
#
#
# def print_bingo(card):
#
#     head = ['B', 'I', 'N', 'G', 'O']
#     print('\t'.join(head))
#
#     for i in range(0, 5):
#         tmplist = []
#         for h in head:
#             tmplist.append(str(card[h][i]))
#         print('\t'.join(tmplist))
#     print("\n")
#
#
# def main():
#     card = {'B': [7, 15, 11, 2, 10],
#             'I': [25, 22, 30, 28, 27],
#             'N': [44, 40, 0, 37, 39],
#             'G': [57, 50, 46, 55, 59],
#             'O': [62, 70, 74, 68, 75]}
#
#     print_bingo(card)
#     if check_bingo(card):
#         print("contain a winning line")
#     else:
#         print("No Luck!")
#
#     card = {'B': [0, 0, 0, 0, 0],
#             'I': [25, 22, 30, 28, 27],
#             'N': [44, 40, 0, 37, 39],
#             'G': [57, 50, 46, 55, 59],
#             'O': [62, 70, 74, 68, 75]}
#     print_bingo(card)
#     if check_bingo(card):
#         print("contain a winning line")
#     else:
#         print("No Luck!")
#
#     card = {'B': [7, 0, 11, 2, 10],
#             'I': [25, 0, 30, 28, 27],
#             'N': [44, 0, 0, 37, 39],
#             'G': [57, 0, 46, 55, 59],
#             'O': [62, 0, 74, 68, 75]}
#     print_bingo(card)
#     if check_bingo(card):
#         print("contain a winning line")
#     else:
#         print("No Luck!")
#
#     card = {'B': [0, 15, 11, 2, 10],
#             'I': [25, 0, 30, 28, 27],
#             'N': [44, 40, 0, 37, 39],
#             'G': [57, 50, 46, 0, 59],
#             'O': [62, 70, 74, 68, 0]}
#     print_bingo(card)
#     if check_bingo(card):
#         print("contain a winning line")
#     else:
#         print("No Luck!")
#
#
# if __name__ == "__main__":
#     main()

# 140
# import random


# def get_bingo_card():
#     gridSize = 5

#     bingo_card = {}
#     randRange = range(1, 15)
#     values = random.sample(randRange, gridSize)
#     bingo_card['B'] = values

#     values = []
#     randRange = range(16, 30)
#     values = random.sample(randRange, gridSize)
#     bingo_card['I'] = values

#     values = []
#     randRange = range(31, 45)
#     values = random.sample(randRange, gridSize)
#     bingo_card['N'] = values

#     values = []
#     randRange = range(46, 60)
#     values = random.sample(randRange, gridSize)
#     bingo_card['G'] = values

#     values = []
#     randRange = range(61, 75)
#     values = random.sample(randRange, gridSize)
#     bingo_card['O'] = values

#     return bingo_card


# def check_for_bingo_value(val):
#     cur_bingo_card = get_bingo_card()
#     for i in cur_bingo_card:
#         if int(val[1:]) in cur_bingo_card[i]:
#             print(cur_bingo_card[i][int(val[1:])])
#             cur_bingo_card[i][int(val[1:])] = 0
#     print_bingo_card(cur_bingo_card)


# def print_bingo_card(card):
#     head = ['B', 'I', 'N', 'G', 'O']
#     print('\t'.join(head))

#     for i in range(0, 5):
#         tmplist = []
#         for h in head:
#             tmplist.append(str(card[h][i]))
#         print('\t'.join(tmplist))


# check_for_bingo_value("B5")
