#!/usr/bin/env python3
"""Render a reconstructed particle from its voxel point file (Python 3).

    python3 render_particle.py p01.txt images/p01_reconstruction.png

Each line of the point file is "(x, y, z)" in micrometres, one occupied voxel
per line, as written by analysis1.py. Needs numpy and matplotlib; unlike the
original 2visualize.py it does not need Mayavi or a display.
"""
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

GRID = 6.1  # voxel edge in micrometres (the scan's step size)


def main(src="p01.txt", out="images/p01_reconstruction.png"):
    with open(src) as fh:
        pts = np.array([[float(v) for v in re.findall(r"[-\d.]+", line)]
                        for line in fh if line.startswith("(")])
    volume = len(pts) * GRID ** 3
    diameter = (6 * volume / np.pi) ** (1 / 3)
    print(f"{len(pts)} voxels, volume {volume:.3e} um^3, "
          f"equivalent sphere diameter {diameter:.0f} um")

    fig = plt.figure(figsize=(11, 5), dpi=160)
    for i, (elev, azim) in enumerate([(22, -60), (22, 35)]):
        ax = fig.add_subplot(1, 2, i + 1, projection="3d")
        ax.scatter(*pts.T, c=pts[:, 2], cmap="viridis", s=3, marker="s", linewidths=0)
        ax.set_box_aspect(np.ptp(pts, axis=0))
        ax.view_init(elev, azim)
        ax.set_xlabel("x (µm)"); ax.set_ylabel("y (µm)"); ax.set_zlabel("z (µm)")
    fig.suptitle(f"Sand particle {src.rsplit('.', 1)[0]}: {len(pts):,} voxels at "
                 f"{GRID} µm (colour = slice height z)", fontsize=11)
    fig.tight_layout()
    fig.savefig(out)


if __name__ == "__main__":
    main(*sys.argv[1:3])
