def frame():
    scoreboard = []
    frame = 1
    while len(scoreboard) != 9:
        score = []
        ball_1 = input(
            '\nFrame: {}\n"First Bowl"\nHow many pins were knocked down?\n>>> '.
            format(frame))
        if ball_1.isdigit() and int(ball_1) <= 10:
            ball_1 = int(ball_1)
            frame += 1
            if ball_1 < 10:
                score.append(ball_1)
                while True:
                    ball_2 = input(
                        '"\nSecond Bowl"\nHow many pins were knocked down?\n>>> '
                    )
                    if ball_2.isdigit() and int(ball_2) <= 10 - ball_1:
                        ball_2 = int(ball_2)
                        if ball_2 < 10 - ball_1:
                            score.append(ball_2)
                            scoreboard.append(score)
                            break
                        elif ball_2 == 10 - ball_1:
                            score.append('/')
                            scoreboard.append(score)
                            break
                    else:
                        print('Not a valid number')
            else:
                score.append('X')
                scoreboard.append(score)
        else:
            print('Not a valid number')
    return scoreboard


def total_score(scoreboard, name):
    scoretable(scoreboard)
    total = 0
    for score in range(len(scoreboard)):
        if '/' in scoreboard[score]:
            for frame in scoreboard:
                for i in frame:
                    if i != '/' and i != 'X':
                        ball_1 = i
            ball_2 = 10 - ball_1
            total += ball_1 + ball_2
            if score + 1 < len(scoreboard):
                next_ball = scoreboard[score + 1][0]
                if next_ball == 'X':
                    total += 10
                else:
                    total += next_ball
            else:
                next_ball = scoreboard[score][2]
                if next_ball == 'X':
                    total += 10
                elif next_ball == '/':
                    total += 10
                else:
                    total += next_ball
        elif 'X' in scoreboard[score]:
            total += 10
            if score + 1 < len(scoreboard):
                next_ball = scoreboard[score + 1][0]
                if next_ball == 'X':
                    total += 10
                    if score + 2 < len(scoreboard):
                        third_ball = scoreboard[score + 2][0]
                        if third_ball == 'X':
                            total += 10
                        else:
                            total += third_ball
                    else:
                        third_ball = scoreboard[score + 1][1]
                        if third_ball == 'X':
                            total += 10
                        else:
                            total += third_ball
                else:
                    third_ball = scoreboard[score + 1][1]
                    if third_ball == '/':
                        total += 10
                    else:
                        total += next_ball + third_ball
            else:
                next_ball = scoreboard[score][1]
                third_ball = scoreboard[score][2]
                if next_ball == 'X' and third_ball == 'X':
                    total += 20
                elif next_ball == 'X':
                    total += 10 + third_ball
                else:
                    if third_ball == '/':
                        total += 10
                    else:
                        total += next_ball + third_ball
        else:
            total += sum(scoreboard[score])
    print('{}\'s score: {}'.format(name, total))


def tenth_frame(scoreboard):
    score = []
    while len(score) <= 0:
        ball_1 = input(
            '\nFrame: 10\n"First Bowl"\nHow many pins were knocked down?\n>>> '
        )
        if ball_1.isdigit():
            ball_1 = int(ball_1)
            if ball_1 < 10:
                while True:
                    ball_2 = input(
                        '\n"Second Bowl"\nHow many pins were knocked down?\n>>> '
                    )
                    if ball_2.isdigit() and int(ball_2) <= 10 - ball_1:
                        ball_2 = int(ball_2)
                        if ball_1 + ball_2 == 10:
                            ball_2 = '/'
                            while True:
                                ball_3 = input(
                                    '\n"Third Bowl"\nHow many pins were knocked down?\n>>> '
                                )
                                if ball_3.isdigit():
                                    score = [ball_1, ball_2, int(ball_3)]
                                    for i in range(len(score)):
                                        if score[i] == 10:
                                            score[i] = 'X'
                                    scoreboard.append(score)
                                    break
                                else:
                                    print('Not a valid number')
                            break
                        else:
                            score = [ball_1, ball_2]
                            scoreboard.append(score)
                            break
                    else:
                        print('Not a valid number')
            elif ball_1 == 10:
                while True:
                    ball_2 = input(
                        '\n"Second Bowl"\nHow many pins were knocked down?\n>>> '
                    )
                    if ball_2.isdigit():
                        ball_2 = int(ball_2)
                        if ball_2 == 10:
                            while True:
                                ball_3 = input(
                                    '\n"Third Bowl"\nHow many pins were knocked down?\n>>> '
                                )
                                if ball_3.isdigit():
                                    score = ['X', 'X', int(ball_3)]
                                    for i in range(len(score)):
                                        if score[i] == 10:
                                            score[i] = 'X'
                                    scoreboard.append(score)
                                    break
                                else:
                                    print('Not a valid number')
                            break
                        else:
                            while True:
                                ball_3 = input(
                                    '\n"Third Bowl"\nHow many pins were knocked down?\n>>> '
                                )
                                if ball_3.isdigit(
                                ) and int(ball_3) <= 10 - ball_2:
                                    if int(ball_3) + ball_2 == 10:
                                        score = ['X', ball_2, '/']
                                        scoreboard.append(score)
                                        break
                                    else:
                                        score = ['X', ball_2, int(ball_3)]
                                        scoreboard.append(score)
                                        break
                                else:
                                    print('Not a valid number')
                            break
                    else:
                        print('Not a valid number')
        else:
            print('Not a valid number')


def play_again():
    game = ''
    while game != '2':
        game = input('\nNew Game?\n1 - Yes\n2 - No\n>>> ')
        if game == '1':
            main()
        elif game == '2':
            exit()
        else:
            print('Invalid Choice')


def scoretable(scoretable):
    for score in range(len(scoretable) - 1):
        if len(scoretable[score]) == 2:
            print('Frame {}: {}|{}'.format(score + 1, scoretable[score][0],
                                           scoretable[score][1]))
        else:
            print('Frame {}:  |{}'.format(score + 1, scoretable[score][0]))
    if len(scoretable[9]) == 3:
        print('Frame 10: {}|{}|{}'.format(scoretable[9][0], scoretable[9][1],
                                          scoretable[9][2]))
    else:
        print('Frame 10: {}|{}| '.format(scoretable[9][0], scoretable[9][1]))


def main():
    scoreboard = []
    name = input('\nWhat is the player\'s name?\n>>> ')
    scoreboard = frame()
    tenth_frame(scoreboard)
    print('\n')
    total_score(scoreboard, name)
    play_again()


if __name__ == '__main__':
    main()
