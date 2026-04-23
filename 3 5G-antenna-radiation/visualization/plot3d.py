import numpy as np
import plotly.graph_objects as go

def ura_array_factor(theta, phi, M=8, N=8, dx=0.5, dy=0.5, theta0=0, phi0=0):
    k = 2 * np.pi

    # Fases para steering
    beta_x = -k * dx * np.sin(theta0) * np.cos(phi0)
    beta_y = -k * dy * np.sin(theta0) * np.sin(phi0)

    AF = np.zeros(theta.shape, dtype=complex)

    for m in range(M):
        for n in range(N):
            phase = (
                m * k * dx * np.sin(theta) * np.cos(phi) +
                n * k * dy * np.sin(theta) * np.sin(phi) +
                m * beta_x +
                n * beta_y
            )
            AF += np.exp(1j * phase)

    return np.abs(AF) / (M * N)


def element_pattern(theta):
    # Aproximación de patch antenna (más realista que cos^n)
    return np.cos(theta)**2


def total_pattern(theta, phi):
    AF = ura_array_factor(theta, phi, M=8, N=8, theta0=np.pi/6, phi0=np.pi/4)
    E = element_pattern(theta)
    return AF * E


def plot_3d_real():
    theta = np.linspace(0, np.pi, 120)
    phi = np.linspace(0, 2*np.pi, 120)

    theta, phi = np.meshgrid(theta, phi)

    R = total_pattern(theta, phi)

    # Conversión a cartesianas
    x = R * np.sin(theta) * np.cos(phi)
    y = R * np.sin(theta) * np.sin(phi)
    z = R * np.cos(theta)

    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

    fig.update_layout(
        title="Patrón de Radiación 3D - URA Beamforming 5G",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z"
        )
    )

    fig.show()


if __name__ == "__main__":
    plot_3d_real()