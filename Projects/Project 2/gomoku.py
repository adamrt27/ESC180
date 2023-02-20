"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 28, 2022
"""

def is_empty(board):
    for e in board:
        for i in e:
            if i != " ":
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    x = x_end - (d_x*(length-1))
    y = y_end - (d_y*(length-1))
    # print(len(board))
    # d_y = abs(d_y)
    # # d_x = abs(d_x)
    # if y-d_y < 0:
    #     d_y = -d_y
    # if x-d_x < 0:
    #     d_x = -d_x
    # if y_end+d_y >= len(board):
    #     d_y = 0
    # if x_end+d_x >= len(board):
    #     d_x = 0
    # print('y:',y,'x:',x,"y_end:",y_end,'x_end:',x_end)
    # print(d_y,d_x)
    if y-d_y >=0 and y-d_y <=(len(board)-1) and x-d_x >=0 and x-d_x <=(len(board)-1) and y_end+d_y <= (len(board)-1) and y_end+d_y >=0  and x_end+d_x <= (len(board)-1) and x_end+d_x >=0  and board[(y-d_y)][(x-d_x)] == " " and board[(y_end + d_y)][(x_end + d_x)] == " ":
        # print("open")
        return "OPEN"

    # FIX THIS LINE
    elif (((y == 0 or y == (len(board)-1)) and d_y != 0)  or ((x == 0 or x == (len(board)-1)) and d_x != 0) or board[(y-d_y)][(x-d_x)] != " ") is not (((y_end == 0 or y_end == (len(board)-1)) and d_y != 0) or ((x_end == 0 or x_end == (len(board)-1)) and d_x != 0) or board[(y_end + d_y)][(x_end + d_x)] != " "):
        # print("closed")
        return "SEMIOPEN"
    else:
        # print("semiopen")
        return "CLOSED"
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    # Go through each potential sequence in board (if sequence is 123 and length is 2 there is 12, 23) and run
    # is_bounded

    # figure out how to make it detect whether there is sequence cuz that is where issue is.
    if col == 'b':
        othercol = 'w'
    else:
        othercol = 'b'
    open_seq_count = 0
    semi_open_seq_count = 0
    seq_list = []
    # max_y = len(board)
    # max_x = len(board[0])
    # if d_y != 0:
    #     len_row_y = (max_y-y_start)/d_y - length
    # else:
    #     len_row_y = len(board)+1
    # if d_x != 0:
    #     len_row_x = (max_x-x_start)/d_x - length
    # else:
    #     len_row_x = len(board)+1
    # print("#rows: ", len_row_x,"#cols:",len_row_y)
    # len_row = min(abs(len_row_x),abs(len_row_y))
    # num_seq = int(len_row + 1)
    # print("num_seq:",num_seq)
    for i in range(len(board)):
        if y_start+(d_y*i)+((length-1)*d_y) < 0 or y_start+(d_y*i)+((length-1)*d_y) >= len(board) or x_start+(d_x*i)+((length-1)*d_x) < 0 or x_start+(d_x*i)+((length-1)*d_x) >= len(board):
            # print([[y_start+(d_y*i),x_start + (d_x*i)],[y_start+(d_y*i)+((length-1)*d_y),x_start + (d_x*i)+((length-1)*d_x)]])
            break
        seq_list.append([[y_start+(d_y*i),x_start + (d_x*i)],[y_start+(d_y*i)+((length-1)*d_y),x_start + (d_x*i)+((length-1)*d_x)]])
    for seq in seq_list:
        # print(seq)
        count = 0
        for k in range(length):
            if board[seq[0][0] + (d_y*k)][seq[0][1]+(d_x*k)] == col:
                count += 1
        # print(count)
        if count == length:
            # print(seq)
            y_start = seq[0][0]
            if y_start - d_y < 0 or y_start - d_y == len(board):
                y_start_1 = y_start
            else:
                y_start_1 = y_start - d_y
            x_start = seq[0][1]
            if x_start - d_x < 0 or x_start - d_x == len(board):
                x_start_1 = x_start
            else:
                x_start_1 = x_start - d_x
            y_end = seq[1][0]
            if y_end + d_y == len(board) or y_end + d_y < 0:
                y_end_1 = y_end
            else:
                y_end_1 = y_end + d_y
            x_end = seq[1][1]
            if x_end + d_x == len(board) or x_end + d_x < 0:
                x_end_1 = x_end
            else:
                x_end_1 = x_end + d_x            
            
            if is_bounded(board,y_end,x_end,length,d_y,d_x) == "OPEN":
                # print(seq)
                open_seq_count += 1
            elif is_bounded(board,y_end,x_end,length,d_y,d_x) == "SEMIOPEN":
                # print(seq)
                # print(y_end)
                # print(y_end_1)
                # print(othercol)
                # if seq[0][1] not in [0,7] and seq[0][0] not in [0,7] and seq[1][1] not in [0,7] and seq[1][0] not in [0,7]:
                if ((x_start != x_start_1 and x_end != x_end_1) or d_x == 0) and ((y_end != y_end_1 and y_start != y_start_1) or d_y == 0):
                    # print("hi")
                    if (board[y_start_1][x_start_1] == othercol or board[y_start_1][x_start_1] ==  " ") and (board[y_end_1][x_end_1] == othercol or board[y_end_1][x_end_1] == " "):
                        semi_open_seq_count += 1
                else:
                    # print("hello")
                    if (board[y_start_1][x_start_1] == othercol or board[y_start_1][x_start_1] ==  " ") or (board[y_end_1][x_end_1] == othercol or board[y_end_1][x_end_1] == " "):
                        semi_open_seq_count += 1

            # if d_y != -1 and d_x != -1:
            #     # print('hi')
            #     if seq[0][0] != 0 and seq[0][1] != 0 and board[seq[0][0] - d_y][seq[0][1]-d_x] != col:
            #         if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "OPEN" and board[seq[1][0]][seq[1][1]] == col:
            #             open_seq_count += 1
            #             print(seq)
            #         if ((seq[1][0] == (len(board)-1) and d_y != 0) or (seq[1][1] == (len(board)-1)) and d_x != 0) or ((board[seq[1][0] + d_y][seq[1][1]+d_x] != col) and (board[seq[0][0]-d_y][seq[0][1]-d_x] != col)):
            #             if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "SEMIOPEN" and board[seq[1][0]][seq[1][1]] == col:
            #                 semi_open_seq_count += 1
            #                 print(seq)
            #     elif seq[0][0] == 0 and seq[0][1] != 0:
            #         if (seq[1][0] == (len(board)-1) or seq[1][1] == (len(board)-1)) or ((board[seq[1][0] + d_y][seq[1][1]+d_x] != col) and (board[seq[0][0]][seq[0][1]-d_x] != col)):
            #             if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "SEMIOPEN" and board[seq[1][0]][seq[1][1]] == col:
            #                 semi_open_seq_count += 1
            #                 print(seq)
            #     elif seq[0][1] == 0 and seq[0][0] != 0:
            #         if (seq[1][0] == (len(board)-1) or seq[1][1] == (len(board)-1)) or ((board[seq[1][0] + d_y][seq[1][1]+d_x] != col) and (board[seq[0][0]-d_y][seq[0][1]] != col)):
            #             if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "SEMIOPEN" and board[seq[1][0]][seq[1][1]] == col:
            #                 semi_open_seq_count += 1
            #                 print(seq)
            #     else:
            #         if (seq[1][0] == (len(board)-1) or seq[1][1] == (len(board)-1)) or ((board[seq[1][0] + d_y][seq[1][1]+d_x] != col)):
            #             if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "SEMIOPEN" and board[seq[1][0]][seq[1][1]] == col:
            #                 semi_open_seq_count += 1
            #                 print(seq)

            # elif d_x == -1:               
            #     # print('hey')
            #     if seq[0][0] != 0 and seq[0][1] != 7 and board[seq[0][0]-d_y][seq[0][1]-d_x] != col:
            #         if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "OPEN" and board[seq[1][0]][seq[1][1]] == col:
            #             open_seq_count += 1
            #         if (seq[1][0] == (len(board)-1) or seq[1][0] == 0 or seq[1][1] == (len(board)-1)) or seq[1][1] == 0 or  (board[seq[1][0] + d_y][seq[1][1]+d_x] != col):
            #             if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "SEMIOPEN" and board[seq[1][0]][seq[1][1]] == col:
            #                 semi_open_seq_count += 1
            #     elif seq[0][0] == 0 or seq[0][1] == 7:
            #         if (seq[1][0] == (len(board)-1) or seq[1][0] == 0 or seq[1][1] == (len(board)-1)) or seq[1][1] == 0 or  (board[seq[1][0] + d_y][seq[1][1]+d_x] != col):
            #             if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "SEMIOPEN" and board[seq[1][0]][seq[1][1]] == col:
            #                 semi_open_seq_count += 1
            # else:
            #     # print('ho')
            #     if seq[0][0] != 7 and seq[0][1] != 0 and board[seq[0][0]-d_y][seq[0][1]-d_x] != col:
            #         if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "OPEN" and board[seq[1][0]][seq[1][1]] == col:
            #             open_seq_count += 1
            #         if (seq[1][0] == (len(board)-1) or seq[1][0] == 0 or seq[1][1] == (len(board)-1)) or seq[1][1] == 0 or (board[seq[1][0] + d_y][seq[1][1]+d_x] != col):
            #             if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "SEMIOPEN" and board[seq[1][0]][seq[1][1]] == col:
            #                 semi_open_seq_count += 1
            #     elif seq[0][0] == 7 or seq[0][1] == 0:
            #         if (seq[1][0] == (len(board)-1) or seq[1][0] == 0 or seq[1][1] == (len(board)-1)) or seq[1][1] == 0 or (board[seq[1][0] + d_y][seq[1][1]+d_x] != col):
            #             if is_bounded(board, seq[1][0], seq[1][1], length, d_y, d_x) == "SEMIOPEN" and board[seq[1][0]][seq[1][1]] == col:
            #                 semi_open_seq_count += 1
    return (open_seq_count, semi_open_seq_count)
    

def detect_rows(board, col, length):
    ####CHANGE ME
    x = 0
    y = 0

    list = [0,0]

    # print("VERTICAL")
    #horizontal rows
    for i in range(len(board)):
        x = i
        temp = detect_row(board, col, y,x,length,1,0)
        list[0] += temp[0]
        list[1] += temp[1]
        # if(temp[0] >= 1):
        #     print(temp[0],y,x)
        # if temp[1] >= 1:
        #     print(temp[1],y,x)
    x = 0

    # print("HORIZONRAL")
    #vertical rows
    for i in range(len(board)):
        y = i
        # print(y,x)
        temp = detect_row(board, col, y,x,length,0,1)
        list[0] += temp[0]
        list[1] += temp[1]
        # if(temp[0] >= 1):
        #     print(temp[0],y,x)
        # if temp[1] >= 1:
        #     print(temp[1],y,x)
    y = 0
    
    # print("DIAGONAL RIGHT")
    #diagonal towards right
    start_y = len(board) - length
    end_x = start_y
    #along the y first
    for i in range(start_y,-1,-1):
        y = i
        # print(y)
        temp = detect_row(board, col, y,x,length,1,1)
        list[0] += temp[0]
        list[1] += temp[1]
        # if(temp[0] >= 1):
        #     print(temp[0],y,x)
        # if temp[1] >= 1:
        #     print(temp[1],y,x)
    
    #along x
    for i in range(1,end_x):
        x = i
        temp = detect_row(board, col, y,x,length,1,1)
        list[0] += temp[0]
        list[1] += temp[1]
        # if(temp[0] >= 1):
        #     print(temp[0],y,x)
        # if temp[1] >= 1:
        #     print(temp[1],y,x)

    x = 0
    # print("DIAGONAL LEFT")
    #diagonal towards left. starts at
    for i in range(length-1,len(board)):
        y = i
        # print(y,x)
        temp = detect_row(board, col, y,x,length,-1,1)
        list[0] += temp[0]
        list[1] += temp[1]
        # if(temp[0] >= 1):
        #     print(temp[0],y,x)
        # if temp[1] >= 1:
        #     print(temp[1],y,x)
    x = 7
    for i in range(1,len(board)-length):
        y= i
        # print(y,x)
        # print_board(board)
        temp = detect_row(board, col, y,x,length,1,-1)
        list[0] += temp[0]
        list[1] += temp[1]
        # if(temp[0] >= 1):
        #     print(temp[0],y,x)
        # if temp[1] >= 1:
        #     print(temp[1],y,x)

    return (list[0],list[1])
    
def search_max(board):
    score_max = -10000
    for i in range(len(board)):
        for k in range(len(board)):
            # print(i,k)
            temp_board = []
            for x in range(len(board)):
                temp = []
                for elem in board[x]:
                    temp.append(elem)
                temp_board.append(temp)
            if temp_board[i][k] == ' ':
                temp_board[i][k] = "b"
                # print_board(temp_board)
                temp_score = score(temp_board)
                # print("Score at ", i, k, ": ",temp_score)
                if temp_score > score_max:
                    score_max = temp_score
                    move_y = i
                    move_x = k

    print("result",move_y,move_x)
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    # print('score:',score(board))

    coll = ['w','b']
    win = ["White won", "Black won"]

    for i in range(2):
        col = coll[i]
        if col == 'w':
            othercol = 'b'
        else:
            othercol = 'w'
        winprint = win[i]
        x = 0
        y = 0

        length = 5

        # print("DIAGONAL RIGHT")
        #diagonal towards right
        start_y = len(board) - length
        end_x = start_y
        #along the y first
        for i in range(start_y,-1,-1):
            y = i
            # print(y)
            count = 0
            for i in range(length):
                if board[y+i][x+i] == col:
                    count += 1
            if count == length and ((y+5) == len(board) or (x+5) == len(board) or board[y+5][x+5] == othercol):
                return winprint
        
        #along x
        for i in range(1,end_x):
            x = i
            count = 0
            for i in range(length):
                
                if board[y+i][x+i] == col:
                    count += 1
            if count == length and ((y+5) == len(board) or (x+5) == len(board) or board[y+5][x+5] == othercol):
                return winprint

        x = 0
        # print("DIAGONAL LEFT")
        #diagonal towards left. starts at
        for i in range(length-1,len(board)):
            y = i
            count = 0
            for i in range(length):
                if board[y+(-i)][x+i] == col:
                    count += 1
            if count == length and ((y-5) <= 0 or (x+5) >= len(board) or board[y-5][x+5] == othercol):
                return winprint

        x = 7
        for i in range(1,len(board)-length):
            y= i
            # print(y,x)
            # print_board(board)
            count = 0
            for i in range(length):
                if board[y+i][x+(-i)] == col:
                    count += 1
            if count == length and ((y+5) >= len(board) or (x-5) <= 0 or board[y+5][x-5] == othercol):
                return winprint

    if score(board) == 100000:
        return "Black won"
    elif score(board) == -100000:
        return "White won"
    elif any(' ' in sublist for sublist in board):
        return "Continue playing"
    else:
        return "Draw"


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    board = make_empty_board(8)
    # # # # print(is_empty(board))
    put_seq_on_board(board,0,4,1,-1,5,"w")
    print_board(board)
    print(is_win(board))
    # # board[0][0] = 'w'
    # # board[1][0] = 'w'
    # # board[1][1] = 'w'
    # # board[0][1] = 'w'
    # # board[2][2] = 'b'
    # # board[1][4] = 'w'
    # board = [['w', ' ', 'b', 'b', 'b', ' ', ' ', ' '], ['w', ' ', 'b', 'w', ' ', 'b', 'w', ' '], [' ', 'b', 'w', 'b', 'w', 'b', ' ', 'w'], ['b', 'b', ' ', 'w', 'b', 'w', 'w', ' '], ['b', 'b', 'w', ' ', 'w', ' ', ' ', 'b'], ['b', 'b', 'b', 'w', ' ', 'b', 'b', ' '], ['w', 'b', ' ', ' ', 'b', 'w', ' ', 'w'], ['b', 'w', ' ', 'w', 'w', ' ', 'w', ' ']]
    # print_board(board)
    # print(detect_rows(board,'b',2))
    # # print(detect_rows(board,'b',2))
    # print_board(board)


    
    # board[2][4] = 'b'

    # print_board(board)
    # put_seq_on_board(board,0,1,1,0,8,"w")
    # put_seq_on_board(board,0,2,1,0,8,"w")
    # put_seq_on_board(board,0,3,1,0,8,"w")
    # put_seq_on_board(board,0,4,1,0,8,"w")
    # put_seq_on_board(board,0,5,1,0,8,"w")

    # # print(is_empty(board))
    # # print_board(board)
    # # print(is_bounded(board,3,3,3,1,1))
    # put_seq_on_board(board,0,6,1,0,8,"b")    
    # put_seq_on_board(board,0,7,1,0,8,"b")

    # put_seq_on_board(board,3,3,1,0,3,"w")
    # print(is_empty(board))
    # board[4][5] = 'b'
    # print_board(board)
    # print(score(board))
    # print(detect_row(board,'b',0,6,4,1,0))
    # print(is_bounded(board,2,3,3,1,1))
    # print("ROW",detect_row(board,"b",2,7,3,1,-1))
    # print(detect_rows(board,"w",5))
    # test_detect_rows()
    # print(search_max(board))
    # print_board(board)
    
    # print(score(board))
    # temp_board = board
    # temp_board[0][4] = 'b'
    # print(score(temp_board))
    # print(test_search_max())
    # print(test_detect_row())
    # print(is_win(board))
    # play_gomoku(8)
