board = [' '] * 9

player = 'X'

def display():

    print()

    print(board[0], "|", board[1], "|", board[2])
    print("--|---|--")
    print(board[3], "|", board[4], "|", board[5])
    print("--|---|--")
    print(board[6], "|", board[7], "|", board[8])

    print()

def check():

    win = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for i in win:

        a = i[0]
        b = i[1]
        c = i[2]

        if board[a] == board[b] == board[c] != ' ':
            return True

    return False

for i in range(9):

    display()

    pos = int(input("Enter position (0-8): "))

    if board[pos] == ' ':

        board[pos] = player

        if check():

            display()

            print(player, "Wins")

            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    else:
        print("Already Filled")

else:

    display()

    print("Draw")