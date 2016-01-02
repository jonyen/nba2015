import nba_py
import calendar
import sys

#game_sequence = headers[1]
#points = headers[21]
#team_abbv = headers[4]

johnny_teams = ['POR', 'OKC', 'LAC', 'LAL', 'BKN', 'HOU']
jonyen_teams = ['PHI', 'CLE', 'GSW', 'MIN', 'DEN', 'SAS']
teams = johnny_teams + jonyen_teams
#all_teams = ['POR','OKC','LAC','LAL','BKN','HOU','PHI','CLE','GSW','MIN','DEN','SAS','MEM','PHX','NOP','UTA','SAC','CHI','IND','WAS','MIA','CHA','BOS','TOR','MIL','DET','NYK','ATL','ORL','DAL']

#months = [(10,2015), (11,2015)]#, (12,2015), (1,2016), (2,2016), (3,2016), (4,2016)]
months = [(12,2015)]#, (1,2016), (2,2016), (3,2016), (4,2016)]

johnny_wins = {}
jonyen_wins = {}

season_start = '10-27-2015'
season_end = '4-13-2016'

for month_tuple in months:
  month = month_tuple[0]
  year = month_tuple[1]
  start = 1

  johnny_wins[month] = 0
  jonyen_wins[month] = 0

  if month == 10:
    start = 27

  end = calendar.monthrange(year, month)[1] + 1

  if month != 11:
    wins_by_month = {}
    for team in teams:
      wins_by_month[team] = 0

  for day in range(start, end):
    s = nba_py.Scoreboard(month, day, year)
    for team in teams:
      headers = s.json['resultSets'][1]['headers']
      rows = s.json['resultSets'][1]['rowSet']

      for i in range(len(rows)):
        if rows[i][4] == team:
          team_points = rows[i][21]
          game_sequence = rows[i][1]
          if (rows[i-1][1] == game_sequence):
            opponent_points = rows[i-1][21]
            if team_points > opponent_points:
              wins_by_month[team] += 1
	      if team in johnny_teams:
		johnny_wins[month] += 1
	      if team in jonyen_teams:
		jonyen_wins[month] += 1
          if (i != len(rows) - 1 and rows[i+1][1] == game_sequence):
            opponent_points = rows[i+1][21]
            if team_points > opponent_points:
              wins_by_month[team] += 1
	      if team in johnny_teams:
		johnny_wins[month] += 1
	      if team in jonyen_teams:
		jonyen_wins[month] += 1
  if month != 10:
    for team in johnny_teams:
      print team + "\t (" + str(month) + "-" + str(year) + "):\t " + str(wins_by_month[team])
    print "--------------"
    print "Johnny Total: " + str(johnny_wins[month])
    print
    for team in jonyen_teams:
      print team + "\t (" + str(month) + "-" + str(year) + "):\t " + str(wins_by_month[team])
    print "--------------"
    print "JonYen Total: " + str(jonyen_wins[month])
