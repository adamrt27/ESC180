import gomoku as g

GREEN = "\x1b[1;30;42m"
RED = "\x1b[1;30;41m"
MAGENTA = "\x1b[1;30;45m"
END = "\x1b[0m"

PRINT_BOARD_ALWAYS = False


def test_detect_rows(size, insertions, solutions):
    fail = False
    board = g.make_empty_board(size)

    for i in insertions:
        g.put_seq_on_board(board, i[0], i[1], i[2], i[3], i[4], i[5])
        # put_seq_on_board(board, y, x, d_y, d_x, length, col)

    for i in solutions:
        test = g.detect_rows(board, i[0], i[1])
        if test == i[2]:
            print(
                f'{i[0]} {i[1]} {GREEN}PASSED:{END} {test} | {i[2]}')
        else:
            print(
                f'{i[0]} {i[1]} {RED}FAILED:{END} {test} | {i[2]}')
            fail = True
    if PRINT_BOARD_ALWAYS or fail:
        print('color length status received expected')
        g.print_board(board)


def test_is_win(size, insertions, solution):
    fail = False
    board = g.make_empty_board(size)

    for i in insertions:
        g.put_seq_on_board(board, i[0], i[1], i[2], i[3], i[4], i[5])
        # put_seq_on_board(board, y, x, d_y, d_x, length, col)

    test = g.is_win(board)
    if test == solution:
        print(
            f'{GREEN}PASSED:{END} {test} | {solution}')
    else:
        print(
            f'{RED}FAILED:{END} {test} | {solution}')
        fail = True
    if PRINT_BOARD_ALWAYS or fail:
        g.print_board(board)

# put_seq_on_board(board, y, x, d_y, d_x, length, col)


class detect_rows_cases:
    case1 = (((1, 5, 1, 0, 3, 'w'),
              (0, 0, 0, 1, 4, 'b'),
              (3, 1, 1, 1, 3, 'w'),
              (4, 7, 1, -1, 3, 'b')
              ),
             (('w', 3, (2, 0)),
              ('b', 4, (0, 1)),
              ('b', 3, (0, 1)),
              ))

    case2 = (((1, 1, 0, 1, 2, 'w'),
              (2, 1, 0, 1, 2, 'w')
              ),
             (('w', 2, (6, 0)),
              ))

    case3 = (((1, 5, 0, 1, 2, 'b'),
              (2, 5, 0, 1, 2, 'b')),
             (('b', 2, (6, 0)),
              ))

    case4 = (((5, 5, 0, 1, 2, 'b'),
              (6, 5, 0, 1, 2, 'b')),
             (('b', 2, (6, 0)),
              ))

    case5 = (((5, 1, 0, 1, 2, 'b'),
              (6, 1, 0, 1, 2, 'b')),
             (('b', 2, (6, 0)),
              ))

    case6 = (((0, 0, 0, 1, 8, 'w'),
              (1, 0, 0, 1, 8, 'w'),
              (2, 0, 0, 1, 8, 'w'),
              (3, 0, 0, 1, 8, 'w'),
              (4, 0, 0, 1, 8, 'w'),
              (5, 0, 0, 1, 8, 'w'),
              (6, 0, 0, 1, 8, 'w'),
              (7, 0, 0, 1, 8, 'w')),
             (('w', 8, (0, 0)),
              ('w', 7, (0, 0)),
              ('w', 6, (0, 0)),
              ('w', 5, (0, 0)),
              ('w', 4, (0, 0)),
              ))
    case7 = (((0, 0, 0, 1, 2, 'w'),
              (0, 3, 0, 1, 2, 'w')),
             (('w', 2, (1, 1)),
              ))

    cases = (case1, case2, case3, case4, case5, case6, case7)


class is_win_cases:
    case1 = ((
        (0, 0, 1, 0, 5, 'w'),
        (4, 2, 1, 1, 2, 'b')
    ), "White won")
    case2 = ((
        (0, 0, 1, 0, 1, 'b'),
    ), "Continue playing")
    case3 = ((
        (0, 0, 0, 1, 8, 'w'),
        (1, 0, 0, 1, 8, 'w'),
        (2, 0, 0, 1, 8, 'w'),
        (3, 0, 0, 1, 8, 'w'),
        (4, 0, 0, 1, 8, 'w'),
        (5, 0, 0, 1, 8, 'w'),
        (6, 0, 0, 1, 8, 'w'),
        (7, 0, 0, 1, 8, 'w')
    ), "White won")
    case4 = ((
        (1, 7, 1, -1, 5, 'b'),
    ), "Black won")
    case5 = ((
        (3, 0, 1, 1, 5, 'b'),
    ), "Black won")
    case6 = ((
        (0, 4, 1, -1, 5, 'w'),
    ), "White won")
    case7 = ((
        (0, 2, 1, 1, 5, 'w'),
    ), "White won")
    case8 = ((
        (0, 2, 1, 1, 6, 'w'),
    ), "Continue playing")
    case9 = ((
        (0, 0, 0, 1, 8, 'w'),
        (1, 0, 0, 1, 8, 'b'),
        (2, 0, 0, 1, 8, 'w'),
        (3, 0, 0, 1, 8, 'b'),
        (4, 0, 0, 1, 8, 'w'),
        (5, 0, 0, 1, 8, 'b'),
        (6, 0, 0, 1, 8, 'w'),
        (7, 0, 0, 1, 8, 'b')
    ), "Draw")
    case10 = ((
        (1, 1, 0, 1, 2, 'w'),
        (1, 4, 0, 1, 2, 'w'),
        (3, 3, 1, 0, 4, 'b'),
        (2, 6, 1, -1, 6, 'w'),
        (3, 5, 1, -1, 4, 'b'),
    ), "Continue playing")
    case11 = ((
        (1, 5, 1, 0, 5, 'b'),
    ), "Black won")

    cases = (case1, case2, case3, case4, case5,
             case6, case7, case8, case9, case10, case11)


print(f'{MAGENTA}detect_row cases{END}')

for case in detect_rows_cases.cases:
    test_detect_rows(8, case[0], case[1])

print()
print(f'{MAGENTA}is_win cases{END}')

for case in is_win_cases.cases:
    test_is_win(8, case[0], case[1])
