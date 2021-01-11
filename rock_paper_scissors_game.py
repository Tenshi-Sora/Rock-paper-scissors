import random
print('\n \n ----------Start---------- \n \n')


def validate(rps):
    '''
    Validates if the input is either rock, paper, or scissors and returns that value in the corect format. If it is not valid, it asks for a valid entry and re-runs the validation
    '''
    while True:
        if rps.casefold().strip() in ('rock', 'paper', 'scissors'):
            return rps.casefold().strip()
        else:
            print('You can\'t do that! Try again!')
            rps = input('Chose Rock, Paper, or Scissors: ')


play_again = True

while play_again:

    game_round = 0
    player1_victories = 0
    player2_victories = 0

    print('Lets play Rock, Paper, Scissors!')
    players = input(
        'How many players are playing? 1 or 2?: ').casefold().strip()
    while not players in ('1', '2'):
        print('That was an invalid entry, let\'s try again')
        players = input(
            'How many players are playing? 1 or 2?: ').casefold().strip()

    best_of = input(
        'Alright, and it will be best of how many rounds?: ').casefold().strip()
    while not str.isdecimal(best_of) or int(best_of) <= 0:
        print('That was an invalid entry, let\'s try again')
        best_of = input(
            'Alright, and it will be best of how many rounds?: ').casefold().strip()
    best_of = int(best_of)

    while game_round <= best_of:

        # Player 1's choice
        player1 = input('Player 1, chose Rock, Paper, or Scissors: ')
        player1 = validate(player1)

        if players == '1':  # Bot choice
            player2 = random.choice(['rock', 'paper', 'scissors'])
            player2 = validate(player2)

        if players == '2':  # Player 2's choice
            print('OK! Now for Player 2!')
            player2 = input('Player 2, chose Rock, Paper, or Scissors: ')
            player2 = validate(player2)

        print('Now lets go!')
        print('ROCK, PAPER, SCISSORS!!!')

        if ('rock', 'paper', 'scissor').index(player1) == ('scissor', 'rock', 'paper').index(player2):
            print('Player 1 wins!')
            player1_victories = player1_victories + 1
            game_round = game_round + 1
        if ('rock', 'paper', 'scissor').index(player1) == ('rock', 'paper', 'scissor').index(player2):
            print('It\'s a tie!')
        if ('rock', 'paper', 'scissor').index(player1) == ('paper', 'scissor', 'rock').index(player2):
            print('Player 2 wins!')
            player2_victories = player2_victories + 1
            game_round = game_round + 1

        if best_of > 1:  # Checks best_of winner
            if player1_victories == best_of:
                print(f'Player 1 won {best_of} rounds! Congradulations :D!')
                print('Would you like to play again?')
            if player2_victories == best_of:
                print(f'Player 2 won {best_of} rounds! Congradulations :D!')
                print('Would you like to play again?')
            if player1_victories == best_of or player2_victories == best_of:
                best_of = 0
            else:
                print(
                    f'The score is Player 1: {player1_victories} to Player 2: {player2_victories}\n')

        # Play again loop
        while best_of == 0:
            play_again = input('Play again?: ').casefold().strip()
            if play_again == 'yes':
                play_again = True
                break
            elif play_again == 'no':
                print('See you next time then!')
                play_again = False
                break
            print("I didn't get that, Would you like to play again? (Yes or No)")

print('Thanks for playing! Cya next time!')

print('\n \n ----------End---------- \n \n')
