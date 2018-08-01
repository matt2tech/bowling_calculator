def frame(scoreboard):
    while True:
        score = []
        ball_1 = input('"First Bowl"\nHow many pins were knocked down?\n>>> ')
        if ball_1.isdigit() and int(ball_1) <= 10:
            ball_1 = int(ball_1)
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
                            break
                        elif ball_2 == 10 - ball_1:
                            score.append('/')
                            break
                    else:
                        print('Not a valid number')
                break
            else:
                score.append(ball_1)
                score.append(0)
                break
        else:
            print('Not a valid number')
    scoreboard.append(score)
    print(scoreboard)


def total_score(scoreboard):
    total = 0
    for score in range(len(scoreboard)):
        if scoreboard[score][1] == '/':
            total += 10 + scoreboard[score + 1][0]
        # elif scoreboard[score][1] is scoreboard[-1][1] and scoreboard[-1][1] == '/':
        # while True:
        # roll = input(
        # '"Third Bowl":\nHow many pins were knocked down?\n>>> ')
        # if roll.isdigit():
        # total += 10 + int(roll)
        # break
        # else:
        # print('Not a valid number')
        # break
        else:
            total += sum(scoreboard[score])
    print(total)


def main():
    scoreboard = []
    # name = input('What is the player\'s name?\n>>> ')
    frame(scoreboard)
    frame(scoreboard)
    # frame(scoreboard)
    # frame(scoreboard)
    # frame(scoreboard)
    # frame(scoreboard)
    # frame(scoreboard)
    # frame(scoreboard)
    # frame(scoreboard)
    # frame(scoreboard)
    total_score(scoreboard)


if __name__ == '__main__':
    main()
