# f = open('highscore.txt', 'w')
# f.write('34')
# f.close()


def game():
    return 45


score = game()

with open('highscore.txt', 'r') as f:
    highscore = int(f.read())

if highscore < score:
    with open('highscore.txt', 'w') as f:
        f.write(str(score))


def game():
    return 78


score = game()

with open('highscore.rb', 'r') as f:
    highscore = f.read()

if highscore == '':
    with open('highscore.rb', 'w') as f:
        f.write(str(score))

elif int(highscore) == '':
    with open('highscore.rb', 'w') as f:
        f.write(str(score))
