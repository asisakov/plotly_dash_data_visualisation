import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect('./data/wine_data.sqlite')
c = conn.cursor()

df = pd.read_csv('./data/claims_test.csv')

row_count = df.shape[0]


# top_df = pd.read_sql("select variety, count(variety) as counts, avg(price) as avgPrice, avg(rating) as avgRating from wine_data group by variety order by counts desc limit 8", conn)
# top_df = top_df.round(2)

top_df_prep = df.groupby('MONTH').agg({'MONTH': np.size, 'PAID_AMOUNT': np.mean})
top_df_prep.rename(columns={'MONTH':'NUMBER_OF_TRANSACTIONS', 'PAID_AMOUNT' : 'AVG_PAID_AMOUNT'}, inplace=True)
top_df_prep = top_df_prep.reset_index(level=0)
top_df = top_df_prep.head(10)
top_df = top_df.round(2)

# bottom_df = pd.read_sql("select variety, count(variety) as counts, avg(price) as avgPrice, avg(rating) as avgRating from wine_data group by variety order by counts asc limit 8", conn)
# bottom_df = bottom_df.round(2)

bottom_df = top_df_prep.tail(10)
bottom_df = bottom_df.round(2)

percent = pd.DataFrame()
percent['MONTH'] = top_df_prep['MONTH']
percent['contribution'] =  top_df_prep['NUMBER_OF_TRANSACTIONS'] * top_df_prep['AVG_PAID_AMOUNT'] / sum(top_df_prep['NUMBER_OF_TRANSACTIONS'] * top_df_prep['AVG_PAID_AMOUNT']) * 100
percent['remainder'] = 100 - percent['contribution']

variety = top_df_prep['MONTH']
