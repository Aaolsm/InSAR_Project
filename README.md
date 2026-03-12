# InSAR Project

## 标准目录结构

```text
INSAR_PROJECT/
├── data/
│   ├── 01_raw/
│   │   ├── Building_Data_1.xlsx
│   │   └── shapefiles/
│   │       └── kowloon_tsx_los_tem/
│   │           ├── Kowloon_TSX_LOS_tem.shp
│   │           ├── Kowloon_TSX_LOS_tem.shx
│   │           ├── Kowloon_TSX_LOS_tem.dbf
│   │           └── Kowloon_TSX_LOS_tem.prj
│   └── 02_processed/
├── output/
│   ├── figures/
│   └── logs/
├── src/
│   ├── __init__.py
│   ├── data_clean.py
│   ├── spatial_analysis.py
│   └── visual_plot.py
├── main.py
├── requirements.txt
└── .gitignore
```

## 运行

```bash
pip install -r requirements.txt
python main.py
```

## 当前输入输出路径

- 原始数据: `data/01_raw/Building_Data_1.xlsx`
- 原始矢量: `data/01_raw/shapefiles/kowloon_tsx_los_tem/`
- 清洗结果: `data/02_processed/Cleaned_Building_Data.csv`
- 图件输出: `output/figures/`
