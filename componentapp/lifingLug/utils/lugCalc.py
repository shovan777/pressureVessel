from math import cos, pow

def lug_calc(
    L,
    H,
    t,
    d,
    D_p,
    a_1,
    a_2,
    beta,
    phi,
    t_w,
    W,
    sigma_t,
    sigma_s,
    sigma_p,
    sigma_b,
    x_1,
    x_2
):
    '''[summary]

    Arguments:
        L {float} -- length in inches
        H {float} -- height in inches
        t {float} -- thickness in inches
        d {float} -- hole diameter in inches
        D_p {float} -- pin diameter in inches
        a_1 {float} -- load eccentricity in inches
        a_2 {float} -- distance from load to shell or pad in inches
        beta {float} -- load angle normal to vessel in degree
        phi {float} -- load angle from vertical in degree
        t_w {float} -- size in inches
        sigma_t {float} -- allowable stress, Tensile in psi
        sigma_s {float} -- allowable stress, Shear in psi
        sigma_p {float} -- allowable stress, Bearing in psi
        sigma_t {float} -- allowable stress, Bending in psi
        x_1 {float} -- distance between this lug and the center of gravity
        x_2 {float} -- distance between second lift lug and the center of gravity
    '''

    # calculating lift forces
    # force on vessel at lug, F_r
    F_r = (W/cos(phi)) * (1-x_1 / (x_1 + x_2))

    # calculating lug pin diameter -shear stress
    # lug pin diamter, d_reqd
    d_reqd = pow(2*F_r/)