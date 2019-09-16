import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()

# 创建mysql连接引擎
engine = create_engine(
    'mysql+mysqldb://root:123456@39.108.134.38:3306/provider?charset=utf8'
)

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',20)

df = pd.read_sql('select * from phones', engine, index_col='id')
# print(df)
# print(df.describe())
# print(df.head()[['title','brand']])
# print(df.iloc[0])
print(df.loc[0:2, 'title'])
print(df.loc[0:2, :])


# 重置索引列为brand
# df = pd.read_sql('select * from phones', engine, index_col='brand')
# print(df[['title']].loc['华为'])



# # 查询数据并转为pandas.DataFrame，指定DataFrame的index为数据库中的id字段
# df = pd.read_sql('SELECT * FROM students', engine, index_col='id')
# print(df)
# # 修改DataFrame中的数据（移除age列）
# dft = df.drop(['age'], axis=1)
# # 将修改后的数据追加至原表,index=False代表不插入索引，因为数据库中id字段为自增字段
# dft.to_sql('students', engine, index=False, if_exists='append')
