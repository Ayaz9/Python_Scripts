
'''
 - Create 3 common dictionaries 
    #1 - game_players -  we store all information (game_information and only_game_players)
    #2 - game_information - no player info, only  players, courts, group_games, total_games, rest_available_games
    #3 - only_game_players - only games and players list
 - Get user inputs:
    #1 - users list
    #2 - game time 
    #3 - courts 
 - Creating one common users' groups list. Note we add each team from each created list per player - each_user_game
 - Finding how many group games and how much time per group game we have
    #1 - group_games
    #2 - each_game_time
 - Adding some game information to the dictionary game_players
    #1 - players_count
    #2 - courts
    #3 - group_games
    #4 - each_game_time
 - This function first_rest_teams_func() helps to find out below information: 
    #1 - first_team
    #2 - rest_possible_players
    #3 - pty_list
 - With this function we find second and the rest possible group games
 - This function group_game_float() determines: 
    #1 - if the group_games is the full number (e.g. 13), then group_games = (Total games)/Courts
    #2 - if the group_games is the full number (e.g. 13.5), then group_games = (Total games)/Courts + 1
 - This is our main function for putting the whole picture of this code - run()
    #1 - Determine how many group games will be, collecting the group games to the dictionary main_dict (game_players)
 - With this function run_logic(), we first determine if we have enough players to play (or execute run())
    #1 - players_count/2 >= courts --> there are enough players to play the game, meaning players are greater or equal to the courts 
    #2 - len(players_input)/2 < courts  --> there are not enough players to start the game, meaning players are less than courts
 - We start the loop here. The goal to start loop is to make sure our dict  game_players['rest_available_games'] contains zero players. 
    #1 - we do not have enough players to star the game, collect the players, which means game_players['less_players'] = 'Less Players for the availabe courts'
    #2 - we have enough players, then 
        * we loop until game_players['rest_available_games'] = False or game_players['rest_available_games'] = []
        * we collect only players to only_game_players dictionary
        * we collect only general game information to game_information dictionary

'''
import random

# Three common dictionaries, explained above for what they are
game_players = {}
only_game_players = {}
game_information = {}

# User inputs
players_input = ['Ayaz', 'Aslan','Orxan', 'Ayxan', 'Hatem', 'Aga', 'Jack', 'Virginia', 'Rayan', 'Alessandro', 'Kaylan', 'Cheyenne', 'Amara', 'Vlad', 'Benedict']
# players_input = ['Ayaz', 'Aslan','Orxan', 'Ayxan', 'Hatem', 'Aga']
# players_input = []  # not handled. Handle directly in the project 
time_input = 130
courts = 4
# User input - END

# Useful counts we use during the functions execution
manual_loop = len(players_input) - 1
players_count = len(players_input)
rest_courts = range(courts - 2)
# Useful counts we use during the functions execution - END

# Add all players into one list, where each team is selected from each group
all_games = []
my_dict = {}
def per_user_game(plyr_list):
    games = []
    m = 1
    while m < len(plyr_list):
        if plyr_list[m]:
            games.append(f'{plyr_list[0]}-{plyr_list[m]}')
        else: 
            break
        m += 1
    return games


for i in range(len(players_input)-1):
    if i == players_input[-1]:
        break
    each_user_game = per_user_game(players_input)
    my_dict['key_' + str(i)] = each_user_game
    del players_input[0]


for i in range(len(my_dict['key_0'])):
    for key in my_dict.keys():
        try: 
            all_games.append(my_dict[key][i])
            # print(my_dict[key][i])
        except IndexError:
            continue            

# print(all_games)
# Add all players into one list, where each team is selected from each group - END

# Find how many group games and how many minutes we have
group_games = len(all_games) / courts
each_game_time = format(time_input / group_games, '.2f')
# Find how many group games and how many minutes we have - END

# print(f'Players : {players_count}')
# print(f'Courts : {courts}')
# print(f'Total games : {len(all_games)}')
# print(f'Group games : (Total games)/Courts = {group_games}')

# Adding initial game information to dictionary game_players
game_players['players'] = f'Players : {players_count}'
game_players['courts'] = f'Courts : {courts}'
game_players['total_teams'] = f'Total teams {len(all_games)}'
game_players['group_games'] = f'Group games : (Total games)/Courts = {group_games}'
game_players['each_group_time'] = f'Each group game time : {each_game_time} mins'
game_players['less_players'] = False
game_players['rest_available_games'] = False
# Adding game information to dictionary game_players - END

# Split by "-"
def split_dash(pair):
    splitted = pair.split('-')
    return splitted


# Remove players (E.g. Ayaz-Aslan) from the requested list
def remove_index(ind, pty_list):
    remove_id = pty_list.index(ind)
    del pty_list[remove_id]


# print(split_dash('Ayaz-Aslan'))

# Find first team, rest possible players, and rest available games
def first_rest_teams_func(pty_list):
    first_team = pty_list[0]
    # print(first_team)
    del pty_list[0]
    # Split the names (E.g. Ayaz-Aslan --> Ayaz, Aslan)
    names = split_dash(first_team)
    # Find out which group players do not include names[0] and names[1]
    rest_possible_players = []
    for ele in pty_list:
        if names[0] in ele or names[1] in ele:
            continue
        else:
            # print(f'Element : {ele}')
            rest_possible_players.append(ele)
    # First team - first_team, Rest possible players - rest_possible_players, Rest availabe games - pty_list (all_games)
    return first_team, rest_possible_players, pty_list

# Second and rest players, depending on courts count
def rest_team(rest_players, pty_list, dict_key):
    random.shuffle(pty_list)
    # print(f'Reversed : {pty_list}')
    if courts == 2: 
        second_team = rest_players[0]
        # print(second_team)
        dict_key.append(rest_players[0])
        splitted = split_dash(second_team)
        remove_index(second_team, pty_list)
        # remove_index(second_team, rest_players)
    if courts > 2:
        second_team = rest_players[0]
        # print(second_team)
        dict_key.append(rest_players[0])
        splitted = split_dash(second_team)
        remove_index(second_team, pty_list)
        remove_index(second_team, rest_players)

        for i in rest_courts:
            for ele in rest_players:
                if splitted[0] in ele or splitted[1] in ele:
                    continue
                else:
                    # print(ele)
                    dict_key.append(ele)
                    remove_index(ele, pty_list)
                    remove_index(ele, rest_players)
                    break
                    # return 
                    # print(f'Rest {rest_players}')


# Determines if the group_games is full (e.g. 13), or not (e.g. 13.5)
def group_game_float():
    edit_group_games = str(group_games).split('.')
    if len(edit_group_games) >= 2 and int(edit_group_games[1]) != 0:
        return False
    else:
        return True


# Determine how many group games will be, collecting the group games to the dictionary main_dict (game_players)
def run(group_games_count, pty_list, main_dict):
    # print(f'Total GAMES will be : {group_games_count} \n')
    main_dict['total_group_games'] = f'Total Games will be : {group_games_count}'
    for i in range(group_games_count): # How many games
        # print(f'GAME #{i+1}')
        # game_players[f'Game_#{i+1}']
        if pty_list:
            first_rest_teams = first_rest_teams_func(pty_list)
            # print(first_rest_teams[0])
            main_dict[f'Game_#{i+1}'] = [first_rest_teams[0]]
            # print(f'Rest Team : {i}')
            if first_rest_teams[1]:
                rest_team(first_rest_teams[1], pty_list, main_dict[f'Game_#{i+1}'])
            # print('\n')
    # print(f'Rest Available Games: \n {pty_list}')

    # Determines if there are availabe games left
    main_dict['rest_available_games'] = pty_list
    

# Logic how we run main function - run() 
def run_logic():
    # Enough players for the given courts
    if players_count/2 >= courts:
        # print(f'All Games: \n {all_games} \n')
        # print(group_game_float())
        if group_game_float():
            run(int(group_games), all_games, game_players)
        else:
            # print(group_game_float())
            run(int(group_games) + 1, all_games, game_players)  
    # Less players for the given courts
    elif len(players_input)/2 < courts:
        # print('Less Players for the courts')
        game_players['less_players'] = 'Less Players for the availabe courts'

# for key, value in game_players.items(): print(key + ' : ', value)

# Logic how we run main function (run()) - END

# Starting the loop,details are on top comments
while True:
    run_logic()
    # Less players and more courts - elif of run_logic() matched
    if game_players['less_players'] != False:  
        for key, value in game_players.items():
            game_information[key] = value
        break

    # Enough players to play - if block of run_logic() matched
    else: 
        # Continue to loop until 0 players left in "rest_available_games" (if condition)
        if game_players['rest_available_games']:
            continue
        else:
            for key, value in game_players.items(): 
                if 'Game_#' in key:
                    only_game_players[key] = value
                # print(key + ' : ', value)
                else:
                    game_information[key] = value
            break

# Starting the loop,details are on top comments - END

# Printing game_information and only_game_players dictionaries 
print('\n**************************************\n')
for key, value in game_information.items(): print(f'{key} : {value}')
print('\n**************************************\n')
for key, value in only_game_players.items(): print(f'{key} : {value}')
print('\n**************************************\n')
# Printing game_information and only_game_players dictionaries - END