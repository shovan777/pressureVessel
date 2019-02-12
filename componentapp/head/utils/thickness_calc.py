"""Calculate inner thickness."""
from math import exp, atan, cos

def head_t(P, S, D, C_A, E=1.0):
    """Calculate thickness as per ASME DIV I

    Parameters
    ----------
    P : float
        Design Pressure or max. allowable working pressure psi.
    S : int
        Stress value of material psi.
    D : inch float
        Inside diameter .
    CA : float
        Corrosion Allowance.
    E : float max 1 
        Joint efficiency.

    Returns
    -------
    float
        thickness.

    """
    upper_part = float(P * D)
    lower_part = float( (2 * S * E) - (0.2 * P) )
    return (upper_part/lower_part) + float(C_A)

def conical_t(D, P, S, D_l, D_s, L_c, CA, E=1.0):
    D_l += 2 * CA
    D_s += 2 * CA
    alpha = atan(0.5 * (D_l - D_s) / L_c)
    t_wo_allowance = (P * D) / (2 * cos(alpha) * (S * E * 1000 - 0.6 * P))
    return t_wo_allowance
