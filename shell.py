def frame():
    scoreboard = []
    frame = 1
    while len(scoreboard) != 9:
        score = []
        ball_1 = input(
            'Frame: {}\n"First Bowl"\nHow many pins were knocked down?\n>>> '.
            format(frame))
        if ball_1.isdigit() and int(ball_1) <= 10:
            ball_1 = int(ball_1)
            frame += 1
            if ball_1 < 10:
                score.append(ball_1)
                while True:
                    ball_2 = input(
                        '"Second Bowl"\nHow many pins were knocked down?\n>>> '
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


def total_score(scoreboard):
    print(scoreboard)
    total = 0
    for score in range(len(scoreboard)):
        if '/' in scoreboard[score]:
            ball_1 = scoreboard[score][0]
            ball_2 = 10 - ball_1
            total += ball_1 + ball_2
            if score + 1 < len(scoreboard):
                next_ball = scoreboard[score + 1][0]
                if next_ball == 'X':
                    total += 10
                else:
                    total += next_ball
        elif scoreboard[score][0] == 'X':
            if scoreboard[score + 1][0] == 'X' and scoreboard[score +
                                                              2][0] == 'X':
                total += 30
            elif scoreboard[score + 1][-1] == '/':
                total += 20
            elif scoreboard[score + 1][0] == 'X':
                total += 20 + scoreboard[score + 2][0]
            else:
                total += 10 + scoreboard[score + 1][0] + scoreboard[score +
                                                                    1][-1]
        else:
            total += sum(scoreboard[score])
    print(total)


def main():
    # name = input('What is the player\'s name?\n>>> ')
    scoreboard = frame()
    total_score(scoreboard)


if __name__ == '__main__':
    main()

    # if scoreboard[score][-1] == '/':
    #     if scoreboard[score + 1][0] == 'X':
    #         total += 20
    #     else:
    #         total += 10 + scoreboard[score + 1][0]
