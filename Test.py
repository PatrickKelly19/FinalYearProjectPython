import csv
import requests

URL = 'http://www.football-data.co.uk/mmz4281/1718/E0.csv'

with requests.Session() as s:
    download = s.get(URL)
    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

    WinCount = 0
    DrawCount = 0
    LossCount = 0

    for row in my_list:
        with open('testfile.txt', 'a') as f:
            f.write(''.join(row[2] + ',' + row[3] + ',' + row[6] + ',') + '\n')

    with open('testfile.txt', 'r') as f:
        for line in f:
            parts = line.split(',', 3)
            if 'Arsenal' in line:
                print(line.split(',', 3))

            Home = parts[0]
            Away = parts[1]
            Result = parts[2]

            if Home == 'Arsenal':
                if Result == 'H':
                    WinCount += 1
                    with open('results.txt', 'a') as f:
                        f.write("Arsenal Won Home: ")
                        f.write(str(WinCount))
                        f.write('\n')
                elif Result == 'D':
                    DrawCount += 1
                    with open('results.txt', 'a') as f:
                        f.write("Arsenal Draw Home: ")
                        f.write('DrawCount')
                        f.write('\n')
                else:
                    LossCount += 1
                    with open('results.txt', 'a') as f:
                        f.write("Arsenal Lost Home: ")
                        f.write('LossCount')
                        f.write('\n')

            if Away == 'Arsenal':
                if Result == 'A':
                    WinCount += 1
                    with open('results.txt', 'a') as f:
                        f.write("Arsenal Won Away Count: ")
                        f.write('WinCount')
                        f.write('\n')
                elif Result == 'D':
                    DrawCount += 1
                    with open('results.txt', 'a') as f:
                        f.write("Arsenal Draw Away Count: ")
                        f.write('DrawCount')
                        f.write('\n')
                else:
                    LossCount += 1
                    with open('results.txt', 'a') as f:
                        f.write("Arsenal Lost Away Count: ")
                        f.write('LossCount')
                        f.write('\n')
