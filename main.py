from pathlib import Path
import sys

import geopandas as gpd


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    shp_name = "Kowloon_TSX_LOS_tem.shp"

    # 优先适配“data 与 code 并列”以及当前项目目录结构
    candidate_paths = [
        script_dir / "data" / "01_raw" / "shapefiles" / "kowloon_tsx_los_tem" / shp_name,
        script_dir / ".." / "data" / shp_name,
        script_dir.parent / "data" / shp_name,
    ]

    shp_path = next((p.resolve() for p in candidate_paths if p.exists()), None)
    if shp_path is None:
        print("=" * 60)
        print("[错误] 未找到 Shapefile 文件。")
        print("请确认文件路径是否正确，已尝试以下位置：")
        for p in candidate_paths:
            print(f"- {p.resolve()}")
        print("=" * 60)
        sys.exit(1)

    try:
        gdf = gpd.read_file(shp_path)
    except FileNotFoundError:
        print("=" * 60)
        print(f"[错误] 文件不存在：{shp_path}")
        print("请检查 data 目录及文件名是否正确。")
        print("=" * 60)
        sys.exit(1)
    except Exception as exc:
        print("=" * 60)
        print("[错误] 读取 Shapefile 失败。")
        print(f"原因：{exc}")
        print("=" * 60)
        sys.exit(1)

    print("=" * 60)
    print("1) 数据读取")
    print(f"文件路径: {shp_path}")
    print("=" * 60)

    print("=" * 60)
    print("2) 坐标系检查 (CRS)")
    print(gdf.crs)
    print("=" * 60)

    print("=" * 60)
    print("3) 字段探查")
    print("columns:")
    print(gdf.columns.tolist())
    print("-" * 60)
    print("head(10):")
    print(gdf.head(10))
    print("-" * 60)
    print(f"总行数（点位总数）: {len(gdf)}")
    print("=" * 60)

    print("=" * 60)
    print("4) 数值型字段统计摘要 describe()")
    numeric_summary = gdf.select_dtypes(include="number").describe()
    if numeric_summary.empty:
        print("未发现数值型列。")
    else:
        print(numeric_summary)
    print("=" * 60)


if __name__ == "__main__":
    main()
