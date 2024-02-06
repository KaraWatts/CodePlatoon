import pytest
from tic_tac_toe import *

def test_valid_coordinates():
    # Test valid coordinates
    assert is_valid_coordinates(0, 0) == True
    assert is_valid_coordinates(1, 1) == True
    assert is_valid_coordinates(2, 2) == True

    # Test coordinates out of range
    assert is_valid_coordinates(-1, 0) == False
    assert is_valid_coordinates(0, -1) == False
    assert is_valid_coordinates(3, 0) == False
    assert is_valid_coordinates(0, 3) == False

    # Test non-integer coordinates
    assert is_valid_coordinates('a', 'b') == False




def test_computer_win_in_3_moves():
    # Define a sequence of moves for a game where the computer wins in 3 moves
    moves = [
        ((0, 0), (0, 1)),  # Human player moves to (0, 0), computer player moves to (0, 1)
        ((1, 1), (0, 2)),  # Human player moves to (1, 1), computer player moves to (0, 2)
        ((2, 2), (1, 0)),  # Human player moves to (2, 2), computer player moves to (1, 0)
    ]

    # Run the Tic-Tac-Toe game with the predetermined sequence of moves
    for human_move, computer_move in moves:
        play_tic_tac_toe(human_move=human_move, computer_move=computer_move)
    
    # Assert that the final state of the board indicates the computer wins
    expected_output = "Computer wins!"
    assert expected_output in captured.out

def test_board_printout(capfd):
    # Test board printout
    for i in range(3):
        Board[i][i] = X
    print_board()
    captured = capfd.readouterr()
    assert captured.out == "| X |   |   |\n-------------\n|   | X |   |\n-------------\n|   |   | X |\n"

def test_cats_game_scenario(monkeypatch, capfd):
    # Test Cat's game scenario
    monkeypatch.setattr('random.randint', lambda _, __: 2)
    play_tic_tac_toe()
    captured = capfd.readouterr()
    assert "Cat's Game!" in captured.out

def test_player_win_scenario(monkeypatch, capfd):
    # Test player win's scenario
    Board[0][0] = X
    Board[1][1] = X
    Board[2][2] = X
    monkeypatch.setattr('random.randint', lambda _, __: 1)
    play_tic_tac_toe()
    captured = capfd.readouterr()
    assert "You win!" in captured.out

def test_player_loses_scenario(monkeypatch, capfd):
    # Test player loses scenario
    Board[0][0] = O
    Board[1][1] = O
    Board[2][2] = O
    monkeypatch.setattr('random.randint', lambda _, __: 1)
    play_tic_tac_toe()
    captured = capfd.readouterr()
    assert "You win!" not in captured.out
    assert "Cat's Game!" not in captured.out

