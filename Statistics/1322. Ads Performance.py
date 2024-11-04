import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    result= ads.groupby(['ad_id','action'])['user_id'].count()
    result=result.reset_index()
    ids=ads['ad_id'].unique()
    ads['ctr']=0.0
    for id in ids:
        filt_clicked= (result['ad_id']==id) & (result['action']=='Clicked')
        filt_viewed= (result['ad_id']==id) & (result['action']=='Viewed')
        clicked= result[filt_clicked]['user_id'].sum()
        viewed=result[filt_viewed]['user_id'].sum()
        if clicked+viewed ==0:
            ctr=0
        else:
            ctr=100.0*clicked/(clicked+viewed)
        ads.loc[ads['ad_id']==id,'ctr']=round(ctr,2)
    ads.drop_duplicates(subset=['ad_id', 'ctr'], inplace=True)
    ads.sort_values(by=['ctr','ad_id'],ascending=[False,True],inplace=True)
    return ads[['ad_id','ctr']]
    
