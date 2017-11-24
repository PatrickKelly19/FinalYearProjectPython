Teams = ['Arsenal', 'Bournemouth', 'Brighton', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Huddersfield', 'Leicester',
         'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Southampton', 'Stoke', 'Swansea',
         'Tottenham', 'Watford', 'West Brom', 'West Ham']

win = 0
loss = 0
draw = 0

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

    yearFiles = open('ResultsArsenal.txt', 'a')
    yearFiles.write('\n')
    yearFiles.write('Wins Against '+teamName+': ' + str(win)+'\n')
    yearFiles.write('Losses Against '+teamName+': ' + str(loss)+'\n')
    yearFiles.write('Draws Against '+teamName+': ' + str(draw)+'\n')

    total = win + loss + draw
    yearFiles.write("Total Number of Games Against Bournemouth: " + str(total)+'\n')

    if total == 0:
        winPer = 0
        lossPer = 0
        drawPer = 0
        yearFiles.write('Win Percentage Against '+teamName+': ' + str(winPer)+'%'+'\n')
        yearFiles.write('Loss Percentage Against '+teamName+': ' + str(lossPer)+'%'+'\n')
        yearFiles.write('Draw Percentage Against '+teamName+': ' + str(drawPer)+'%'+'\n')

    elif win == 0:
        winPer = format(0,'.2f')
        lossPer = format(loss / total * 100, '.2f')
        drawPer = format(draw / total * 100, '.2f')
        yearFiles.write('Win Percentage Against  '+teamName+': ' + winPer+'%'+'\n')
        yearFiles.write('Loss Percentage Against '+teamName+': ' + lossPer+'%'+'\n')
        yearFiles.write('Draw Percentage Against '+teamName+': ' + drawPer+'%'+'\n')

    elif loss == 0:
        lossPer = format(0,'.2f')
        winPer = format(win / total * 100, '.2f')
        drawPer = format(draw / total * 100, '.2f')
        yearFiles.write('Win Percentage Against '+teamName+': ' + winPer+'%'+'\n')
        yearFiles.write('Loss Percentage Against '+teamName+': ' + lossPer+'%'+'\n')
        yearFiles.write('Draw Percentage Against '+teamName+': ' + drawPer+'%'+'\n')

    elif draw == 0:
        drawPer = format(0,'.2f')
        winPer = format(win / total * 100, '.2f')
        lossPer = format(loss / total * 100, '.2f')
        yearFiles.write('Win Percentage Against '+teamName+': ' + winPer+'%'+'\n')
        yearFiles.write('Draw Percentage Against '+teamName+': ' + lossPer+'%'+'\n')
        yearFiles.write('Loss Percentage Against '+teamName+': ' + drawPer+'%'+'\n')

    else:
        winPer = format(win / total * 100, '.2f')
        lossPer = format(loss / total * 100, '.2f')
        drawPer = format(draw / total * 100, '.2f')
        yearFiles.write('Win Percentage Against '+teamName+': ' + winPer+'%'+'\n')
        yearFiles.write('Loss Percentage Against '+teamName+': ' + lossPer+'%'+'\n')
        yearFiles.write('Draw Percentage Against '+teamName+': ' + drawPer+'%'+'\n')
    win = 0
    loss = 0
    draw = 0