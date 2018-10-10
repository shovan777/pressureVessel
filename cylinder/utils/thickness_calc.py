"""Calculate inner thickness."""
from math import exp, atan, cos

def cylinder_t(P, S, R, CA, E=1.0):
    """Calculate thickness as per ASME DIV I

    Parameters
    ----------
    P : float
        Description of parameter `P`.
    S : type
        Description of parameter `S`.
    R : type
        Description of parameter `R`.
    CA : type
        Description of parameter `CA`.
    E : type
        Description of parameter `E`.

    Returns
    -------
    float
        Description of returned object.

    """
    # return (D/2) * (exp(P / (S * E)) - 1
    t_wo_allowance = (P * R) / (S * E - 0.6 * P)
    t_w_allowance = t_wo_allowance + CA
    return t_w_allowance

def conical_t(D, P, S, D_l, D_s, L_c, CA, E=1.0):
    D_l += 2 * CA
    D_s += 2 * CA
    alpha = atan(0.5 * (D_l - D_s) / L_c)
    t_wo_allowance = (P * D) / (2 * cos(alpha) * (S * E - 0.6 * P))
    return t_wo_allowance
