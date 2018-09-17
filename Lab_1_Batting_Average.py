#This is the lab that is done by Daniel Duong and Cameron Kovacik.

baseball_player =(input('Enter your full name:'))
plate_apperances = int(input('Enter the number of times you have taken a turn:'))
singles = int(input('Enter the number the number of singles:'))
doubles = int(input('Enter the number the number of doubles:'))
triples = int(input('Enter the number the number of triples:'))
home_runs = int(input('Enter the number of home runs:'))
at_bats = plate_apperances
total_hits = singles + doubles + triples + home_runs
batting_average = total_hits / at_bats
#To calculate batting average you take all of your hits and divide it by the number of at bats.
slugging_average = ((singles) + (doubles * 2) + (triples * 3) + (home_runs * 4)) / at_bats

print('The player', baseball_player, 'had:', total_hits, 'hits,', singles, 'singles,', doubles, 'doubles,', triples, 'triples,', home_runs, 'homeruns,', \
      'his batting average was', format(batting_average, '.3f'), ',' 'his slugging average was', format(slugging_average, '.3f'))




