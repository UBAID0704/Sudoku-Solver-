import sys
from collections import deque
import copy
import time


def load_puzzle(source):
    if isinstance(source, str):
        with open(source) as fh:
            lines = [l.strip() for l in fh if l.strip()]
    else:
        lines = source

    assert len(lines) == 9
    board_domains = {}

    for row, line in enumerate(lines):
        assert len(line) == 9
        for col, ch in enumerate(line):
            digit = int(ch)
            board_domains[(row, col)] = {digit} if digit != 0 else set(range(1, 10))

    return board_domains


def print_board(board_domains):
    sep = "+-------+-------+-------+"
    lines = [sep]

    for row in range(9):
        row_str = "| "
        for col in range(9):
            domain = board_domains[(row, col)]
            value = str(next(iter(domain))) if len(domain) == 1 else "."
            row_str += value + (" | " if col % 3 == 2 else " ")
        lines.append(row_str)
        if row % 3 == 2:
            lines.append(sep)

    return "\n".join(lines)


def _compute_neighbors(row, col):
    neighbors = set()

    for c in range(9):
        if c != col:
            neighbors.add((row, c))

    for r in range(9):
        if r != row:
            neighbors.add((r, col))

    box_r, box_c = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if (r, c) != (row, col):
                neighbors.add((r, c))

    return frozenset(neighbors)


NEIGHBORS = {
    (r, c): _compute_neighbors(r, c)
    for r in range(9)
    for c in range(9)
}


def revise_constraint(board_domains, square_i, square_j):
    revised = False

    for digit in list(board_domains[square_i]):
        if all(other == digit for other in board_domains[square_j]):
            board_domains[square_i].discard(digit)
            revised = True

    return revised


def ac3_solver(board_domains):
    queue = deque(
        (square_i, square_j)
        for square_i in NEIGHBORS
        for square_j in NEIGHBORS[square_i]
    )

    while queue:
        square_i, square_j = queue.popleft()

        if revise_constraint(board_domains, square_i, square_j):
            if len(board_domains[square_i]) == 0:
                return False

            for square_k in NEIGHBORS[square_i]:
                if square_k != square_j:
                    queue.append((square_k, square_i))

    return True


_bt_calls = 0
_bt_failures = 0


def select_unassigned_square(board_domains):
    unassigned = [
        (len(domain), square)
        for square, domain in board_domains.items()
        if len(domain) > 1
    ]

    if not unassigned:
        return None

    return min(unassigned)[1]


def is_solved(board_domains):
    return all(len(domain) == 1 for domain in board_domains.values())


def solve_backtracking(board_domains):
    global _bt_calls, _bt_failures
    _bt_calls += 1

    if is_solved(board_domains):
        return board_domains

    square = select_unassigned_square(board_domains)

    if square is None:
        return None

    for digit in sorted(board_domains[square]):
        new_board = copy.deepcopy(board_domains)
        new_board[square] = {digit}

        forward_check = True
        for neighbor in NEIGHBORS[square]:
            new_board[neighbor].discard(digit)
            if len(new_board[neighbor]) == 0:
                forward_check = False
                break

        if not forward_check:
            _bt_failures += 1
            continue

        if not ac3_solver(new_board):
            _bt_failures += 1
            continue

        result = solve_backtracking(new_board)
        if result is not None:
            return result

    _bt_failures += 1
    return None


def solve(label, source):
    global _bt_calls, _bt_failures
    _bt_calls = 0
    _bt_failures = 0

    board_domains = load_puzzle(source)

    if not ac3_solver(board_domains):
        print(f"\n{label}: Unsolvable — initial AC-3 wiped a domain.")
        return None

    start_time = time.perf_counter()
    result = solve_backtracking(board_domains)
    elapsed = (time.perf_counter() - start_time) * 1000

    print(f"\n{'='*52}")
    print(f"  {label}")


    if result:
        print(print_board(result))
    else:
        print("  No solution found.")

    print(f"\n  BACKTRACK calls    : {_bt_calls}")
    print(f"  BACKTRACK failures : {_bt_failures}")
    print(f"  Time               : {elapsed:.1f} ms\n")

    return result


EASY = [
    "004030050",
    "609400000",
    "005100489",
    "000060930",
    "300807002",
    "026040000",
    "453009600",
    "000004705",
    "090050200",
]

MEDIUM = [
    "530070000",
    "600195000",
    "098000060",
    "800060003",
    "400803001",
    "700020006",
    "060000280",
    "000419005",
    "000080079",
]

HARD = [
    "800000000",
    "003600000",
    "070090200",
    "060005030",
    "004010700",
    "010400600",
    "009200050",
    "000080040",
    "300001090",
]

VERY_HARD = [
    "000000010",
    "040030602",
    "000500000",
    "010070500",
    "700000300",
    "003010080",
    "000900006",
    "080100040",
    "500002007",
]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        solve(sys.argv[1], sys.argv[1])
    else:
        solve("Easy", EASY)
        solve("Medium", MEDIUM)
        solve("Hard", HARD)
        solve("Very Hard", VERY_HARD)