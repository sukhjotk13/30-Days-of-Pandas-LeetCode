import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    grouped=employee.groupby('managerId')['id'].count().reset_index()
    g=grouped[grouped['id']>=5]
    m=pd.merge(g,employee,how='inner',left_on='managerId',right_on='id')
    return m[['name']]
