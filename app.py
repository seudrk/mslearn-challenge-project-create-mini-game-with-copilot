# write 'hello world' to the console
# print('hello world')
import random

# Define moves and their respective wins/losses
moves = ['R', 'S', 'P']
win_conditions = {
    'R': {'R':0, 'S': 1, 'P': -1},
    'S': {'S':0, 'P': 1, 'R': -1},
    'P': {'P':0, 'R': 1, 'S': -1}
}

# print(win_conditions['R']['P'])

def get_random_move():
    return random.choice(moves)

def compare_moves(player_move, algo_move):
    if player_move == algo_move:
        return 0  # Tie
    elif win_conditions[player_move][algo_move] == -1:
        return -1  # Player win
    elif win_conditions[player_move][algo_move] == 1:
        return 1  # Algorithm win

def play_game():
    player_move = input("Choose your move (R/S/P): ")
    algo_move = get_random_move()
    result = compare_moves(player_move, algo_move)
    print(f"Algorithm's move: {algo_move}")
    print(f"Comparing moves:")
    print(f"  Your move: {player_move}")
    print(f"  Algorithm's move: {algo_move}")
    if result == 0:
        print("It's a tie! Well played!")
    elif result > 0:
        print("You won!")
    else:
        print("The algorithm won.")
    return result

play_game()