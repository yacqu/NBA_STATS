
nba_df = {}

def ppg(player_name, nba_df):

    nba_df.set_index('PLAYER_NAME', inplace=True)

    points_per_game = nba_df.loc[player_name]['PTS']

    return points_per_game