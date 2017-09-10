fname = 'DKSalaries.csv'
file = open(fname)
line = file.readline()
titles = list()
for title in line.split(','):
    titles.append(title.strip())

players = dict()
lines = file.read().split('\n')
for i in range(len(lines) - 1):
    data = lines[i].split(',')
    #useful---------
    pos = data[0]
    name = data[1]
    salary = data[2]
    #less useful----
    matchup = data[3]
    pts = data[4]
    team = data[5]
    
    if pos not in players.keys():
        players[ pos ] = dict()
    players[ pos ][ name ] = (salary, pts)

        
lineups = list()
limits = {'QB':1, 'RB':3, 'WR':4, 'TE':2, 'DST':1}
salary = 50000
lineup = dict()
#something to loop and set a lineup without weights, just in constraints


#SALARY CAP IS 50,000
#1 QB
#2 RB
#3 WR
#1 TE
#1 DST
#1 (RB, WR, TE)