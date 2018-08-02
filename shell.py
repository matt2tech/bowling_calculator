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
    print(scoreboard)
    total = 0
    for score in range(len(scoreboard)):
        if '/' in scoreboard[score]:
            ball_1 = scoreboard[score][-2]
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


def main():
    scoreboard = []
    name = input('What is the player\'s name?\n>>> ')
    scoreboard = frame()
    tenth_frame(scoreboard)
    total_score(scoreboard, name)


if __name__ == '__main__':
    main()
