import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped=actor_director.groupby(['actor_id','director_id'])['timestamp'].count()
    grouped=grouped.reset_index()
    filt=grouped['timestamp']>=3
    result=grouped[filt]
    return result[['actor_id','director_id']]
