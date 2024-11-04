import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby('email')['id'].transform('min')
    
    # Keep rows where the id is the smallest id for that email
    person.drop(person[person['id'] > min_id].index, inplace=True)
