# automate team fucntions for urls


count = 0

if count < 30:
    team_file = open('teams.txt', "r") 
    team = team_file.readline(count)
    team_file.close()
    url_file = open('atl{count}.txt', 'r')
    url = url_file.readline(count)

    team_func = """def %s():
                        season_id = '2021-22'
                        per_mode = 'PerGame'

                        player_info_url = '%s'
        
        
                        #use this header to fool adam silver

                        headers = {
                            'Connection': 'keep-alive',
                            'Accept': 'application/json, text/plain, */*',
                            'x-nba-stats-token': 'true',
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                            'x-nba-stats-origin': 'stats',
                            'Sec-Fetch-Site': 'same-origin',
                            'Sec-Fetch-Mode': 'cors',
                            'Referer': 'https://stats.nba.com/',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9',
                         }

                        response = requests.get(url=player_info_url, headers=headers).json()

                        player_info = response['resultSets'][0]['rowSet']


                        # coloumn names from nba.stats

                        columns_list = [
                            # 'season_id' add in for for loop later
                            "PLAYER_ID",
                            "PLAYER_NAME",
                            "NICKNAME",
                            "TEAM_ID",
                            "TEAM_ABBREVIATION",
                            "AGE",
                            "GP",
                            "W",
                            "L",
                            "W_PCT",
                            "MIN",
                            "FGM",
                            "FGA",
                            "FG_PCT",
                            "FGM",
                            "FGA",
                            "FG_PCT",
                            "FTM",
                            "FTA",
                            "FT_PCT",
                            "OREB",
                            "DREB",
                            "REB",
                            "AST",
                            "TOV",
                            "STL",
                            "BLK",
                            "BLKA",
                            "PF",
                            "PFD",
                            "PTS",
                            "PLUS_MINUS",
                            "NBA_FANTASY_PTS",
                            "DD",
                            "TD",
                            "GP_RANK",
                            "W_RANK",
                            "L_RANK",
                            "W_PCT_RANK",
                            "MIN_RANK",
                            "FGM_RANK",
                            "FGA_RANK",
                            "FG_PCT_RANK",
                            "FGM_RANK",
                            "FGA_RANK",
                            "FG_PCT_RANK",
                            "FTM_RANK",
                            "FTA_RANK",
                            "FT_PCT_RANK",
                            "OREB_RANK",
                            "DREB_RANK",
                            "REB_RANK",
                            "AST_RANK",
                            "TOV_RANK",
                            "STL_RANK",
                            "BLK_RANK",
                            "BLKA_RANK",
                            "PF_RANK",
                            "PFD_RANK",
                            "PTS_RANK",
                            "PLUS_MINUS_RANK",
                            "NBA_FANTASY_PTS_RANK",
                            "DD_RANK",
                            "TD_RANK",
                            "CFID",
                            "CFPARAMS"
                        ]

                        nba_df = pd.DataFrame(player_info, columns= columns_list)"""

    new_def = team_func(team, url)
    file = open('functions.txt', 'a')
    file.write()
    count = count +1