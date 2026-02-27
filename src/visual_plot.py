from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


FIGURES_DIR = Path("output/figures")


def save_density_plots(df_clean: pd.DataFrame, output_dir: Path = FIGURES_DIR) -> None:
    """Generate and save scatter/regression and box plots."""
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.rcParams["font.sans-serif"] = ["WenQuanYi Zen Hei", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False

    plt.figure(figsize=(10, 6))
    sns.regplot(data=df_clean, x="height_max", y="Density")
    plt.title("Height vs Point Density")
    plt.xlabel("h_max")
    plt.ylabel("p_density")
    plt.savefig(output_dir / "H vs P_Density.png", dpi=300, bbox_inches="tight")
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_clean, x="building", y="Density", hue="building", palette="Set2")
    plt.title("建筑类型点云密度分布")
    plt.xlabel("Building Type")
    plt.ylabel("Point Density")
    plt.savefig(output_dir / "Density_by_Building_Type.png", dpi=300, bbox_inches="tight")
    plt.close()
