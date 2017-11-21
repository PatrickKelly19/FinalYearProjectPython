#Need to fix the amount of decimal places
#Need to fix huddersfield/Sunderland problem with dividing by zero
#Need to se if there is a better way of writing this code

#print(format(bournemouthDrawCount/bournemouthTotal*100, '.2f')) - decimal place formatter

#Team 1
bournemouthWinCount = 0
bournemouthLossCount = 0
bournemouthDrawCount = 0

#Team 2
brightonWinCount = 0
brightonLossCount = 0
brightonDrawCount = 0

#Team 3
burnleyWinCount = 0
burnleyLossCount = 0
burnleyDrawCount = 0

#Team 4
chelseaWinCount = 0
chelseaLossCount = 0
chelseaDrawCount = 0

#Team 5
crystalpalaceWinCount = 0
crystalpalaceLossCount = 0
crystalpalaceDrawCount = 0

#Team 6
evertonWinCount = 0
evertonLossCount = 0
evertonDrawCount = 0

#Team 7
leicesterWinCount = 0
leicesterLossCount = 0
leicesterDrawCount = 0

#Team 8
huddersfieldWinCount = 0
huddersfieldLossCount = 0
huddersfieldDrawCount = 0

#Team 9
liverpoolWinCount = 0
liverpoolLossCount = 0
liverpoolDrawCount = 0

#Team 10
mancityWinCount = 0
mancityLossCount = 0
mancityDrawCount = 0

#Team 11
manunitedWinCount = 0
manunitedLossCount = 0
manunitedDrawCount = 0

#Team 12
newcastleWinCount = 0
newcastleLossCount = 0
newcastleDrawCount = 0

#Team 13
southamptonWinCount = 0
southamptonLossCount = 0
southamptonDrawCount = 0

#Team 14
stokeWinCount = 0
stokeLossCount = 0
stokeDrawCount = 0

#Team 15
sunderlandWinCount = 0
sunderlandLossCount = 0
sunderlandDrawCount = 0

#Team 16
swanseaWinCount = 0
swanseaLossCount = 0
swanseaDrawCount = 0

#Team 17
tottenhamWinCount = 0
tottenhamLossCount = 0
tottenhamDrawCount = 0

#Team 18
watfordWinCount = 0
watfordLossCount = 0
watfordDrawCount = 0

#Team 19
westbromWinCount = 0
westbromLossCount = 0
westbromDrawCount = 0

#Team 20
westhamWinCount = 0
westhamLossCount = 0
westhamDrawCount = 0

file = open(r"Arsenal.txt", "r", encoding="utf-8-sig")
for line in file:
    if line.startswith('Beaten Teams ='):
        if 'Bournemouth' in line:
            if line.count('Bournemouth') == 2:
                bournemouthWinCount += 2
            elif line.count('Bournemouth') == 1:
                bournemouthWinCount += 1
            else:
                bournemouthWinCount += 0

        if 'Brighton' in line:
            if line.count('Brighton') == 2:
                brightonWinCount += 2
            elif line.count('Brighton') == 1:
                brightonWinCount += 1
            else:
                brightonWinCount += 0

        if 'Burnley' in line:
            if line.count('Burnley') == 2:
                burnleyWinCount += 2
            elif line.count('Burnley') == 1:
                burnleyWinCount += 1
            else:
                burnleyWinCount += 0

        if 'Chelsea' in line:
            if line.count('Chelsea') == 2:
                chelseaWinCount += 2
            elif line.count('Chelsea') == 1:
                chelseaWinCount+=1
            else:
                chelseaWinCount+=0

        if 'Crystal Palace' in line:
            if line.count('Crystal Palace') == 2:
                crystalpalaceWinCount += 2
            elif line.count('Crystal Palace') == 1:
                crystalpalaceWinCount += 1
            else:
                crystalpalaceWinCount += 0

        if 'Everton' in line:
            if line.count('Everton') == 2:
                evertonWinCount += 2
            elif line.count('Everton') == 1:
                evertonWinCount += 1
            else:
                evertonWinCount += 0

        if 'Huddersfield' in line:
            if line.count('Huddersfield') == 2:
                huddersfieldWinCount += 2
            elif line.count('Southampton') == 1:
                huddersfieldWinCount += 1
            else:
                huddersfieldWinCount += 0

        if 'Leicester' in line:
            if line.count('Leicester') == 2:
                leicesterWinCount += 2
            elif line.count('Leicester') == 1:
                leicesterWinCount += 1
            else:
                leicesterWinCount += 0

        if 'Liverpool' in line:
            if line.count('Liverpool') == 2:
                liverpoolWinCount += 2
            elif line.count('Liverpool') == 1:
                liverpoolWinCount += 1
            else:
                liverpoolWinCount += 0

        if 'Man City' in line:
            if line.count('Man City') == 2:
                mancityWinCount += 2
            elif line.count('Man City') == 1:
                mancityWinCount += 1
            else:
                mancityWinCount += 0

        if 'Man United' in line:
            if line.count('Man United') == 2:
                manunitedWinCount += 2
            elif line.count('Man United') == 1:
                manunitedWinCount += 1
            else:
                manunitedWinCount += 0

        if 'Newcastle' in line:
            if line.count('Newcastle') == 2:
                newcastleWinCount += 2
            elif line.count('Newcastle') == 1:
                newcastleWinCount += 1
            else:
                newcastleWinCount += 0

        if 'Southampton' in line:
            if line.count('Southampton') == 2:
                southamptonWinCount += 2
            elif line.count('Southampton') == 1:
                southamptonWinCount += 1
            else:
                southamptonWinCount += 0

        if 'Stoke' in line:
            if line.count('Stoke') == 2:
                stokeWinCount += 2
            elif line.count('Stoke') == 1:
                stokeWinCount += 1
            else:
                stokeWinCount += 0

        if 'Swansea' in line:
            if line.count('Swansea') == 2:
                swanseaWinCount += 2
            elif line.count('Swansea') == 1:
                swanseaWinCount += 1
            else:
                swanseaWinCount += 0

        if 'Tottenham' in line:
            if line.count('Tottenham') == 2:
                tottenhamWinCount += 2
            elif line.count('Tottenham') == 1:
                tottenhamWinCount += 1
            else:
                tottenhamWinCount += 0

        if 'Watford' in line:
            if line.count('Watford') == 2:
                watfordWinCount += 2
            elif line.count('Watford') == 1:
                watfordWinCount += 1
            else:
                watfordWinCount += 0

        if 'West Brom' in line:
            if line.count('West Brom') == 2:
                westbromWinCount += 2
            elif line.count('West Brom') == 1:
                westbromWinCount += 1
            else:
                westbromWinCount += 0

        if 'West Ham' in line:
            if line.count('West Ham') == 2:
                westhamWinCount += 2
            elif line.count('West Ham') == 1:
                westhamWinCount += 1
            else:
                westhamWinCount += 0

    if line.startswith('Lost to Teams ='):
        if 'Bournemouth' in line:
            if line.count('Bournemouth') == 2:
                bournemouthLossCount += 2
            elif line.count('Bournemouth') == 1:
                bournemouthLossCount += 1
            else:
                bournemouthLossCount += 0

        if 'Brighton' in line:
            if line.count('Brighton') == 2:
                brightonLossCount += 2
            elif line.count('Brighton') == 1:
                brightonLossCount += 1
            else:
                brightonLossCount += 0

        if 'Burnley' in line:
            if line.count('Burnley') == 2:
                burnleyLossCount += 2
            elif line.count('Burnley') == 1:
                burnleyLossCount += 1
            else:
                burnleyLossCount += 0

        if 'Chelsea' in line:
            if line.count('Chelsea') == 2:
                chelseaLossCount += 2
            elif line.count('Chelsea') == 1:
                chelseaLossCount += 1
            else:
                chelseaLossCount += 0

        if 'Crystal Palace' in line:
            if line.count('Crystal Palace') == 2:
                crystalpalaceLossCount += 2
            elif line.count('Crystal Palace') == 1:
                crystalpalaceLossCount += 1
            else:
                crystalpalaceLossCount += 0

        if 'Everton' in line:
            if line.count('Everton') == 2:
                evertonLossCount += 2
            elif line.count('Everton') == 1:
                evertonLossCount += 1
            else:
                evertonLossCount += 0

        if 'Huddersfield' in line:
            if line.count('Huddersfield') == 2:
                huddersfieldLossCount += 2
            elif line.count('Southampton') == 1:
                huddersfieldLossCount += 1
            else:
                huddersfieldLossCount += 0

        if 'Leicester' in line:
            if line.count('Leicester') == 2:
                leicesterLossCount += 2
            elif line.count('Leicester') == 1:
                leicesterLossCount += 1
            else:
                leicesterLossCount += 0

        if 'Liverpool' in line:
            if line.count('Liverpool') == 2:
                liverpoolLossCount += 2
            elif line.count('Liverpool') == 1:
                liverpoolLossCount += 1
            else:
                liverpoolLossCount += 0

        if 'Man City' in line:
            if line.count('Man City') == 2:
                mancityLossCount += 2
            elif line.count('Man City') == 1:
                mancityLossCount += 1
            else:
                mancityLossCount += 0

        if 'Man United' in line:
            if line.count('Man United') == 2:
                manunitedLossCount += 2
            elif line.count('Man United') == 1:
                manunitedLossCount += 1
            else:
                manunitedLossCount += 0

        if 'Newcastle' in line:
            if line.count('Newcastle') == 2:
                newcastleLossCount += 2
            elif line.count('Newcastle') == 1:
                newcastleLossCount += 1
            else:
                newcastleLossCount += 0

        if 'Southampton' in line:
            if line.count('Southampton') == 2:
                southamptonLossCount += 2
            elif line.count('Southampton') == 1:
                southamptonLossCount += 1
            else:
                southamptonLossCount += 0

        if 'Stoke' in line:
            if line.count('Stoke') == 2:
                stokeLossCount += 2
            elif line.count('Stoke') == 1:
                stokeLossCount += 1
            else:
                stokeLossCount += 0

        if 'Swansea' in line:
            if line.count('Swansea') == 2:
                swanseaLossCount += 2
            elif line.count('Swansea') == 1:
                swanseaLossCount += 1
            else:
                swanseaLossCount += 0

        if 'Tottenham' in line:
            if line.count('Tottenham') == 2:
                tottenhamLossCount += 2
            elif line.count('Tottenham') == 1:
                tottenhamLossCount += 1
            else:
                tottenhamLossCount += 0

        if 'Watford' in line:
            if line.count('Watford') == 2:
                watfordLossCount += 2
            elif line.count('Watford') == 1:
                watfordLossCount += 1
            else:
                watfordLossCount += 0

        if 'West Brom' in line:
            if line.count('West Brom') == 2:
                westbromLossCount += 2
            elif line.count('West Brom') == 1:
                westbromLossCount += 1
            else:
                westbromLossCount += 0

        if 'West Ham' in line:
            if line.count('West Ham') == 2:
                westhamLossCount += 2
            elif line.count('West Ham') == 1:
                westhamLossCount += 1
            else:
                westhamLossCount += 0

    if line.startswith('Drew with Teams ='):
        if 'Bournemouth' in line:
            if line.count('Bournemouth') == 2:
                bournemouthDrawCount += 2
            elif line.count('Bournemouth') == 1:
                bournemouthDrawCount += 1
            else:
                bournemouthDrawCount += 0

        if 'Brighton' in line:
            if line.count('Brighton') == 2:
                brightonDrawCount += 2
            elif line.count('Brighton') == 1:
                brightonDrawCount += 1
            else:
                brightonDrawCount += 0

        if 'Burnley' in line:
            if line.count('Burnley') == 2:
                burnleyDrawCount += 2
            elif line.count('Burnley') == 1:
                burnleyDrawCount += 1
            else:
                burnleyDrawCount += 0

        if 'Chelsea' in line:
            if line.count('Chelsea') == 2:
                chelseaDrawCount += 2
            elif line.count('Chelsea') == 1:
                chelseaDrawCount += 1
            else:
                chelseaDrawCount += 0

        if 'Crystal Palace' in line:
            if line.count('Crystal Palace') == 2:
                crystalpalaceDrawCount += 2
            elif line.count('Crystal Palace') == 1:
                crystalpalaceDrawCount += 1
            else:
                crystalpalaceDrawCount += 0

        if 'Everton' in line:
            if line.count('Everton') == 2:
                evertonDrawCount += 2
            elif line.count('Everton') == 1:
                evertonDrawCount += 1
            else:
                evertonDrawCount += 0

        if 'Huddersfield' in line:
            if line.count('Huddersfield') == 2:
                huddersfieldDrawCount += 2
            elif line.count('Southampton') == 1:
                huddersfieldDrawCount += 1
            else:
                huddersfieldDrawCount += 0

        if 'Leicester' in line:
            if line.count('Leicester') == 2:
                leicesterDrawCount += 2
            elif line.count('Leicester') == 1:
                leicesterDrawCount += 1
            else:
                leicesterDrawCount += 0

        if 'Liverpool' in line:
            if line.count('Liverpool') == 2:
                liverpoolDrawCount += 2
            elif line.count('Liverpool') == 1:
                liverpoolDrawCount += 1
            else:
                liverpoolDrawCount += 0

        if 'Man City' in line:
            if line.count('Man City') == 2:
                mancityDrawCount += 2
            elif line.count('Man City') == 1:
                mancityDrawCount += 1
            else:
                mancityDrawCount += 0

        if 'Man United' in line:
            if line.count('Man United') == 2:
                manunitedDrawCount += 2
            elif line.count('Man United') == 1:
                manunitedDrawCount += 1
            else:
                manunitedDrawCount += 0

        if 'Newcastle' in line:
            if line.count('Newcastle') == 2:
                newcastleDrawCount += 2
            elif line.count('Newcastle') == 1:
                newcastleDrawCount += 1
            else:
                newcastleDrawCount += 0

        if 'Southampton' in line:
            if line.count('Southampton') == 2:
                southamptonDrawCount += 2
            elif line.count('Southampton') == 1:
                southamptonDrawCount += 1
            else:
                southamptonDrawCount += 0

        if 'Stoke' in line:
            if line.count('Stoke') == 2:
                stokeDrawCount += 2
            elif line.count('Stoke') == 1:
                stokeDrawCount += 1
            else:
                stokeDrawCount += 0

        if 'Swansea' in line:
            if line.count('Swansea') == 2:
                swanseaDrawCount += 2
            elif line.count('Swansea') == 1:
                swanseaDrawCount += 1
            else:
                swanseaDrawCount += 0

        if 'Tottenham' in line:
            if line.count('Tottenham') == 2:
                tottenhamDrawCount += 2
            elif line.count('Tottenham') == 1:
                tottenhamDrawCount += 1
            else:
                tottenhamDrawCount += 0

        if 'Watford' in line:
            if line.count('Watford') == 2:
                watfordDrawCount += 2
            elif line.count('Watford') == 1:
                watfordDrawCount += 1
            else:
                watfordDrawCount += 0

        if 'West Brom' in line:
            if line.count('West Brom') == 2:
                westbromDrawCount += 2
            elif line.count('West Brom') == 1:
                westbromDrawCount += 1
            else:
                westbromDrawCount += 0

        if 'West Ham' in line:
            if line.count('West Ham') == 2:
                westhamDrawCount += 2
            elif line.count('West Ham') == 1:
                westhamDrawCount += 1
            else:
                westhamDrawCount += 0


#Team 1
print('Arsenal Wins Against Bournemouth: ' + str(bournemouthWinCount))
print('Arsenal Losses Against Bournemouth: ' + str(bournemouthLossCount))
print('Arsenal Draws Against Bournemouth: ' + str(bournemouthDrawCount))
print('Arsenal Total Number of Games Against Bournemouth: ',bournemouthWinCount + bournemouthLossCount + bournemouthDrawCount)
bournemouthTotal = bournemouthWinCount + bournemouthLossCount + bournemouthDrawCount
print('Arsenal Win Percentage Against Bournemouth: ',bournemouthWinCount/bournemouthTotal*100, '%')
print('Arsenal Loss Percentage Against Bournemouth: ',bournemouthLossCount/bournemouthTotal*100, '%')
print('Arsenal Draw Percentage Against Bournemouth: ',bournemouthDrawCount/bournemouthTotal*100, '%')
print(format(bournemouthDrawCount/bournemouthTotal*100, '.2f'))
print('\n')

#Team 2
print('Arsenal Wins Against Brighton: ' + str(brightonWinCount))
print('Arsenal Losses Against Brighton: ' + str(brightonLossCount))
print('Arsenal Draws Against Brighton: ' + str(brightonDrawCount))
print('Arsenal Total Number of Games Against Brighton: ',brightonWinCount + brightonLossCount + brightonDrawCount)
brightonTotal = brightonWinCount + brightonLossCount + brightonDrawCount
print('Arsenal Win Percentage Against Brighton: ',brightonWinCount/brightonTotal*100, '%')
print('Arsenal Loss Percentage Against Brighton: ',brightonLossCount/brightonTotal*100, '%')
print('Arsenal Draw Percentage Against Brighton: ',brightonDrawCount/brightonTotal*100, '%')
print('\n')

#Team 3
print('Arsenal Wins Against Burnley: ' + str(burnleyWinCount))
print('Arsenal Losses Against Burnley: ' + str(burnleyLossCount))
print('Arsenal Draws Against Burnley: ' + str(burnleyDrawCount))
print('Arsenal Total Number of Games Against Burnley: ',burnleyWinCount + burnleyLossCount + burnleyDrawCount)
burnleyTotal = burnleyWinCount + burnleyLossCount + burnleyDrawCount
print('Arsenal Win Percentage Against Burnley: ',burnleyWinCount/burnleyTotal*100, '%')
print('Arsenal Loss Percentage Against Burnley: ',burnleyLossCount/burnleyTotal*100, '%')
print('Arsenal Draw Percentage Against Burnley: ',burnleyDrawCount/burnleyTotal*100, '%')
print('\n')

#Team 4
print('Arsenal Wins Against Chelsea: ' + str(chelseaWinCount))
print('Arsenal Losses Against Chelsea: ' + str(chelseaLossCount))
print('Arsenal Draws Against Chelsea: ' + str(chelseaDrawCount))
print('Arsenal Total Number of Games Against Chelsea: ',chelseaWinCount + chelseaLossCount + chelseaDrawCount)
chelseaTotal = chelseaWinCount + chelseaLossCount + chelseaDrawCount
print('Arsenal Win Percentage Against Chelsea: ',chelseaWinCount/chelseaTotal*100, '%')
print('Arsenal Loss Percentage Against Chelsea: ',chelseaLossCount/chelseaTotal*100, '%')
print('Arsenal Draw Percentage Against Chelsea: ',chelseaDrawCount/chelseaTotal*100, '%')
print('\n')

#Team 5
print('Arsenal Wins Against Crystal Palace: ' + str(crystalpalaceWinCount))
print('Arsenal Losses Against Crystal Palace: ' + str(crystalpalaceLossCount))
print('Arsenal Draws Against Crystal Palace: ' + str(crystalpalaceDrawCount))
print('Arsenal Total Number of Games Against Crystal Palace: ',crystalpalaceWinCount + crystalpalaceLossCount + crystalpalaceDrawCount)
crystalpalaceTotal = crystalpalaceWinCount + crystalpalaceLossCount + crystalpalaceDrawCount
print('Arsenal Win Percentage Against Crystal Palace: ',crystalpalaceWinCount/crystalpalaceTotal*100, '%')
print('Arsenal Loss Percentage Against Crystal Palace: ',crystalpalaceLossCount/crystalpalaceTotal*100, '%')
print('Arsenal Draw Percentage Against Crystal Palace: ',crystalpalaceDrawCount/crystalpalaceTotal*100, '%')
print('\n')

#Team 6
print('Arsenal Wins Against Everton: ' + str(evertonWinCount))
print('Arsenal Losses Against Everton: ' + str(evertonLossCount))
print('Arsenal Draws Against Everton: ' + str(evertonDrawCount))
print('Arsenal Total Number of Games Against Everton: ',evertonWinCount + evertonLossCount + evertonDrawCount)
evertonTotal = evertonWinCount + evertonLossCount + evertonDrawCount
print('Arsenal Win Percentage Against Everton: ',evertonWinCount/evertonTotal*100, '%')
print('Arsenal Loss Percentage Against Everton: ',evertonLossCount/evertonTotal*100, '%')
print('Arsenal Draw Percentage Against Everton: ',evertonDrawCount/evertonTotal*100, '%')
print('\n')

#Team 7
print('Arsenal Wins Against Leicester: ' + str(leicesterWinCount))
print('Arsenal Losses Against Leicester: ' + str(leicesterLossCount))
print('Arsenal Draws Against Leicester: ' + str(leicesterDrawCount))
print('Arsenal Total Number of Games Against Leicester: ',leicesterWinCount + leicesterLossCount + leicesterDrawCount)
leicesterTotal = leicesterWinCount + leicesterLossCount + leicesterDrawCount
print('Arsenal Win Percentage Against Leicester: ',leicesterWinCount/leicesterTotal*100, '%')
print('Arsenal Loss Percentage Against Leicester: ',leicesterLossCount/leicesterTotal*100, '%')
print('Arsenal Draw Percentage Against Leicester: ',leicesterDrawCount/leicesterTotal*100, '%')
print('\n')

#Team 8 #Need to error check if they divide by zero
# print('Arsenal Wins Against Huddersfield: ' + str(huddersfieldWinCount))
# print('Arsenal Losses Against Huddersfield: ' + str(huddersfieldLossCount))
# print('Arsenal Draws Against Huddersfield: ' + str(huddersfieldDrawCount))
# print('Arsenal Total Number of Games Against Huddersfield: ',huddersfieldWinCount + huddersfieldLossCount + huddersfieldDrawCount)
# huddersfieldTotal = huddersfieldWinCount + huddersfieldLossCount + huddersfieldDrawCount
# print('Arsenal Win Percentage Against Huddersfield: ',huddersfieldWinCount/huddersfieldTotal*100, '%')
# print('Arsenal Loss Percentage Against Huddersfield: ',huddersfieldLossCount/huddersfieldTotal*100, '%')
# print('Arsenal Draw Percentage Against Huddersfield: ',huddersfieldDrawCount/huddersfieldTotal*100, '%')
# print('\n')

#Team 9
print('Arsenal Wins Against Liverpool: ' + str(liverpoolWinCount))
print('Arsenal Losses Against Liverpool: ' + str(liverpoolLossCount))
print('Arsenal Draws Against Liverpool: ' + str(liverpoolDrawCount))
print('Arsenal Total Number of Games Against Liverpool: ',liverpoolWinCount + liverpoolLossCount + liverpoolDrawCount)
liverpoolTotal = liverpoolWinCount + liverpoolLossCount + liverpoolDrawCount
print('Arsenal Win Percentage Against Liverpool: ',liverpoolWinCount/liverpoolTotal*100, '%')
print('Arsenal Loss Percentage Against Liverpool: ',liverpoolLossCount/liverpoolTotal*100, '%')
print('Arsenal Draw Percentage Against Liverpool: ',liverpoolDrawCount/liverpoolTotal*100, '%')
print('\n')

#Team 10
print('Arsenal Wins Against Man City: ' + str(mancityWinCount))
print('Arsenal Losses Against Man City: ' + str(mancityLossCount))
print('Arsenal Draws Against Man City: ' + str(mancityDrawCount))
print('Arsenal Total Number of Games Against Man City: ',mancityWinCount + mancityLossCount + mancityDrawCount)
mancityTotal = mancityWinCount + mancityLossCount + mancityDrawCount
print('Arsenal Win Percentage Against Man City: ',mancityWinCount/mancityTotal*100, '%')
print('Arsenal Loss Percentage Against Man City: ',mancityLossCount/mancityTotal*100, '%')
print('Arsenal Draw Percentage Against Man City: ',mancityDrawCount/mancityTotal*100, '%')
print('\n')

#Team 11
print('Arsenal Wins Against Man United: ' + str(manunitedWinCount))
print('Arsenal Losses Against Man United: ' + str(manunitedLossCount))
print('Arsenal Draws Against Man United: ' + str(manunitedDrawCount))
print('Arsenal Total Number of Games Against Man United: ',manunitedWinCount + manunitedLossCount + manunitedDrawCount)
manunitedTotal = manunitedWinCount + manunitedLossCount + manunitedDrawCount
print('Arsenal Win Percentage Against Man United: ',manunitedWinCount/manunitedTotal*100, '%')
print('Arsenal Loss Percentage Against Man United: ',manunitedLossCount/manunitedTotal*100, '%')
print('Arsenal Draw Percentage Against Man United: ',manunitedDrawCount/manunitedTotal*100, '%')
print('\n')

#Team 12
print('Arsenal Wins Against Newcastle: ' + str(newcastleWinCount))
print('Arsenal Losses Against Newcastle: ' + str(newcastleLossCount))
print('Arsenal Draws Against Newcastle: ' + str(newcastleDrawCount))
print('Arsenal Total Number of Games Against Newcastle: ',newcastleWinCount + newcastleLossCount + newcastleDrawCount)
newcastleTotal = newcastleWinCount + newcastleLossCount + newcastleDrawCount
print('Arsenal Win Percentage Against Newcastle: ',newcastleWinCount/newcastleTotal*100, '%')
print('Arsenal Loss Percentage Against Newcastle: ',newcastleLossCount/newcastleTotal*100, '%')
print('Arsenal Draw Percentage Against Newcastle: ',newcastleDrawCount/newcastleTotal*100, '%')
print('\n')

#Team 13

print('Wins Against Southampton: ' + str(southamptonWinCount))
print('Losses Against Southampton: ' + str(southamptonLossCount))
print('Draws Against Southampton: ' + str(southamptonDrawCount))
print('Total Number of Games Against Southampton: ',southamptonWinCount + southamptonLossCount + southamptonDrawCount)
southamptonTotal = southamptonWinCount + southamptonLossCount + southamptonDrawCount
print('Win Percentage Against Southampton',southamptonWinCount/southamptonTotal*100, '%')
print('Loss Percentage Against Southampton',southamptonLossCount/southamptonTotal*100, '%')
print('Draw Percentage Against Southampton',southamptonDrawCount/southamptonTotal*100, '%')

#Team 14
print('Arsenal Wins Against Stoke: ' + str(stokeWinCount))
print('Arsenal Losses Against Stoke: ' + str(stokeLossCount))
print('Arsenal Draws Against Stoke: ' + str(stokeDrawCount))
print('Arsenal Total Number of Games Against Stoke: ',stokeWinCount + stokeLossCount + stokeDrawCount)
stokeTotal = stokeWinCount + stokeLossCount + stokeDrawCount
print('Arsenal Win Percentage Against Stoke: ',stokeWinCount/stokeTotal*100, '%')
print('Arsenal Loss Percentage Against Stoke: ',stokeLossCount/stokeTotal*100, '%')
print('Arsenal Draw Percentage Against Stoke: ',stokeDrawCount/stokeTotal*100, '%')
print('\n')

#Team 15
# print('Arsenal Wins Against Sunderland: ' + str(sunderlandWinCount))
# print('Arsenal Losses Against Sunderland: ' + str(sunderlandLossCount))
# print('Arsenal Draws Against Sunderland: ' + str(sunderlandDrawCount))
# print('Arsenal Total Number of Games Against Sunderland: ',sunderlandWinCount + sunderlandLossCount + sunderlandDrawCount)
# sunderlandTotal = sunderlandWinCount + sunderlandLossCount + sunderlandDrawCount
# print('Arsenal Win Percentage Against Sunderland: ',sunderlandWinCount/sunderlandTotal*100, '%')
# print('Arsenal Loss Percentage Against Sunderland: ',sunderlandLossCount/sunderlandTotal*100, '%')
# print('Arsenal Draw Percentage Against Sunderland: ',sunderlandDrawCount/sunderlandTotal*100, '%')
# print('\n')

#Team 16
print('Arsenal Wins Against Swansea: ' + str(swanseaWinCount))
print('Arsenal Losses Against Swansea: ' + str(swanseaLossCount))
print('Arsenal Draws Against Swansea: ' + str(swanseaDrawCount))
print('Arsenal Total Number of Games Against Swansea: ',swanseaWinCount + swanseaLossCount + swanseaDrawCount)
swanseaTotal = swanseaWinCount + swanseaLossCount + swanseaDrawCount
print('Arsenal Win Percentage Against Swansea: ',swanseaWinCount/swanseaTotal*100, '%')
print('Arsenal Loss Percentage Against Swansea: ',swanseaLossCount/swanseaTotal*100, '%')
print('Arsenal Draw Percentage Against Swansea: ',swanseaDrawCount/swanseaTotal*100, '%')
print('\n')

#Team 17
print('Arsenal Wins Against Tottenham: ' + str(tottenhamWinCount))
print('Arsenal Losses Against Tottenham: ' + str(tottenhamLossCount))
print('Arsenal Draws Against Tottenham: ' + str(tottenhamDrawCount))
print('Arsenal Total Number of Games Against Tottenham: ',tottenhamWinCount + tottenhamLossCount + tottenhamDrawCount)
tottenhamTotal = tottenhamWinCount + tottenhamLossCount + tottenhamDrawCount
print('Arsenal Win Percentage Against Tottenham: ',tottenhamWinCount/tottenhamTotal*100, '%')
print('Arsenal Loss Percentage Against Tottenham: ',tottenhamLossCount/tottenhamTotal*100, '%')
print('Arsenal Draw Percentage Against Tottenham: ',tottenhamDrawCount/tottenhamTotal*100, '%')
print('\n')

#Team 18
print('Arsenal Wins Against Watford: ' + str(watfordWinCount))
print('Arsenal Losses Against Watford: ' + str(watfordLossCount))
print('Arsenal Draws Against Watford: ' + str(watfordDrawCount))
print('Arsenal Total Number of Games Against Watford: ',watfordWinCount + watfordLossCount + watfordDrawCount)
watfordTotal = watfordWinCount + watfordLossCount + watfordDrawCount
print('Arsenal Win Percentage Against Watford: ',watfordWinCount/watfordTotal*100, '%')
print('Arsenal Loss Percentage Against Watford: ',watfordLossCount/watfordTotal*100, '%')
print('Arsenal Draw Percentage Against Watford: ',watfordDrawCount/watfordTotal*100, '%')
print(format(watfordWinCount/watfordTotal*100, '.2f'))
print('\n')

#Team 19
print('Arsenal Wins Against West Brom: ' + str(westbromWinCount))
print('Arsenal Losses Against West Brom: ' + str(westbromLossCount))
print('Arsenal Draws Against West Brom: ' + str(westbromDrawCount))
print('Arsenal Total Number of Games Against West Brom: ',westbromWinCount + westbromLossCount + westbromDrawCount)
westbromTotal = westbromWinCount + westbromLossCount + westbromDrawCount
print('Arsenal Win Percentage Against West Brom: ',westbromWinCount/westbromTotal*100, '%')
print('Arsenal Loss Percentage Against West Brom: ',westbromLossCount/westbromTotal*100, '%')
print('Arsenal Draw Percentage Against West Brom: ',westbromDrawCount/westbromTotal*100, '%')
print('\n')

#Team 20
print('Arsenal Wins Against West Ham: ' + str(westhamWinCount))
print('Arsenal Losses Against West Ham: ' + str(westhamLossCount))
print('Arsenal Draws Against West Ham: ' + str(westhamDrawCount))
print('Arsenal Total Number of Games Against West Ham: ',westhamWinCount + westhamLossCount + westhamDrawCount)
westhamTotal = westhamWinCount + westhamLossCount + westhamDrawCount
print('Arsenal Win Percentage Against West Ham ',westhamWinCount/westhamTotal*100, '%')
print('Arsenal Loss Percentage Against West Ham: ',westhamLossCount/westhamTotal*100, '%')
print('Arsenal Draw Percentage Against West Ham: ',westhamDrawCount/westhamTotal*100, '%')
print('\n')