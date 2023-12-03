import adventofcode2023.day_2 as day_2

def test_is_game_possible():
    assert day_2.is_game_possible('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    assert day_2.is_game_possible('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')
    assert not day_2.is_game_possible('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red')
    assert not day_2.is_game_possible('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red')
    assert day_2.is_game_possible('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')

def test_sum_valid_games():
    assert day_2.sum_of_valid_games(
        [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]
    ) == 8

def test_compute_game_points():
    assert day_2.compute_game_points('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green') == 48
    assert day_2.compute_game_points('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue') == 12
    assert day_2.compute_game_points('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red') == 1560
    assert day_2.compute_game_points('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red') == 630
    assert day_2.compute_game_points('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green') == 36

def test_sum_of_game_points():
    assert day_2.sum_of_game_points(
        [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
        ]
    ) == 2286