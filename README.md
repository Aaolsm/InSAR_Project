# InSAR Project

## 标准目录结构

```text
INSAR_PROJECT/
├── data/
│   ├── 01_raw/
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
- 清洗结果: `data/02_processed/Cleaned_Building_Data.csv`
- 图件输出: `output/figures/`
