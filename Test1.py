import pymysql

# Pathtofile = "1617.txt"
# def WriteToDB(words):
#     print(words)
conn = pymysql.connect(host='104.197.152.81', user='root', passwd='root', db='Football')
cur = conn.cursor()

def InsertTeams(word,word1,word2,word3,word4):
    conn = pymysql.connect(host='104.197.152.81', user='root', passwd='root', db='Football')
    cur = conn.cursor()
    cur.execute("insert into PremierLeagueResults (HomeTeam, AwayTeam, HomeScore, AwayScore, Winner) values (%s,%s, %s, %s, %s)", (word,word1,word2,word3,word4))
    conn.commit()

def InsertHA(rowsss, tt):
    print(rowsss)
    print(tt)

thisvalue = ['1617', '1516', '1415', '1314', '1213', '1112', '1011', '0910', '0809', '0708', '0607', '0506', '0304',
                 '0203', '0102', '0001', '9900', '9899', '9798', '9697', '9596', '9495', '9394']

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

for i in thisvalue:
    with open(i+".txt", 'r') as f:
        for line in f:
            for team in Teams:
                if team in line:
                    Home, Away, HS, AS, Result, newline = line.split(',')
                    if Home == team:
                        homeTeam.append(Home)
                        homeScore.append(HS)

                    elif Away == team:
                        awayTeam.append(Away)
                        awayScore.append(AS)

                        if int(AS) > int(HS):
                            winnerGame.append(Away)
                        elif int(AS) < int(HS):
                            winnerGame.append(Home)
                        elif int(AS) == int(HS):
                            winnerGame.append("Draw")

for line, line1, line2, line3, line4 in zip([*homeTeam],[*awayTeam],[*homeScore],[*awayScore],[*winnerGame]):
    i=0
    print('{} {} {} {} {}'.format(line,line1,line2,line3,line4))
    InsertTeams(line,line1,line2,line3,line4)

Arsenal = cur.execute("SELECT * FROM PremierLeagueResults")

Prem = ['Arsenal', 'Bournemouth', 'Burnley', 'Brighton', 'Chelsea', 'Crystal Palace', 'Everton',
         'Huddersfield', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Southampton', 'Stoke',
         'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham']

ResultSet = cur.fetchall()
for team in Prem:
    for row in ResultSet:
        if team in row:
            #InsertHA(row, team)
            print(team)
            print(row)
            cur.execute("insert into " + team.replace(" ","") + "(id, HomeTeam, AwayTeam, HomeScore, AwayScore, Winner) values (%s,%s,%s,%s,%s,%s)",(row))
            conn.commit()