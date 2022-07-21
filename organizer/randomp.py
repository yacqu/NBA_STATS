import json
import os


ATL_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\ATL_dic.txt", "r").read())
BKN_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\BKN_dic.txt", "r").read())
BOS_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\BOS_dic.txt", "r").read())
CHA_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\CHA_dic.txt", "r").read())
CHI_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\CHI_dic.txt", "r").read())
CLE_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\CLE_dic.txt", "r").read())
DAL_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\DAL_dic.txt", "r").read())
DEN_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\DEN_dic.txt", "r").read())
DET_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\DET_dic.txt", "r").read())
GSW_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\GSW_dic.txt", "r").read())
HOU_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\HOU_dic.txt", "r").read())
IND_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\IND_dic.txt", "r").read())
LAC_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\LAC_dic.txt", "r").read())
LAL_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\LAL_dic.txt", "r").read())
MEM_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\MEM_dic.txt", "r").read())
MIA_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\MIA_dic.txt", "r").read())
MIL_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\MIL_dic.txt", "r").read())
MIN_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\MIN_dic.txt", "r").read())
NOP_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\NOP_dic.txt", "r").read())
NYK_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\NYK_dic.txt", "r").read())
OKC_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\OKC_dic.txt", "r").read())
ORL_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\ORL_dic.txt", "r").read())
PHI_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\PHI_dic.txt", "r").read())
PHX_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\PHX_dic.txt", "r").read())
POR_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\POR_dic.txt", "r").read())
SAC_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\SAC_dic.txt", "r").read())
SAS_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\SAS_dic.txt", "r").read())
TOR_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\TOR_dic.txt", "r").read())
UTA_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\UTA_dic.txt", "r").read())
WAS_url_dictionary= json.loads(open(r"C:\python scripts\tryingnewsyntax\dics\WAS_dic.txt", "r").read())

dics = [
ATL_url_dictionary,
BKN_url_dictionary,
BOS_url_dictionary,
CHA_url_dictionary,
CHI_url_dictionary,
CLE_url_dictionary,
DAL_url_dictionary,
DEN_url_dictionary,
DET_url_dictionary,
GSW_url_dictionary,
HOU_url_dictionary,
IND_url_dictionary,
LAC_url_dictionary,
LAL_url_dictionary,
MEM_url_dictionary,
MIA_url_dictionary,
MIL_url_dictionary,
MIN_url_dictionary,
NOP_url_dictionary,
NYK_url_dictionary,
OKC_url_dictionary,
ORL_url_dictionary,
PHI_url_dictionary,
PHX_url_dictionary,
POR_url_dictionary,
SAC_url_dictionary,
SAS_url_dictionary,
TOR_url_dictionary,
UTA_url_dictionary,
WAS_url_dictionary]


team_list = ('ATL',
'BKN',
'BOS',
'CHA',
'CHI',
'CLE',
'DAL',
'DEN',
'DET',
'GSW',
'HOU',
'IND',
'LAC',
'LAL',
'MEM',
'MIA',
'MIL',
'MIN',
'NOP',
'NYK',
'OKC',
'ORL',
'PHI',
'PHX',
'POR',
'SAC',
'SAS',
'TOR',
'UTA',
'WAS')

for j in range(0, 30):

    home_team = team_list[j].strip("''")

    class_def_file = open("functions_%s.txt" % (home_team), "w")
    class_def_file.close()
    print('j')

    for i in range(0,30):
        
        dictionary_in_use = dics[j]
        team_quotes = team_list[i]

        away_team_url = dictionary_in_use[team_quotes]
        print("i")
        team = team_quotes.strip("''")

        team_func = """ def %s():
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

                     
                            nba_df = pd.DataFrame(player_info, columns= columns_list)""" % (team, away_team_url)
        

        
        
        team_def_file = open("functions_%s.txt" % (home_team), "a")
        team_def_file.write(team_func)
        team_def_file.write('\n')
        team_def_file.close


