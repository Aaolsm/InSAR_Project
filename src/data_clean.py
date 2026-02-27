from pathlib import Path

import pandas as pd


RAW_XLSX_PATH = Path("data/01_raw/Building_Data_1.xlsx")
PROCESSED_CSV_PATH = Path("data/02_processed/Cleaned_Building_Data.csv")


def clean_building_data(
    input_path: Path = RAW_XLSX_PATH,
    output_path: Path = PROCESSED_CSV_PATH,
) -> pd.DataFrame:
    """Load raw data, compute density, drop invalid rows, and save cleaned CSV."""
    df = pd.read_excel(input_path)

    df["Density"] = df["NUMPOINTS"] / df["Area_sqm"]
    df_clean = df[(df["height_max"] > 0) & (df["NUMPOINTS"] > 0)].copy()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(output_path, index=False, encoding="utf-8-sig")

    return df_clean
