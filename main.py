from src.data_clean import clean_building_data
from src.spatial_analysis import summarize_density_by_building
from src.visual_plot import save_density_plots


def main() -> None:
    df_clean = clean_building_data()
    summary = summarize_density_by_building(df_clean)
    save_density_plots(df_clean)

    print(f"清洗前后字段: {list(df_clean.columns)}")
    print("建筑类型统计:")
    print(df_clean["building"].value_counts(dropna=False))
    print("建筑类型密度汇总:")
    print(summary)
    print("输出完成: data/02_processed + output/figures")


if __name__ == "__main__":
    main()
