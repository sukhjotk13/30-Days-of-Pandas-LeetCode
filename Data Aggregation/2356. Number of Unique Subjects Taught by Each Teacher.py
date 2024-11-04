import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result=teacher.groupby('teacher_id')['subject_id'].nunique()
    result=result.reset_index()
    result.rename(columns={'subject_id':'cnt'},inplace=True)
    return result[['teacher_id','cnt']]
