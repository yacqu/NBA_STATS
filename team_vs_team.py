# this file runs the home team func
# once the team id of the player is established the corresponding class is ccalled
# then the desired(inputted) away team is established
# the corresponding fuction of the away team is called
# once the match up is established the stat fuction is run inside that.

from all_team import home_team



desired_player = input()

home_team_id = home_team(desired_player)

#create txt file with team id
#use the teams.txt and team_id.txt to create a dictionary
# then call team_id_dictionary[home_team_id]
# create a for loop to create a dictionary of {"ATLxBKN": ATL.bkn(),...., "BKNxBOS": BKN.bos()}
home_team_id_dictionary = {}

away_team = input()

away_team_dictionary = {}

match_up_url_dictionary ={}

