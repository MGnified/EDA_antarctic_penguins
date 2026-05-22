import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler


def plt_plot_style():
    """Sets up a global dark theme and custom colour palette"""
    # defining custom colour palette
    colours = [
        "#4F9768",
        "#7624E0",
        "#C23570",
        "#BE524B",
        "#447ACB",
        "#C19138",
        "#FFFFFF",
    ]

    # applying dark theme
    plt.style.use("dark_background")

    # updating rcParams for global consistency
    plt.rcParams.update(
        {
            # colour cycle
            "axes.prop_cycle": cycler(color=colours),
            # grid and axes
            "axes.grid": True,
            "grid.color": "#9B9B9B",
            "grid.linestyle": "--",
            "grid.alpha": 0.5,
            "axes.edgecolor": "#ffffff",
            # Fonts
            "font.family": "Fira Code",
            "font.size": 12,
            "axes.titlesize": 18,
            "axes.labelsize": 14,
            # figuresize
            "figure.figsize": (10, 6),
        }
    )


# setting up a style function for my seaborn plots
def sns_plot_style(style="dark_background", palette="crest", size=(12, 7)):
    
    """Sets up the style for every seaborn plot in the File."""

    # setting dark background
    plt.style.use(style)

    # setting a global color palette
    sns.set_palette(palette)

    # setting up standard size
    plt.rc("figure", figsize=size)

    # setting up a grid for visibility
    plt.rc("grid", color="#cccccc", linewidth=0.8, linestyle="--", alpha=0.3)

    # setting up standard font-size
    plt.rc("font", family="Fira Code", size=12)
    plt.rc("axes", titlesize=18, labelsize=14)
    plt.rc("xtick", labelsize=12)
    plt.rc("ytick", labelsize=12)
    plt.rc("legend", fontsize=12)
