import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    regex1=r"\sDIAB1[a-zA-Z0-9]*"
    regex2=r"^DIAB1[a-zA-Z0-9]*"
    return patients[(patients['conditions'].str.contains(regex1)) |
     (patients['conditions'].str.contains(regex2))]
