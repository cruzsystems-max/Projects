import numpy as np

def array_factor(theta, N=8, d=0.5, beta=0):
    """
    Array Factor para un arreglo lineal uniforme (ULA)
    
    theta: ángulo
    N: número de elementos
    d: espaciamiento (lambda)
    beta: fase progresiva (beam steering)
    """
    k = 2 * np.pi  # número de onda (normalizado)

    AF = np.zeros_like(theta, dtype=complex)

    for n in range(N):
        AF += np.exp(1j * (n * k * d * np.cos(theta) + n * beta))

    return np.abs(AF)