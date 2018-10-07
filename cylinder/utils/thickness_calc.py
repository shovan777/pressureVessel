"""Calculate inner thickness."""
from math import exp

def cylinder_t(D, P, S, R, E=1.0, CA):
    # return (D/2) * (exp(P / (S * E)) - 1
    t_wo_allowance = (P * R) / (S * E - 0.6 * P)
    t_w_allowance = t_wo_allowance + CA
    return t_w_allowance

# def conical_t()
