Teams = ['Arsenal', 'Aston Villa', 'Barnsley', 'Birmingham', 'Blackburn', 'Blackpool', 'Bolton', 'Bournemouth',
             'Bradford', 'Brighton', 'Burnley', 'Cardiff', 'Charlton', 'Chelsea', 'Coventry', 'Crystal Palace', 'Derby',
             'Everton', 'Fulham', 'Huddersfield', 'Hull', 'Ipswich', 'Leeds', 'Leicester', 'Liverpool', 'Man City',
             'Man United', 'Middlesbrough', 'Newcastle', 'Norwich', 'Oldham', 'Portsmouth', 'QPR', 'Reading',
             'Sheffield United', 'Sheffield Weds', 'Southampton', 'Stoke', 'Sunderland', 'Swansea', 'Swindon', 'Tottenham',
             'Watford', 'West Brom', 'West Ham', 'Wigan', 'Wimbledon', 'Wolves']

beatenTeam = []
lostToTeams = []
drewWith = []
win = 0
loss = 0
draw = 0

seasonResults = open('testfile.txt', 'r')

for teamName in Teams:
    teamFiles = open("{}.txt".format(teamName), "w")
    seasonResults = open('testfile.txt', 'r')

    for line in seasonResults:
        home, away, result, newline = line.split(',')
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
    win = 0
    loss = 0
    draw = 0
    beatenTeam = []
    lostToTeams = []
    drewWith = []
    teamFiles.close()