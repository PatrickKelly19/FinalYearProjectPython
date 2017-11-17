Teams = ['Arsenal', 'Aston Villa', 'Barnsley', 'Birmingham', 'Blackburn', 'Blackpool', 'Bolton', 'Bournemouth',
             'Bradford', 'Brighton', 'Burnley', 'Cardiff', 'Charlton', 'Chelsea', 'Coventry', 'Crystal Palace', 'Derby',
             'Everton', 'Fulham', 'Huddersfield', 'Hull', 'Ipswich', 'Leeds', 'Leicester', 'Liverpool', 'Man City',
             'Man United', 'Middlesbrough', 'Newcastle', 'Norwich', 'Oldham', 'Portsmouth', 'QPR', 'Reading',
             'Sheffield United', 'Sheffield Weds', 'Southampton', 'Stoke', 'Sunderland', 'Swansea', 'Swindon', 'Tottenham',
             'Watford', 'West Brom', 'West Ham', 'Wigan', 'Wimbledon', 'Wolves']

beatenTeam=[]
lostToTeams=[]
drewWith=[]
win = 0
loss = 0
draw=0

seasonResults = open('testfile.txt', 'r')
for line in seasonResults:
    home, away, result ,newline = line.split(',')
    if home == 'Arsenal':
        if result == 'H':
            beatenTeam.append(away)
            win += 1
        elif result == 'A':
            lostToTeams.append(away)
            loss += 1
        elif result == 'D':
            drewWith.append(away)
            draw += 1
    elif away == 'Arsenal':
        if result == 'A':
            beatenTeam.append(home)
            win += 1
        elif result == 'H':
            lostToTeams.append(home)
            loss += 1
        elif result == 'D':
            drewWith.append(home)
            draw += 1

    print("beaten Teams")
    print(beatenTeam)
    print("Lost To")
    print(lostToTeams)
    print("drew with")
    print(drewWith)
