import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result=activity.groupby('player_id')['event_date'].min()
    result=result.reset_index()
    result.rename(columns={'event_date':'first_login'},inplace=True)
    return result[['player_id','first_login']]
