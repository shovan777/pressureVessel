"""Calculate nozzle params."""

def calculate_t_c(cylinder_t, nozzle_t, C_A):
    """Find minimum weild throat dimension.

    Parameters
    ----------
    cylinder_t : float
        internal thickness of cylinder
        unit: in
    nozzle_t : float
        nozzle thickness
        unit: in
    C_A : float
        corrosion allowance

    Returns
    -------
    float
        minimul fillet weld throat dimension
        unit: in

    """

    t_n = nozzle_t - C_A
    t = cylinder_t - C_A
    t_min = min(t_n, nozzle_t, 0.75)
    t_c = min(0.7*t_min, 0.25)
    return t_c/0.7

def calculate_t_min(D,tn,S,E,P,C_A):
    # minimium nozzle thickness based on stress
    R = float((D-2*tn)/2)
    upper_part = float(P * R)
    lower_part = float((S * 1000 * E) - (0.6 * P))
    return (upper_part/lower_part) + C_A

def calclate_r_1(nozzle_t,C_A):
    """Find inner radius"""
    t = nozzle_t - C_A
    return min(0.25*t, 1/8)
