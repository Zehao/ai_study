"""
Create an animated rotating 3D Earth using Matplotlib.

Run this script directly to open an interactive animation window.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm


# Configure a simple synthetic texture that roughly resembles land/sea patterns.
def _generate_texture(longitude, latitude):
    base = 0.35 * np.sin(3 * longitude) * np.cos(2 * latitude)
    ripples = 0.15 * np.sin(5 * longitude + latitude)
    bands = 0.2 * np.cos(latitude) * np.sin(longitude)
    texture = base + ripples + bands
    normalized = (texture - texture.min()) / (texture.max() - texture.min())
    return cm.terrain(normalized)


def _build_sphere(resolution=180):
    lon = np.linspace(-np.pi, np.pi, resolution)
    lat = np.linspace(-np.pi / 2, np.pi / 2, resolution // 2)
    lon_grid, lat_grid = np.meshgrid(lon, lat)

    x = np.cos(lat_grid) * np.cos(lon_grid)
    y = np.cos(lat_grid) * np.sin(lon_grid)
    z = np.sin(lat_grid)

    colors = _generate_texture(lon_grid, lat_grid)
    return x, y, z, colors


def animate_globe(frame, ax, sphere):
    x, y, z, colors = sphere
    ax.clear()
    ax.plot_surface(
        x,
        y,
        z,
        rstride=1,
        cstride=1,
        facecolors=colors,
        linewidth=0,
        antialiased=False,
        shade=True,
    )
    ax.set_box_aspect([1, 1, 1])
    ax.set_axis_off()
    ax.view_init(elev=20, azim=frame)
    return []


def main():
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")

    sphere = _build_sphere()

    animation.FuncAnimation(
        fig,
        animate_globe,
        fargs=(ax, sphere),
        frames=360,
        interval=50,
        blit=True,
        repeat=True,
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
