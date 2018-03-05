import pymysql

Pathtofile = "1617.txt"
def WriteToDB(words):
    print(words)

def InsertHA(word,word1,word2,word3,word4):
    conn = pymysql.connect(host='104.197.152.81', user='root', passwd='root', db='Football')
    cur = conn.cursor()
    cur.execute("insert into Arsenal1617Table (HomeTeam, AwayTeam, HomeScore, AwayScore, Winner) values (%s,%s, %s, %s, %s)", (word,word1,word2,word3,word4))
    conn.commit()

Teams = ['Arsenal', 'Aston Villa', 'Barnsley', 'Birmingham', 'Blackburn', 'Blackpool', 'Bolton',
            'Bournemouth', 'Bradford', 'Brighton', 'Burnley', 'Cardiff', 'Charlton', 'Chelsea', 'Coventry',
             'Crystal Palace', 'Derby', 'Everton', 'Fulham', 'Huddersfield', 'Hull', 'Ipswich', 'Leeds',
             'Leicester',
             'Liverpool', 'Man City', 'Man United', 'Middlesbrough', 'Newcastle', 'Norwich', 'Oldham',
             'Portsmouth',
             'QPR', 'Reading', 'Sheffield United', 'Sheffield Weds', 'Southampton', 'Stoke', 'Sunderland',
             'Swansea',
             'Swindon', 'Tottenham', 'Watford', 'West Brom', 'West Ham', 'Wigan', 'Wimbledon', 'Wolves']

homeTeam = []
awayTeam = []
homeScore = []
awayScore = []
winnerGame = []

with open(Pathtofile, 'r') as f:
    for line in f:
        for team in Teams:
            if team in line:
                Home, Away, HS, AS, Result, newline = line.split(',')
                if Home == team:
                    homeTeam.append(Home)
                    homeScore.append(HS)

                else:
                    i=0
                    # homeTeam.append(Home)
                    # homeScore.append(HS)

                if Away == team:
                    awayTeam.append(Away)
                    awayScore.append(AS)

                    if int(AS) > int(HS):
                        winnerGame.append(Away)
                    elif int(AS) < int(HS):
                        winnerGame.append(Home)
                    elif int(AS) == int(HS):
                        winnerGame.append("Draw")

                else:
                    i=0
                    # awayTeam.append(Away)
                    # awayScore.append(AS)
                    #
                    # if int(AS) > int(HS):
                    #     winnerGame.append(Away)
                    # elif int(AS) < int(HS):
                    #     winnerGame.append(Home)
                    # elif int(AS) == int(HS):
                    #     winnerGame.append("Draw")

for line, line1, line2, line3, line4 in zip([*homeTeam],[*awayTeam],[*homeScore],[*awayScore],[*winnerGame]):
    print('{} {} {} {} {}'.format(line,line1,line2,line3,line4))
    InsertHA(line,line1,line2,line3,line4)