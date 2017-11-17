import csv
import requests

#thisvalue = ['1617', '1516', '1415', '1314', '1213', '1112', '1011', '0910', '0809', '0708', '0607', '0506', '0304', '0203', '0102', '0001', '9900', '9899', '9798', '9697', '9596', '9495', '9394']
thisvalue = ['1617', '1516', '1415']
#Finding a problem with '0405' year, doesnt seem to be an issue but will ignore that year for the time being

for i in thisvalue:
    yearFiles = open("{}.txt".format(i), "w")

    URL = 'http://www.football-data.co.uk/mmz4281/'+i+'/E0.csv'

    with requests.Session() as s:
        download = s.get(URL)
        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

        for row in my_list:
            with open(i+'.txt', 'a') as f:
                f.write(''.join(row[2] + ',' + row[3] + ',' + row[6] + ',') + '\n')

    with open(i+'.txt', 'r') as f:
        Teams = ['Arsenal', 'Aston Villa', 'Barnsley', 'Birmingham', 'Blackburn', 'Blackpool', 'Bolton',
                     'Bournemouth','Bradford', 'Brighton', 'Burnley', 'Cardiff', 'Charlton', 'Chelsea', 'Coventry',
                     'Crystal Palace', 'Derby', 'Everton', 'Fulham', 'Huddersfield', 'Hull', 'Ipswich', 'Leeds', 'Leicester',
                     'Liverpool', 'Man City', 'Man United', 'Middlesbrough', 'Newcastle', 'Norwich', 'Oldham', 'Portsmouth',
                     'QPR', 'Reading', 'Sheffield United', 'Sheffield Weds', 'Southampton', 'Stoke', 'Sunderland', 'Swansea',
                     'Swindon', 'Tottenham', 'Watford', 'West Brom', 'West Ham', 'Wigan', 'Wimbledon', 'Wolves']

        beatenTeam = []
        lostToTeams = []
        drewWith = []
        win = 0
        loss = 0
        draw = 0

        seasonResults = open(i+'.txt', 'r')

        for teamName in Teams:
            teamFiles = open("{}.txt".format(teamName), "w")
            seasonResults = open(i+'.txt', 'r')

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

            teamFiles.write("Premier League Statistics "+i+"\n\n")
            teamFiles.write("Win count = " + str(win) + "\n")
            teamFiles.write("Loss count = " + str(loss) + "\n")
            teamFiles.write("Draw Count = " + str(draw) + "\n")
            teamFiles.write("Beaten Teams = " + str(beatenTeam) + "\n")
            teamFiles.write("Lost to Teams = " + str(lostToTeams) + "\n")
            teamFiles.write("Drew with Teams = " + str(drewWith) + "\n")

            win = 0
            loss = 0
            draw = 0
            beatenTeam = []
            lostToTeams = []
            drewWith = []
            teamFiles.close()