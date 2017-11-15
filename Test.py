import csv
import requests

URL = 'http://www.football-data.co.uk/mmz4281/1617/E0.csv'

with requests.Session() as s:
    download = s.get(URL)
    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

    Teams = ["Arsenal", "Aston Villa", "Barnsley", "Birmingham", "Blackburn", "Blackpool", "Bolton", "Bournemouth",
             "Bradford", "Brighton", "Burnley", "Cardiff", "Charlton", "Chelsea", "Coventry", "Crystal Palace", "Derby",
             "Everton", "Fulham", "Huddersfield", "Hull", "Ipswich", "Leeds", "Leicester", "Liverpool", "Man City",
             "Man United", "Middlesbrough", "Newcastle", "Norwich", "Nott'm Forest", "Oldham", "Portsmouth", "QPR", "Reading",
             "Sheffield United", "Sheffield Weds", "Southampton", "Stoke", "Sunderland", "Swansea", "Swindon", "Tottenham",
             "Watford", "West Brom", "West Ham", "Wigan", "Wimbledon", "Wolves"]

    Win = 0
    Loss = 0
    Draw = 0
    p = 0
    BeatTeams = []
    DrawTeams = []
    LossTeams = []

    for row in my_list:
        with open('testfile.txt', 'a') as f:
            f.write(''.join(row[2] + ',' + row[3] + ',' + row[6] + ',') + '\n')

    with open('testfile.txt', 'r') as f:
        for line in f:
            parts = line.split(',', 3)

            Home = parts[0]
            Away = parts[1]
            Result = parts[2]

            if 'Arsenal' in Teams:
                if Home == 'Arsenal':
                    if Result == 'H':
                        Win+=1
                        BeatTeams.insert(p,Away)
                        # print(Away)
                    elif Result == 'D':
                        Draw+=1
                        DrawTeams.insert(p, Away)
                        #print(Away)
                    else:
                        Loss+=1
                        LossTeams.insert(p, Away)
                        #print(Away)

                if Away == 'Arsenal':
                    if Result == 'A':
                        Win += 1
                        BeatTeams.insert(p, Home)
                        #print(Home)
                    elif Result == 'D':
                        Draw += 1
                        DrawTeams.insert(p, Home)
                        #print(Home)
                    else:
                        Loss += 1
                        LossTeams.insert(p, Home)
                        #print(Home)

        with open('results.txt', 'a') as f:
            with open("{}.txt".format('Arsenal'), "w") as f:
                f.write("Team Win Count: ")
                f.write(str(Win))
                f.write("\nTeam Draw Count: ")
                f.write(str(Draw))
                f.write("\nTeam Loss Count: ")
                f.write(str(Loss))
                f.write('\n')
                f.write("\nTeams They Beat: ")
                f.write(str(BeatTeams))
                f.write("\nTeams They Drew With: ")
                f.write(str(DrawTeams))
                f.write("\nTeams They Lost To: ")
                f.write(str(LossTeams))