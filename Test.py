Teams = ['Chelsea','Southampton']

win=0
loss=0
draw=0

for teamName in Teams:
    file = open("Arsenal.txt", "r", encoding="utf-8-sig")
    for line in file:
        if line.startswith('Beaten Teams ='):
            if line.count(teamName) == 2:
                win += 2
            elif line.count(teamName) == 1:
                win += 1
            else:
                win += 0

        if line.startswith('Lost to Teams ='):
            if line.count(teamName) == 2:
                loss += 2
            elif line.count(teamName) == 1:
                loss += 1
            else:
                loss += 0

        if line.startswith('Drew with Teams ='):
            if line.count(teamName) == 2:
                draw += 2
            elif line.count(teamName) == 1:
                draw += 1
            else:
                draw += 0

    if teamName == 'Chelsea':
        print("Should be Chelsea",teamName)

        print('Wins Against Chelsea: ' + str(win))
        print('Losses Against Chelsea: ' + str(loss))
        print('Draws Against Chelsea: ' + str(draw))

        win = 0
        loss = 0
        draw = 0

    if teamName == 'Southampton':
        print('\n')
        print("Should be Southampton",teamName)

        print('Arsenal Wins Against Southampton: ' + str(win))
        print('Arsenal Losses Against Southampton: ' + str(loss))
        print('Arsenal Draws Against Southampton: ' + str(draw))

        win = 0
        loss = 0
        draw = 0


