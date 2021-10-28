import random


# input list of colored dice
# output list of 3 random dice
def choose_dice(available_dice):
    green_dice = ['footsteps', 'footsteps', 'brains', 'brains', 'brains', 'shotguns']
    red_dice = ['footsteps', 'footsteps', 'shotguns', 'shotguns', 'shotguns', 'brains']
    yellow_dice = ['footsteps', 'footsteps', 'shotguns', 'shotguns', 'brains', 'brains']
    chosen_dice = []

    while len(chosen_dice) < 3:
        dice_number = random.randint(0, len(available_dice) - 1)
        if available_dice[dice_number] == 'green':
            chosen_dice.append(green_dice)
            available_dice.remove('green')
        elif available_dice[dice_number] == 'yellow':
            chosen_dice.append(yellow_dice)
            available_dice.remove('yellow')
        else:
            chosen_dice.append(red_dice)
            available_dice.remove('red')
    return chosen_dice


# input is a list of 3 random dice
# output is a list of 1 side from each random dice
def rolling_dice(chosen_dice):
    rolled_dice_sides = []
    for dice in chosen_dice:
        dice_roll = random.randint(0, 5)
        rolled_dice_sides.append(dice[dice_roll])
    print(rolled_dice_sides)
    return rolled_dice_sides


# input is a list of rolled dice sides
# input specific player
# input dictionary to count
# output is a dictionary with brains and shotguns counts
def counting_brains_and_shotguns(rolled_dice_sides, player, player_dict):
    for dice_side in rolled_dice_sides:
        if dice_side == 'brains':
            player_dict[player + ' brains'] += 1
        elif dice_side == 'shotguns':
            player_dict[player + ' shotguns'] += 1
    print(player_dict)
    # return player_dict


# input is a dictionary with brains and shotguns counts
# processing shotguns and brains are reset to 0 when 3 shotguns are accumulated
# output a dictionary with brains and shotguns counts
def player_point_reset(player, player_dict):
    if player_dict[player + ' shotguns'] >= 3:
        player_dict[player + ' shotguns'] = 0
        player_dict[player + ' brains'] = 0
    # return player_dict


# input is player and dictionary with brains and shotgun counts
# processing check to see if player has >= 13 brains
# output True if player has >= 13 brains and False otherwise
def is_player_done(player, player_dict):
    if player_dict[player + ' brains'] >= 13:
        return True
    else:
        return False


# input dictionary of brains and shotguns counts
# processing check to see who has the most brains
# output print who won the game
def winning_player(player1, player2, player_dict):
    if player_dict[player1 + ' brains'] > player_dict[player2 + ' brains']:
        print('Player 1 wins!')
    elif player_dict[player1 + ' brains'] < player_dict[player2 + ' brains']:
        print('Player 2 wins!')
    else:
        print('Tie no one wins')


def change_player(curr_player, player1, player2):
    if curr_player == player1:
        print(player2)
        return player2
    else:
        print(player1)
        return player1


# main program
starting_dice = ['green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'yellow', 'yellow',
                 'yellow', 'yellow']
player_1 = 'p1'
player_2 = 'p2'
counting_brains_shotguns = {'p1 brains': 0, 'p1 shotguns': 0, 'p2 brains': 0, 'p2 shotguns': 0}

player = player_1
Player_available_dice = starting_dice.copy()
while True:
    print(player, str(len(Player_available_dice)) + ' available dice')
    if len(Player_available_dice) <= 0:
        player = change_player(player, player_1, player_2)
        Player_available_dice = starting_dice.copy()
    rolled_dice = rolling_dice(choose_dice(Player_available_dice))
    counting_brains_and_shotguns(rolled_dice, player, counting_brains_shotguns)
    if counting_brains_shotguns[player + ' shotguns'] >= 3:
        player_point_reset(player, counting_brains_shotguns)
        player = change_player(player, player_1, player_2)
        Player_available_dice = starting_dice.copy()
    if is_player_done(player, counting_brains_shotguns):
        player = change_player(player, player_1, player_2)
        Player_available_dice = starting_dice.copy()
        break
    print('Would you like to re-roll press 1 or pass press 2?')
    player_choice = input()
    if player_choice == '2':
        counting_brains_shotguns[player + ' shotguns'] = 0
        player = change_player(player, player_1, player_2)
        Player_available_dice = starting_dice.copy()

while len(Player_available_dice) > 0:
    print(player, str(len(Player_available_dice)) + ' available dice')
    rolled_dice = rolling_dice(choose_dice(Player_available_dice))
    counting_brains_and_shotguns(rolled_dice, player, counting_brains_shotguns)
    if counting_brains_shotguns[player + ' shotguns'] >= 3:
        player_point_reset(player, counting_brains_shotguns)
        break
    print('Would you like to re-roll press 1 or end turn press 2?')
    player_choice = input()
    if player_choice == '2':
        break

winning_player(player_1, player_2, counting_brains_shotguns)
print(counting_brains_shotguns)
# player 1 goes
# choose_dice()
# rolling_dice()
# counting_brains_and_shotguns()
# if player accumulates 3 shotguns player_point_reset()
# is_player_done() checks if player has >= 13 brains
# if is_player_done == True winning_player()
# if game proceeds player is asked if they would like to roll again or pass
