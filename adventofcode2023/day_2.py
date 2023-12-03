from utils import extract_lines

SETUP_PART_ONE = {
    'red':12,
    'green':13,
    'blue':14
}

def get_game_max_values(game):
    separate_game_from_sets = game.split(':')[-1]
    raw_sets = separate_game_from_sets.split(';')
    game_max_values = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for raw_set in raw_sets:
        color_bunches = raw_set.strip().split(',')
        for color_bunch in color_bunches:
            number, color = color_bunch.strip().split(' ')
            if game_max_values[color] < int(number):
                game_max_values[color] = int(number)
    return game_max_values


def is_game_possible(game):
    game_max_values = get_game_max_values(game)
    for color in ['red', 'green', 'blue']:
        if game_max_values[color] > SETUP_PART_ONE[color]:
            return False    
    return True


def sum_of_valid_games(string_list=None):
    games = string_list or extract_lines('inputs/day_2.txt')
    sum_of_valid_games = 0
    for i, game in enumerate(games):
        if is_game_possible(game):
            sum_of_valid_games += (i+1)
    return sum_of_valid_games

# Part 2
def compute_game_points(game):
    game_max_values = get_game_max_values(game)
    points = game_max_values['red'] * game_max_values['blue'] * game_max_values['green']
    return points

def sum_of_game_points(string_list=None):
    games = string_list or extract_lines('inputs/day_2.txt')
    sum_of_game_points = 0
    for game in games:
        sum_of_game_points += compute_game_points(game)
    return sum_of_game_points

print(sum_of_valid_games())
print(sum_of_game_points())