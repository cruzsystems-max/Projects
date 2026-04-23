import numpy as np
import plotly.graph_objects as go

def plot_3d(n=6):
    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2*np.pi, 100)

    theta, phi = np.meshgrid(theta, phi)

    r = np.abs(np.cos(theta)) ** n

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

    fig.update_layout(
        title="Patrón de Radiación 3D",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z"
        )
    )

    fig.show()