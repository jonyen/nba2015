import nba_py
import calendar
import sys

#month = sys.argv[1]
#year = sys.argv[2]
#team = sys.argv[3]


#game_sequence = headers[1]
#points = headers[21]
#team_abbv = headers[4]

teams = ['POR', 'OKC', 'LAC', 'LAL', 'BKN', 'HOU', 'PHI', 'CLE', 'GSW', 'MIN', 'DEN', 'SAS']

months = [(10,2015), (11,2015)]#, (12,2015), (1,2016), (2,2016), (3,2016), (4,2016)]

for team in teams:
  print "--------" + team + "--------"
  total_wins = 0
  for month_tuple in months:
    month = month_tuple[0]
    year = month_tuple[1]
    start = 1

    if month == 10:
     start = 27

    if month != 10 and month != 11:
      total_wins = 0

    for day in range(start, calendar.monthrange(year, month)[1] + 1):
      s = nba_py.Scoreboard(month, day, year)
  #    print "DATE: " + str(month) + "/" + str(day) + "/" + str(year)

      headers = s.json['resultSets'][1]['headers']
      rows = s.json['resultSets'][1]['rowSet']

      for i in range(len(rows)):
        if rows[i][4] == team:
          team_points = rows[i][21]
          game_sequence = rows[i][1]
  #        print 'Team points: ' + str(team_points)
          for j in range(len(rows)):
            if rows[j][1] == game_sequence and rows[j][4] != team:
              opponent_points = rows[j][21]
  #  	      print 'Opponent points: ' + str(opponent_points)
              if team_points > opponent_points:
                total_wins += 1

  print team + " total wins in " + str(month) + "-" + str(year) + ": " + str(total_wins)

