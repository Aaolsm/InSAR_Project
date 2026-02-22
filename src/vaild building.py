import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = 'E:/Graduation project/QGIS-relat/Kowloon_TSX_LOS_tem/InSAR_Project/data/Building_Data_1.xlsx'
df = pd.read_excel(file_path)
print(df.columns)
#点密度
df['Density'] = df['NUMPOINTS'] / df['Area_sqm']
#过滤异常
df_clean = df[(df['height_max'] > 0) & (df['NUMPOINTS'] > 0)].copy()
#检查过滤
print('清洗前楼数量',len(df))
print('清洗后楼数量',len(df_clean))

print(df_clean[['height_max','Density']].describe())

# ======================================================
# 绘图
plt.figure(figsize=(10,6))
sns.regplot(data=df_clean, x='height_max', y='Density')
plt.title('Height vs Point_Density')
plt.xlabel('h_max')
plt.ylabel('p_density')
plt.show()

# ==========================================
# Level 4: 建筑类型处理与箱线图
# ==========================================
print('建筑类型统计')
print(df_clean['building'].value_counts())
