from math import cos, sin, pow, pi


def error_check(ratio, calc_param, msg):
    if (ratio >= 1):
        return('error',ratio, msg)

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
    tau_allowable,
    x_1,
    x_2
):
    '''Perform all calculations for lifting lug 
        as per calcgen report 18-001-Calculations.pdf

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
        sigma_b {float} -- allowable stress, Bending in psi
        tau_allowable {float} -- allowable stress, weld shear in psi
        x_1 {float} -- distance between this lug and the center of gravity
        x_2 {float} -- distance between second lift lug and the center of gravity
    '''

    # calculate lift forces
    # force on vessel at lug, F_r
    F_r = (W/cos(phi)) * (1-x_1 / (x_1 + x_2))

    # calculate lug pin diameter -shear stress
    # lug pin diamter, d_reqd
    d_reqd = pow(2*F_r/(pi*sigma_s), 0.5)
    diameter_ratio = d_reqd/D_p
    error_check(diameter_ratio, d_reqd, 'Lug pin diameter is not acceptable')
    # calculate shear stress
    sigma_s_calc = F_r/(2*(0.25*pi*pow(D_p, 2)))
    sigma_s_ratio = sigma_s_calc/sigma_s
    error_check(sigma_s_ratio, sigma_s_calc, 'shear stress is not acceptable')

    # calculate lug thickness - tensile stress
    # required lug thickness, t_reqd
    t_reqd = F_r/((L-d)*sigma_t)
    thickness_ratio = t_reqd / t
    error_check(thickness_ratio, t_reqd, 'thickness is not acceptable due to tensile stress')
    # calculate tensile stress
    sigma_t_calc = F_r / ((L-d)*t)
    sigma_t_ratio = sigma_t / sigma_t_calc
    error_check(sigma_t_ratio, sigma_t_calc, 'tensile stress is not acceptable')

    # calculate lug thickness - bearing stress
    # required lug thickness
    t_reqd = F_r/(D_p*sigma_p)
    thickness_ratio = t_reqd / t
    error_check(thickness_ratio, t_reqd, 'thickness is not acceptable due to bearing stress')
    #  calculate bearing stress
    A_bearing = (D_p * (t))
    sigma_b_calc = F_r / A_bearing
    sigma_b_ratio = sigma_b / sigma_b_calc
    error_check(sigma_b_ratio, sigma_b_calc, 'bearing stress is not acceptable')
    
    # calculate shear stress length
    phi_shear = 55*D_p/d
    L_shear = (H - a_2 - 0.5*d) + 0.5 * D_p * (1-cos(phi))

    # calculate lug thickness - shear stress
    # required lug thickness
    t_reqd = (F_r/sigma_s) / (2*L_shear)
    thickness_ratio = t_reqd/t
    error_check(thickness_ratio, t_reqd, 'thickness is not acceptable due to shear stress')
    A_shear = 2*t*L_shear
    tau = F_r/A_shear
    sigma_s_ratio = tau/sigma_s
    error_check(sigma_s_ratio, tau, 'shear stress is not acceptable')

    # calculate lug plate stress
    # dont understand the formula M_bend and Z_bend
    # how to get those quantities

    # calculate weld stress
    A_weld = 2*0.707*t_w*(L+t)
    alpha = 0.0
    tau_t = F_r * cos(alpha) / A_weld
    tau_s = F_r * sin(alpha) / A_weld
    M = 3.0#how to calculate M
    Hght = 3.0 #how to calculate hght
    c = F_r*sin(alpha)*Hght - F_r*cos(alpha)*a_1
    h = 1.0#how to calculate h what is h?
    l = 0.707*h*L*(3*t+L)
    tau_b = M * abs(c)/l

    tau_ratio = pow(pow(tau_t + tau_b, 2) + pow(tau_s, 2),2) / tau_allowable


