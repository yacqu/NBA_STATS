import re
import clipboard


teams = open('teams.txt', 'r')
lines1 = teams.read()
teams_list = lines1.splitlines() #list of teams

team = (teams_list[3])

txt_file = open("%s.txt" % team, "w")

print(team)

teams.close()


    



