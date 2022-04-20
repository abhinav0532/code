playingArea = {'7': ' ' , '8': ' ' , '9': ' ' , '4': ' ' , '5': ' ' , '6': ' ' , '1': ' ' , '2': ' ' , '3': ' ' }

keys = []

for key in playingArea:
    keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(playingArea)
        print("Its the turn of," + turn + ".Which place do you want to move to?")

        move = input()        

        if playingArea[move] == ' ':
            playingArea[move] = turn
            count += 1
        else:
            print("Moving to this place is not possible\nWhich place do you want to move to?")
            continue
        
        if count >= 5:
            if playingArea['7'] == playingArea['8'] == playingArea['9'] != ' ':
                printBoard(playingArea)
                print("\nGame Over.\n")                
                print(" !!! " +turn + " won. !!!")                
                break

            elif playingArea['4'] == playingArea['5'] == playingArea['6'] != ' ':
                printBoard(playingArea)
                print("\nGame Over.\n")                
                print(" !!! " +turn + " won. !!!")
                break

            elif playingArea['1'] == playingArea['2'] == playingArea['3'] != ' ':
                printBoard(playingArea)
                print("\nGame Over.\n")                
                print(" !!! " +turn + " won. !!!")
                break
            elif playingArea['1'] == playingArea['4'] == playingArea['7'] != ' ':
                printBoard(playingArea)
                print("\nGame Over.\n")                
                print(" !!! " +turn + " won. !!!")
                break
            elif playingArea['2'] == playingArea['5'] == playingArea['8'] != ' ':
                printBoard(playingArea)
                print("\nGame Over.\n")                
                print(" !!! " +turn + " won. !!!")
                break
            elif playingArea['3'] == playingArea['6'] == playingArea['9'] != ' ':
                printBoard(playingArea)
                print("\nGame Over.\n")                
                print(" !!! " +turn + " won. !!!")
                break 
            elif playingArea['7'] == playingArea['5'] == playingArea['3'] != ' ':
                printBoard(playingArea)
                print("\nGame Over.\n")                
                print(" !!! " +turn + " won. !!!")
                break
            elif playingArea['1'] == playingArea['5'] == playingArea['9'] != ' ':
                printBoard(playingArea)
                print("\nGame Over.\n")                
                print(" !!! " +turn + " won. !!!")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in keys:
            playingArea[key] = " "

        game()

if __name__ == "__main__":
    game()