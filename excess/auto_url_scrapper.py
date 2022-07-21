import re
import pyautogui as pg
import time
import clipboard
import json
teams = open("teams.txt", "r")
lines1 = teams.read()
teams_list = lines1.splitlines() #list of teams

teams.close()

#c = 0


time.sleep(5)

for i in range(0, 30):

    team = teams_list[i]
    txt_file = open(f"{team}.txt", "w")
    txt_file.close()

    # chosing the home team

    pg.click(3795, 250, 1, 1)
    pg.click(271, 151, 1, 1)
    pg.click(3074, 822, 1, 2)
    pg.click(1244, 1000, 1, 1)
    pg.keyDown('down')
    pg.hotkey('enter')
    pg.click(3097, 1634, 1, 1)


    # this changes the home team so when the forloop finishes then the new team gets ran

    #count = 0

    for j in range(0, 30):

        time.sleep(2)

        #picks the vs team and runs it

        pg.click(3795, 250, 1, 1)
        pg.click(271, 151, 1, 1)
        pg.click(3074, 822, 1, 2)
        pg.click(1246, 1067, 1, 1)
        pg.keyDown('down')
        pg.hotkey('enter')
        pg.click(3097, 1634, 1, 1)

        # inspect element stuff

        pg.rightClick(3097, 1634, 1, 1)
        pg.click(2962, 1589,1 ,1)

        #inside inspect

        pg.click(1361, 258, 1, 1)
        pg.hotkey('ctrl', 'r')
        time.sleep(2)
        pg.click(1054, 403, 1, 1)
        pg.click(1118, 555, 1, 1)
        pg.click(1516, 809, 1, 1)
        pg.rightClick(2419, 1066, 1, 1)
        pg.click(2495, 1104, 1, 1)

        #the url has now been copied and is being formated to fit the template

        link = clipboard.paste()

        link1 = re.sub("PerGame", r"'+per_mode+'", link)
        new_link = re.sub("2021-22", r"'+season_id+'", link1)

        #the output is the new link which now needs to be pasted into a url txt file

        text_file = open(f"{team}.txt", "a")
        
        text_file.write(new_link)
        text_file.write("\n")
        text_file.close()
        #count = count + 1
    else:
        # once the 30 team match ups happen and the urls are placed in a txt file the count will finish 
        # the two text files teams and urls will be conjoined into a dictionary
        # i will also try to name each dictionary the count

        match_up_link_file = open(f"{team}.txt", "r")
        lines = match_up_link_file.read()

        #creates the list of urls from the txt we made
        
        list_of_urls = lines.splitlines()

        #creatas lines from the team txt we already had

        teams1 = open('teams.txt', 'r')
        lines2 = teams1.read()
        teams_list1 = lines2.splitlines() #list of teams
        teams1.close()

        #dictionary making
        
        matchup_dictionary = dict(zip(teams_list1, list_of_urls))

        dic_file = open(f"{team}_dic.txt", 'w')
        dic_file.write(json.dumps(matchup_dictionary))
        dic_file.close()
        
        

    # cycles the vs teams list back to the default "all teams" so when the loop runs for a new home team it starts from the top

    pg.click(3795, 250, 1, 1)
    time.sleep(1)
    pg.hotkey('ctrl', 'r')
    time.sleep(1)
    pg.click(3074, 822, 1, 1)
    pg.click(1246, 1067, 1, 1)
    time.sleep(1)

    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')
    pg.hotkey('up')


    time.sleep(1)
    pg.hotkey('enter')
    time.sleep(1)
    pg.click(3097, 1634, 1, 1)

        
    
    #c = c + 1
    
