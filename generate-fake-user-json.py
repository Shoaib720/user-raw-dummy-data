import pandas as pd

raw_df = pd.read_excel('./user_raw_data.xlsx')

raw_df_dropped_cols = raw_df[['id','email','address','city','country']]

print(raw_df_dropped_cols.to_json(orient='records'))