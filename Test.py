Teams = ['Arsenal', 'Chelsea']

beatenTeam=[]
lostToTeams=[]
drewWith=[]
win = 0
loss = 0
draw=0

seasonResults = open('testfile.txt', 'r')


for teamName in Teams:

    for line in seasonResults:
        teamFiles = open("{}.txt".format(teamName), "w")
        home, away, result ,newline = line.split(',')
        if home == teamName:
            if result == 'H':
                beatenTeam.append(away)
                win += 1
            elif result == 'A':
                lostToTeams.append(away)
                loss += 1
            elif result == 'D':
                drewWith.append(away)
                draw += 1
        elif away == teamName:
            if result == 'A':
                beatenTeam.append(home)
                win += 1
            elif result == 'H':
                lostToTeams.append(home)
                loss += 1
            elif result == 'D':
                drewWith.append(home)
                draw += 1
        teamFiles.write("Win count =" + str(win) + "\n")
        teamFiles.write("Loss count =" + str(loss) + "\n")
        teamFiles.write("Draw Count =" + str(draw) + "\n")
        teamFiles.write("beaten Teams =" + str(beatenTeam) + "\n")
        teamFiles.write("Lost to Teams = " + str(lostToTeams) + "\n")
        teamFiles.write("drew with Teams = " + str(drewWith) + "\n")