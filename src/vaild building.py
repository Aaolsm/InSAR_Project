import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import font_manager

plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.unicode_minus'] = False   #坐标轴负号


file_path = 'data/Building_Data_1.xlsx'
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
# 2.绘图
plt.figure(figsize=(10,6))
sns.regplot(data=df_clean, x='height_max', y='Density')
plt.title('Height vs Point_Density')
plt.xlabel('h_max')
plt.ylabel('p_density')
#plt.show()

# ==========================================
# 3.建筑类型处理与箱线图

print('建筑类型统计')
print(df_clean['building'].value_counts())

plt.savefig('output/H vs P_Density.png', dpi=300, bbox_inches='tight')
print("图片已保存->output")

# 4.箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_clean, x="building", y="Density", hue="building", palette="Set2")
plt.title("建筑类型点云密度分布")
plt.xlabel("Building Type")
plt.ylabel('Point Density')
plt.savefig('output/Density_by_Building_Type.png', dpi=300, bbox_inches='tight')
print(" 第二张图：箱线图已保存-> output 文件夹")


# 5.导出清洗后的数据供 QGIS 空间分析
print("/n  清洗后包含字段")
print(df_clean.columns.tolist())
output_csv_path = 'output/Cleaned_Building_Data.csv'
df_clean.to_csv(output_csv_path, index= False, encoding='utf-8-sig')
print(f'已导出 -> {output_csv_path}')
