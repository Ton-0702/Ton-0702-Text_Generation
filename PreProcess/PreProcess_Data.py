import pandas as pd
import numpy as np

df = pd.read_excel(r'F:\Hoc_online\HK5\Xử lý ngôn ngữ tự nhiên\tomtatvanban_chinh.xlsx')


for i in df['content'].index:
    if df['content'][i].find['\n']:
        print(i)