"""Calculate parameters for lifting lug."""
from math import cos, sin, pow as p, pi
from reporter.models import Report
from state.models import LiftingLugState
from componentapp.component.models import Component

from exceptionapp.exceptions import newError

# def error_check(ratio, calc_param, msg):
#     if (ratio >= 1):
#         return('unacceptable', calc_param, msg)
#     else:
#         return('acceptable', calc_param, msg)


def error_check(ratio):
    if(ratio >= 1):
        return False
    else:
        return True


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
    x_2,
    report_id,
    component_react_id
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
        t_w {float} -- weld size in inches
        W {float} -- weight of the vessel
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

    F_r = (W/cos(phi * pi / 180)) * (1 - x_1 / (x_1 + x_2))

    # calculate lug pin diameter -shear stress
    # lug pin diamter, d_reqd
    d_reqd = p(2*F_r/(pi*sigma_s), 0.5)
    diameter_ratio = d_reqd/D_p
    # error_check(diameter_ratio, d_reqd, 'Lug pin diameter is not acceptable')
    # calculate shear stress
    sigma_sd_calc = F_r/(2*(0.25*pi*p(D_p, 2)))
    sigma_sd_ratio = sigma_sd_calc/sigma_s
    # error_check(sigma_sd_ratio, sigma_sd_calc,
    #             'shear stress is not acceptable')

    # calculate lug thickness - tensile stress
    # required lug thickness, t_reqd

    t_reqd_tensile = F_r/((L-d)*sigma_t)
    # thickness_ratio = t_reqd / t
    t_max = t_reqd_tensile
    # error_check(thickness_ratio, t_reqd,
    #             'thickness is not acceptable due to tensile stress')

    # calculate tensile stress
    sigma_t_calc = F_r / ((L-d)*t)
    sigma_t_ratio = sigma_t_calc / sigma_t

    # error_check(sigma_t_ratio, sigma_t_calc,
    #             'tensile stress is not acceptable')

    # calculate lug thickness - bearing stress
    # required lug thickness
    t_reqd_bearing = F_r/(D_p*sigma_p)
    if t_reqd_bearing > t_max:
        t_max = t_reqd_bearing
    # thickness_ratio = t_reqd / t
    # error_check(thickness_ratio, t_reqd,
    #             'thickness is not acceptable due to bearing stress')
    #  calculate bearing stress
    A_bearing = (D_p * (t))
    sigma_b_calc = F_r / A_bearing
    sigma_b_ratio = sigma_b_calc / sigma_b
    # error_check(sigma_b_ratio, sigma_b_calc,
    #             'bearing stress is not acceptable')

    # calculate shear stress length
    phi_shear = 55*D_p/d
    # print('***********')]
    # print(H, a2, d, Dp, )
    L_shear = (H - a_2 - 0.5*d) + 0.5 * D_p * (1-cos(phi_shear * pi / 180))

    # calculate lug thickness - shear stress
    # required lug thickness
    t_reqd_shear = (F_r/sigma_s) / (2*L_shear)
    if t_reqd_shear > t_max:
        t_max = t_reqd_shear
    thickness_ratio = t_max / t
    # thickness_ratio = t_reqd/t
    # error_check(thickness_ratio, t_reqd,
    #             'thickness is not acceptable due to shear stress')
    A_shear = 2*t*L_shear
    tau = F_r/A_shear
    sigma_s_ratio = tau/sigma_s
    # error_check(sigma_s_ratio, tau, 'shear stress is not acceptable')

    # calculate lug plate stress
    # dont understand the formula M_bend and Z_bend
    # how to get those quantities

    # calculate weld stress
    A_weld = 2*0.707*t_w*(L+t)
    alpha = 0.0
    tau_t = F_r * cos(alpha * pi / 180) / A_weld
    tau_s = F_r * sin(alpha * pi / 180) / A_weld
    M = 3.0  # how to calculate M
    Hght = 3.0  # how to calculate hght
    c = F_r*sin(alpha * pi / 180)*Hght - F_r*cos(alpha * pi / 180)*a_1
    h = 1.0  # how to calculate h what is h?
    l = 0.707*h*L*(3*t+L)
    tau_b = M * abs(c)/l

    tau_ratio = p(p(tau_t + tau_b, 2) + p(tau_s, 2), 1/2) / tau_allowable

    return_dict = {
        'lift_force': F_r,
        'lug_pin_diameter': {
            'req_value': d_reqd,
            'check': error_check(diameter_ratio)
        },
        'lug_thickness': {
            'req_value': t_max,
            'check': error_check(thickness_ratio)
        },
        'shear_stress_for_diameter': {
            'req_value': sigma_sd_calc,
            'check': error_check(sigma_sd_ratio)
        },
        'tensile_stress': {
            'req_value': sigma_t_calc,
            'check': error_check(sigma_t_ratio)
        },
        'bearing_stress': {
            'req_value': sigma_b_calc,
            'check': error_check(sigma_b_ratio)
        },
        'shear_stress_thickness': {
            'req_value': tau,
            'check': error_check(sigma_s_ratio)
        },
        'phi': phi,
        'length_shear': L_shear,
        'weld_area': A_weld,
        'lift_shear_stress': tau_s,
        'lift_tensile_stress': tau_t,
        'lift_bending_stress': tau_b,
        'tau_ratio': tau_ratio,
        'phi_shear': phi_shear
    }

    try:
        report = Report.objects.get(id=report_id)
    except:
        raise newError({
            "database":["Report cannot be found Please Create the report"]
            })

    try:
        component = Component.objects.filter(
            report__id=report_id, react_component_id=component_react_id)[0]
    except:
        raise newError({
            "database":["Component cannot be found Please Create the component"]
            })

    lug_state = LiftingLugState.objects.filter(
        report__id=report_id,
        component__id=component.id).update(
            W=W,
            phi=phi,
            x_1=x_1,
            x_2=x_2,
            F_r=F_r,
            d_reqd=d_reqd,
            diameter_ratio=diameter_ratio,
            D_p=D_p,
            sigma_sd_calc=sigma_sd_calc,
            sigma_sd_ratio=sigma_sd_ratio,
            t_reqd_tensile=t_reqd_tensile,
            L=L,
            d=d,
            sigma_t=sigma_t,
            sigma_b=sigma_b,
            sigma_t_calc=sigma_t_calc,
            sigma_t_ratio=sigma_t_ratio,
            t=t,
            t_reqd_bearing=t_reqd_bearing,
            A_bearing=A_bearing,
            sigma_b_calc=sigma_b_calc,
            sigma_b_ratio=sigma_b_ratio,
            phi_shear=phi_shear,
            L_shear=L_shear,
            H=H,
            a_2=a_2,
            t_reqd_shear=t_reqd_shear,
            t_max=t_max,
            thickness_ratio=thickness_ratio,
            A_shear=A_shear,
            tau=tau,
            sigma_s=sigma_s,
            sigma_s_ratio=sigma_s_ratio,
            A_weld=A_weld,
            t_w=t_w,
            alpha=alpha,
            tau_t=tau_t,
            tau_s=tau_s,
            M=M,
            Hght=Hght,
            c=c,
            h=h,
            l=l,
            tau_b=tau_b,
            tau_allowable=tau_allowable,
            tau_ratio=tau_ratio,
            lug_pin_check=return_dict['lug_pin_diameter']['check'],
            lug_thickness_check=return_dict['lug_thickness']['check'],
            shear_thickness_check=return_dict['shear_stress_thickness']['check'],
            shear_diameter_check=return_dict['shear_stress_for_diameter']['check'],
            tensile_check=return_dict['tensile_stress']['check'],
            bearing_check=return_dict['bearing_stress']['check']
    )

    if not lug_state:
        calc_steps = LiftingLugState(
            report=Report.objects.get(id=report_id),
            component=component,  # provide the component object here
            W=W,
            phi=phi,
            x_1=x_1,
            x_2=x_2,
            F_r=F_r,
            d_reqd=d_reqd,
            diameter_ratio=diameter_ratio,
            D_p=D_p,
            sigma_sd_calc=sigma_sd_calc,
            sigma_sd_ratio=sigma_sd_ratio,
            t_reqd_tensile=t_reqd_tensile,
            L=L,
            d=d,
            sigma_t=sigma_t,
            sigma_b=sigma_b,
            sigma_t_calc=sigma_t_calc,
            sigma_t_ratio=sigma_t_ratio,
            t=t,
            t_reqd_bearing=t_reqd_bearing,
            A_bearing=A_bearing,
            sigma_b_calc=sigma_b_calc,
            sigma_b_ratio=sigma_b_ratio,
            phi_shear=phi_shear,
            L_shear=L_shear,
            H=H,
            a_2=a_2,
            t_reqd_shear=t_reqd_shear,
            t_max=t_max,
            thickness_ratio=thickness_ratio,
            A_shear=A_shear,
            tau=tau,
            sigma_s=sigma_s,
            sigma_s_ratio=sigma_s_ratio,
            A_weld=A_weld,
            t_w=t_w,
            alpha=alpha,
            tau_t=tau_t,
            tau_s=tau_s,
            M=M,
            Hght=Hght,
            c=c,
            h=h,
            l=l,
            tau_b=tau_b,
            tau_allowable=tau_allowable,
            tau_ratio=tau_ratio,
            lug_pin_check=return_dict['lug_pin_diameter']['check'],
            lug_thickness_check=return_dict['lug_thickness']['check'],
            shear_thickness_check=return_dict['shear_stress_thickness']['check'],
            shear_diameter_check=return_dict['shear_stress_for_diameter']['check'],
            tensile_check=return_dict['tensile_stress']['check'],
            bearing_check=return_dict['bearing_stress']['check']
        )
        calc_steps.save()
    return return_dict
