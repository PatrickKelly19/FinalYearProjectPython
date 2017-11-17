import csv
import requests

thisvalue = ['1617', '1516', '1415', '1314', '1213', '1112', '1011', '0910', '0809', '0708', '0607', '0506', '0304', '0203', '0102', '0001', '9900', '9899', '9798', '9697', '9596', '9495', '9394']

#Finding a problem with '0405' year, doesnt seem to be an issue but will ignore that year for the time being

for i in thisvalue:
    print(i)
    yearFiles = open("{}.txt".format(i), "w")

    URL = 'http://www.football-data.co.uk/mmz4281/' + i + '/E0.csv'
    with requests.Session() as s:
        download = s.get(URL)
        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

        for row in my_list:
            yearFiles.write(''.join(row[2] + ',' + row[3] + ',' + row[6] + ',') + '\n')
            print(''.join(row[2] + ',' + row[3] + ',' + row[6] + ',') + '\n')
