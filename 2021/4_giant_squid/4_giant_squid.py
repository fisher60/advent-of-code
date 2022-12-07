# with open("4_giant_squid.txt", "r") as f:
#     raw_inps = f.read().split("\n\n")
#     numbers_called = raw_inps[0].split(",")
#     raw_boards = raw_inps[1:]

test_inps = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

raw_inps = test_inps.split("\n\n")

numbers_called = raw_inps[0].split(",")
raw_boards = raw_inps[1:]


def clean_board(board: str) -> list:
    out_board = []
    for each in board.split("\n"):
        this_row = []
        for num_str in each.split(" "):
            cleaned_num_str = num_str.strip(" ")
            if len(cleaned_num_str) > 0:
                this_row.append(cleaned_num_str)
        out_board.append(this_row)
    return out_board


def check_board(board: list, nums: list) -> tuple:
    for num in nums:
        row_sum = 0
        col_sum = 0
        for col_num, row in enumerate(board):
            row_sum += num in row
            col_sum += any(num in col for col in [x[col_num] for x in board])
            print("###########")
            print(board)
            print(f"Row: {row_sum}:: Col: {col_sum}")
            print("##############")
            if row_sum == 5 or col_sum == 5:
                return True, num
    return False, 0


if __name__ == '__main__':
    boards = list(map(clean_board, raw_boards))
    board_found = False
    winning_board = None
    winning_num_ind = 0
    winning_num = 0

    for ind in range(len(numbers_called)):
        if board_found:
            break

        for this_board in boards:
            checked_board = check_board(this_board, numbers_called[:ind + 1])
            if checked_board[0]:
                winning_board = this_board
                winning_num_ind = ind
                winning_num = checked_board[1]
                board_found = True
                break

    if winning_board is not None:
        board_sum = 0
        for temp_row in winning_board:
            for temp_num in temp_row:
                if temp_num not in numbers_called[:winning_num_ind + 1]:
                    board_sum += int(temp_num)
        print("winning board found")
