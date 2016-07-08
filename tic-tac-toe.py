import sys

def construct_array(dict):
    print dict[1] + ' | ' + dict[2] + ' | ' + dict[3]
    print dict[4] + ' | ' + dict[5] + ' | ' + dict[6]
    print dict[7] + ' | ' + dict[8] + ' | ' + dict[9]
 
def choose_number(player, options):
    option = input('%s! choose numbers which you want to mark?' % player)
    if option not in options:
        print('Try Again!')
        print('please choose from %s' % options)
        # dont forget to put return - else give weird results
        return choose_number(player, options)
    else:
        options.remove(option)
    return option
    
def decide_game(dict, player, symbol):
    if dict[1] == symbol and dict[2] == symbol  and dict[3] == symbol:
        print('Hurray! %s is a winner.' % player)
        sys.exit()
    elif dict[4] == symbol and dict[5] == symbol and dict[6] == symbol:
        print('Hurray! %s is a winner.' % player)
        sys.exit()
    elif dict[7] == symbol and dict[8] == symbol and dict[9] == symbol:
        print('Hurray! %s is a winner.' % player)
        sys.exit()
    elif dict[1] == symbol and dict[5] == symbol and dict[9] == symbol:
        print('Hurray! %s is a winner.' % player)
        sys.exit()
    elif dict[1] == symbol and dict[4] == symbol and dict[7] == symbol:
        print('Hurray! %s is a winner.' % player)
        sys.exit()
    elif dict[2] == symbol and dict[5] == symbol and dict[8] == symbol:
        print('Hurray! %s is a winner.' % player)
        sys.exit()
    elif dict[3] == symbol and dict[6] == symbol and dict[9] == symbol:
        print('Hurray! %s is a winner.' % player)
        sys.exit()
    else:
        return
 
if __name__ == '__main__':
    dict = {1:'1', 2:'2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    
    # initial tic-tac-toe representation
    construct_array(dict)
    
    player1 = raw_input('name of player1?')
    print('welcome %s!' % player1)
    
    player2 = raw_input('name of player2?')
    print('welcome %s!' % player2)
    
    print('Following symbols belong to players:')
    print('%s - X' % player1)
    print('%s - Y' % player2)
    
    options = [1,2,3,4,5,6,7,8,9]
    for key in dict.keys():
        # odd for player1, even for player2
        construct_array(dict)
        if key%2 == 0:
            option = choose_number(player2, options)
            dict[option] = 'Y'
            decide_game(dict, player2, 'Y')
        else:
            option = choose_number(player1, options)
            dict[option] = 'X'
            decide_game(dict, player1, 'X')
         
    print('This is a tie.')   
    print('Game End!')
