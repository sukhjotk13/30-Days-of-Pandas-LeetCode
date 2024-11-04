import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result=courses.groupby('class')['student'].count()
    result=result.reset_index()
    result1=result[result['student']>=5]
    return result1[['class']]
