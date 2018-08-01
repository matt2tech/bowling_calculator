def frames():
    frame = 0
    scoreboard = []
    while len(scoreboard) != 9:
        while True:
            frame += 1
            score = []
            ball_1 = input(
                'Frame: {}\n"First Roll"\nHow many pins were knocked down?\n>>> '.
                format(frame))
            if ball_1.isdigit() and not int(ball_1) > 10:
                if int(ball_1) < 10:
                    while True:
                        ball_2 = input(
                            '"Second Roll"\nHow many pins were knocked down?\n>>> '
                        )
                        if ball_2.isdigit() and int(ball_2) < 10 - int(ball_1):
                            score.append(int(ball_1))
                            score.append(int(ball_2))
                            scoreboard.append(score)
                            break
                        elif ball_2.isdigit() and int(
                                ball_2) == 10 - int(ball_1):
                            score.append(int(ball_1))
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
            break
    tenth_frame(scoreboard)
    print(scoreboard)
    return scoreboard


def tenth_frame(scoreboard):
    while True:
        score = []
        ball_1 = input('"First Roll"\nHow many pins were knocked down?\n>>> ')
        if ball_1.isdigit() and not int(ball_1) > 10:
            if int(ball_1) <= 10:
                while True:
                    ball_2 = input(
                        'Frame: 10\n"Second Roll"\nHow many pins were knocked down?\n>>> '
                    )
                    if ball_2.isdigit() and int(ball_2) < 10 - int(ball_1):
                        score.append(int(ball_1))
                        score.append(int(ball_2))
                        scoreboard.append(score)
                        break
                    elif ball_2.isdigit() and int(ball_2) == 10 - int(ball_1):
                        score.append(int(ball_1))
                        score.append('/')
                        ball_3 = input(
                            '"Third Roll"\nHow many pins were knocked down\n>>> '
                        )
                        break
                    else:
                        print('Not a valid number')
                break


# def tenth_frame(scoreboard):
# bowls = 2
# while bowls != 0:
# score = []
# ball_1 = input('Frame: 10\n"First Roll"\nHow many pins were knocked down?\n>>> ')
# if ball_1.isdigit() and not int(ball_1) > 10:
# if int(ball_1) == 10:

# def total_score(scoreboard):
# total = 0
# for score in scoreboard:
# total += sum(score)
# print(total)


def total_score(scoreboard):
    total = 0
    for frame in range(len(scoreboard)):
        if frame is not 9:
            total += sum(scoreboard[frame])
    print(total)


def main():
    # name = input('What is the player\'s name?\n>>> ')
    score = frames()
    total_score(score)


if __name__ == '__main__':
    main()
