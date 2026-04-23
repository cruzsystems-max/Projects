import numpy as np

def radiation_pattern(theta, n=8):
    """
    Patrón simple direccional tipo cos^n(theta)
    """
    return np.abs(np.cos(theta)) ** n