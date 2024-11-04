import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    m1=pd.merge(students,subjects,how='cross')
    grouped=examinations.value_counts().reset_index()
    grouped.rename(columns={'count':'attended_exams'},inplace=True)
    m=pd.merge(m1,grouped,how='left',on=['student_id','subject_name'])
    m['attended_exams'].fillna(0,inplace=True)
    m.sort_values(by=['student_id','subject_name'],inplace=True)
    return m
