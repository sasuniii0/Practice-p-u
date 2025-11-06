"""Simple Tic-Tac-Toe CLI.

Features:
- Human vs Human
- Human vs Computer (Minimax AI)
- `--demo` mode to run a quick AI vs AI game for smoke tests

Run: python "AI/tic-tac-toe.py"
"""

import sys
import random
from typing import List, Optional, Tuple

BOARD_SIZE = 3


def new_board() -> List[List[str]]:
    return [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board: List[List[str]]) -> None:
    header = "   " + "   ".join(str(i + 1) for i in range(BOARD_SIZE))
    print(header)
    for i, row in enumerate(board):
        print(f"{i+1}  " + " | ".join(row))
        if i < BOARD_SIZE - 1:
            print("  " + "----" * BOARD_SIZE)


def check_winner(board: List[List[str]], player: str) -> bool:
    # rows
    for row in board:
        if all(s == player for s in row):
            return True
    # cols
    for c in range(BOARD_SIZE):
        if all(board[r][c] == player for r in range(BOARD_SIZE)):
            return True
    # diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    return False


def board_full(board: List[List[str]]) -> bool:
    return all(board[r][c] != " " for r in range(BOARD_SIZE) for c in range(BOARD_SIZE))


def get_empty_positions(board: List[List[str]]) -> List[Tuple[int, int]]:
    return [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == " "]


def minimax(board: List[List[str]], current: str, ai_player: str, human_player: str) -> Tuple[int, Optional[Tuple[int, int]]]:
    # returns (score, move)
    if check_winner(board, ai_player):
        return 1, None
    if check_winner(board, human_player):
        return -1, None
    if board_full(board):
        return 0, None

    best_move: Optional[Tuple[int, int]] = None
    if current == ai_player:
        best_score = -float("inf")
        for (r, c) in get_empty_positions(board):
            board[r][c] = current
            score, _ = minimax(board, human_player, ai_player, human_player)
            board[r][c] = " "
            if score > best_score:
                best_score = score
                best_move = (r, c)
        return best_score, best_move
    else:
        best_score = float("inf")
        for (r, c) in get_empty_positions(board):
            board[r][c] = current
            score, _ = minimax(board, ai_player, ai_player, human_player)
            board[r][c] = " "
            if score < best_score:
                best_score = score
                best_move = (r, c)
        return best_score, best_move


def get_ai_move(board: List[List[str]], ai_player: str, human_player: str) -> Tuple[int, int]:
    _, move = minimax(board, ai_player, ai_player, human_player)
    if move is None:
        # fallback
        return random.choice(get_empty_positions(board))
    return move


def get_user_move(board: List[List[str]]) -> Tuple[int, int]:
    while True:
        raw = input("Enter row and column (e.g. 2 3): ").strip()
        if not raw:
            print("Please enter row and column.")
            continue
        parts = raw.replace(',', ' ').split()
        if len(parts) != 2:
            print("Please enter two numbers separated by space or comma.")
            continue
        try:
            r = int(parts[0]) - 1
            c = int(parts[1]) - 1
        except ValueError:
            print("Invalid numbers. Use 1..3 for row and column.")
            continue
        if not (0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE):
            print(f"Numbers must be between 1 and {BOARD_SIZE}.")
            continue
        if board[r][c] != " ":
            print("That cell is already taken. Choose another.")
            continue
        return r, c


def play(interactive: bool = True) -> None:
    board = new_board()
    mode = None
    if interactive:
        print("Tic-Tac-Toe")
        print("1) Human vs Human")
        print("2) Human vs Computer")
        while True:
            mode = input("Choose mode (1 or 2): ").strip()
            if mode in ("1", "2"):
                break
            print("Please enter 1 or 2.")
    else:
        mode = "2"

    current = "X"
    ai_player = "O"
    human_player = "X"

    if mode == "2":
        if interactive:
            first = input("Do you want to go first? (y/n): ").strip().lower()
            if first and first[0] == 'n':
                human_player = "O"
                ai_player = "X"
                current = "X"
            else:
                human_player = "X"
                ai_player = "O"
                current = "X"
        else:
            # non-interactive demo: keep defaults (human X, ai O)
            human_player = "X"
            ai_player = "O"

    while True:
        print_board(board)
        if check_winner(board, "X"):
            print("X wins!")
            break
        if check_winner(board, "O"):
            print("O wins!")
            break
        if board_full(board):
            print("It's a tie!")
            break

        if mode == "1":
            print(f"Player {current}'s turn.")
            r, c = get_user_move(board)
        else:
            if current == human_player:
                print(f"Your turn ({human_player}).")
                r, c = get_user_move(board)
            else:
                print(f"Computer ({ai_player}) is thinking...")
                r, c = get_ai_move(board, ai_player, human_player)

        board[r][c] = current

        # switch
        current = "O" if current == "X" else "X"

    print_board(board)


def demo() -> None:
    # quick AI vs AI demo for smoke testing
    board = new_board()
    current = "X"
    ai_x = "X"
    ai_o = "O"
    while True:
        print_board(board)
        if check_winner(board, "X"):
            print("X wins!")
            break
        if check_winner(board, "O"):
            print("O wins!")
            break
        if board_full(board):
            print("It's a tie!")
            break
        if current == ai_x:
            r, c = get_ai_move(board, ai_x, ai_o)
        else:
            r, c = get_ai_move(board, ai_o, ai_x)
        board[r][c] = current
        current = "O" if current == "X" else "X"
    print("Demo finished.")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        try:
            play(interactive=True)
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")

