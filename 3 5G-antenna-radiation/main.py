import numpy as np
from antenna.patterns import radiation_pattern
from antenna.array_factor import array_factor
from visualization.plot2d import plot_2d
from visualization.plot3d import plot_3d_real


def main():
    theta = np.linspace(0, 2*np.pi, 500)

    # Patrón simple
    G = radiation_pattern(theta, n=8)
    plot_2d(theta, G, title="Patrón Direccional")

    # Array factor (5G-like)
    AF = array_factor(theta, N=8, d=0.5, beta=0)
    plot_2d(theta, AF, title="Array Factor (ULA)")

    # Visualización 3D (PRO)
    plot_3d_real()


if __name__ == "__main__":
    main()