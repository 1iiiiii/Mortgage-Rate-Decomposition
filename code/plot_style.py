"""Shared matplotlib style. Import once at the top of every figure script:

    from plot_style import apply_style, COLORS, source_note

Figures carry a title, axis labels with units and a source line only.
No explanatory prose inside figures; a time axis shows actual dates.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

# Site tokens, copied from Personal Website/theme.scss so figures sit on the page background
SITE = {
    "paper": "#fffdf9",      # $paper: page background
    "ink": "#16130f",        # $ink: titles
    "muted": "#6e6559",      # $muted: axis labels, ticks
    "faint": "#857b6c",      # $faint: source line, reference lines
    "rule": "#e6dfd2",       # $rule: gridlines
    "axis": "#b5ab9b",       # $fainter: axis spines
}

COLORS = {
    "total": SITE["ink"],    # the series being decomposed
    "part1": "#2f5d7c",      # slate blue: first component
    "part2": "#d19a3a",      # ochre: second component
    "accent": "#a8442a",     # site $accent (rust): highlighted series or period
    "grey": SITE["faint"],
}

# Fig 2 pieces, fixed order (adjacent pairs checked for colorblind separation:
# OKLab dE >= 9 under protan/deutan/tritan simulation, >= 15 for normal vision)
PIECES = {
    "exp_real_path": "#2f5d7c",   # slate blue
    "exp_infl": "#a8442a",        # rust (site accent)
    "real_rp": "#5e8c6a",         # sage
    "infl_rp": "#d19a3a",         # ochre
    "resid": "#cfc7b8",           # warm grey: unexplained
    "spread": "#8e5a7a",          # plum
}


def apply_style():
    mpl.rcParams.update({
        "figure.facecolor": SITE["paper"],
        "axes.facecolor": SITE["paper"],
        "savefig.facecolor": SITE["paper"],
        "text.color": SITE["ink"],
        "axes.titlecolor": SITE["ink"],
        "axes.labelcolor": SITE["muted"],
        "axes.edgecolor": SITE["axis"],
        "xtick.color": SITE["muted"],
        "ytick.color": SITE["muted"],
        "legend.labelcolor": SITE["muted"],
        "figure.figsize": (9, 5),
        "figure.dpi": 110,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "font.size": 12,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 12,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": SITE["rule"],
        "grid.linewidth": 0.8,
        "legend.frameon": False,
        "legend.fontsize": 11,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "lines.linewidth": 1.8,
    })


def source_note(fig, text, y=-0.02):
    """Source line in the bottom-left corner, outside the axes.
    Lower y (more negative) when a legend sits below the axes."""
    fig.text(0.01, y, f"Source: {text}", ha="left", va="top",
             fontsize=9, color=COLORS["grey"])
