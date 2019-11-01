from game import Game

# first take input
print("Please enter two sizes line by line")
x = int(input())
y = int(input())

tot = x * y

print("Please enter bomb amount. Must be less than %d." % (tot))
num_bombs = int(input())

# generate the game
g = Game(x, y, num_bombs)

g.print_board()
g.print_bombs()

result = 0
while result == 0:
    print("Please enter coordinates line by line.")
    print("Marking/Unmarking? Answer y/n.")
    mark = input()

    print("Row then column")
    x = int(input())
    y = int(input())


    if mark == 'n':
        result = g.make_move(x, y)
    else:
        g.mark_bomb(x, y)


    if result == -1:
        print("BOMB DETONATED!")

    g.print_board()

    solved = False
    if g.check_win() == False:
        print("Haven't found all the bombs yet.")
    else:
        print("You win!")
        break

g.print_board()
