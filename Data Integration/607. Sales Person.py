import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    m1=pd.merge(orders,company,how='inner',on='com_id')
    m2=pd.merge(sales_person,m1,how='left',on='sales_id',suffixes=('_p','_c'))
    filt=(m2['name_c']=='RED')
    new=(m2[filt]['sales_id']).to_list()
    new1=m2[~m2['sales_id'].isin(new)]
    new1.rename(columns={'name_p':'name'},inplace=True)
    return new1[['name']].drop_duplicates()
