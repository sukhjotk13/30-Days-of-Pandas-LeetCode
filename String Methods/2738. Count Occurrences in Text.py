import pandas as pd
import re

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    pattern1=r'\sbull\s'
    pattern2=r'\sbear\s'
    df1=files[files['content'].str.contains(pattern1,regex=True)]
    df2=files[files['content'].str.contains(pattern2,regex=True)]
    bull_count=df1['content'].count()
    bear_count=df2['content'].count()
    return pd.DataFrame({
        'word': ['bull', 'bear'],
        'count': [bull_count, bear_count]})
