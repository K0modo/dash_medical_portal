import pandas as pd
import pathlib

PATH = pathlib.Path(__file__).parent

cat_col_member = ['mem_acct',
               'claim_item',
               'injury_disease',
               'specialty',
               'facility_class',
               'period'
               ]

data = pd.read_csv(PATH.joinpath('data_members.csv'), parse_dates=['charge_trans_date']).sort_values('mem_acct')
data['trans_date'] = data['charge_trans_date'].dt.date
for col in cat_col_member:
    data[col] = data[col].astype('category')
data_load = data.to_dict('records')
# print(data.info())

# # MEMBER DATA READ FUNCTIONS
# def read_in_member_data(file, cat_col_mem):
#     data = pd.read_csv(file, parse_dates=['charge_trans_date']).sort_values('mem_acct')
#     data['trans_date'] = data['charge_trans_date'].dt.date
#     for col in cat_col_mem:
#         data[col] = data[col].astype('category')
#     return data
#
#
# def load_member_data():
#     df_mem_dict = df_mem.to_dict('records')
#     return df_mem_dict
#
#
# # LOAD MEMBER DATA
# member_data = r'data_members.csv'
# cat_col_mem = ['mem_acct',
#                'claim_item',
#                'injury_disease',
#                'specialty',
#                'facility_class',
#                'period'
#                ]
# df_mem = read_in_member_data(member_data, cat_col_mem)