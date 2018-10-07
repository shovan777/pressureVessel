"""Calculate inner thickness."""
from math import exp

def cylinder_t(D, P, S, E=1.0):
    return (D/2) * (exp(P / (S * E)) - 1)
