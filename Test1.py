import pymysql

conn = pymysql.connect(host='104.197.152.81', user='root', passwd='root', db='Football')
cur = conn.cursor()

def InsertTeams(word1,word2,word3,word4,word5,word6,word7,word8,word9,word10,word11,word12,word13,word14):
    conn = pymysql.connect(host='104.197.152.81', user='root', passwd='root', db='Football')
    cur = conn.cursor()
    cur.execute("insert into PremierLeagueResultsAndOdds (HomeTeam, AwayTeam, HomeScore, AwayScore, Winner, Bet365Home, Bet365Draw, Bet365Away, BetAndWinHome, BetAndWinDraw, BetAndWinAway, LadbrokesHome, LadbrokesDraw, LadbrokesAway) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (word1,word2,word3,word4,word5,word6,word7,word8,word9,word10,word11,word12,word13,word14))
    conn.commit()

thisvalue = ['1718']

Teams = ['Arsenal', 'Bournemouth', 'Burnley', 'Brighton', 'Chelsea', 'Crystal Palace', 'Everton',
         'Huddersfield', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Southampton', 'Stoke',
         'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham']

homeTeam = []
awayTeam = []
homeScore = []
awayScore = []
winnerGame = []
Bet365H = []
Bet365D = []
Bet365A = []
BetAndWinH = []
BetAndWinD = []
BetAndWinA = []
LadbrokesH = []
LadbrokesD = []
LadbrokesA = []

for i in thisvalue:
    with open(i+".txt", 'r') as f:
        for line in f:
            for team in Teams:
                if team in line:
                    Home, Away, HS, AS, Result, B365H, B365D, B365A, BWH, BWD, BWA, LBH, LBD, LBA, newline = line.split(',')
                    if Home == team:
                        homeTeam.append(Home)
                        homeScore.append(HS)
                        Bet365H.append(B365H)
                        BetAndWinH.append(BWH)
                        LadbrokesH.append(LBH)

                    elif Away == team:
                        awayTeam.append(Away)
                        awayScore.append(AS)
                        Bet365A.append(B365A)
                        BetAndWinA.append(BWA)
                        LadbrokesA.append(LBA)

                        if int(AS) > int(HS):
                            winnerGame.append(Away)
                        elif int(AS) < int(HS):
                            winnerGame.append(Home)
                        elif int(AS) == int(HS):
                            winnerGame.append("Draw")

                        Bet365D.append(B365D)
                        BetAndWinD.append(BWD)
                        LadbrokesD.append(LBD)

for line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14 in zip([*homeTeam],[*awayTeam],[*homeScore],[*awayScore],[*winnerGame],[*Bet365H],[*Bet365D],[*Bet365A],[*BetAndWinH],[*BetAndWinD],[*BetAndWinA],[*LadbrokesH],[*LadbrokesD],[*LadbrokesA]):
    print('{} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14))
    InsertTeams(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14)

Arsenal = cur.execute("SELECT * FROM PremierLeagueResultsAndOdds")

Teams = ['Arsenal', 'Bournemouth', 'Burnley', 'Brighton', 'Chelsea', 'Crystal Palace', 'Everton',
         'Huddersfield', 'Leicester', 'Liverpool', 'Man City', 'Man United', 'Newcastle', 'Southampton', 'Stoke',
         'Swansea', 'Tottenham', 'Watford', 'West Brom', 'West Ham']

ResultSet = cur.fetchall()
for team in Teams:
    for row in ResultSet:
        if team in row:
            print(str(row))
            cur.execute("insert into " + team.replace(" ","") + "(id, HomeTeam, AwayTeam, HomeScore, AwayScore, Winner, Bet365Home, Bet365Draw, Bet365Away, BetAndWinHome, BetAndWinDraw, BetAndWinAway, LadbrokesHome, LadbrokesDraw, LadbrokesAway) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(row))
            conn.commit()