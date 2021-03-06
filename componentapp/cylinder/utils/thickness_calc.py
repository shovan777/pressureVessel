"""Calculate inner thickness."""
import math as m
from reporter.models import Report
from state.models import CylinderState
from componentapp.component.models import Component

from exceptionapp.exceptions import newError

def cylinder_t(P, S, D, C_A, report_id, component_react_id, E=1.0):
    """Calculate thickness as per ASME DIV I

    Parameters
    ----------
    P : float psi
        Design pressure or max allowable working pressure.
    S : float psi
        Stress value of material.
    D : float inches
        Inside diameter.
    CA : float inches
        Corrosion allowance.
    E : float max 1.0
        Joint Efficiency.

    Returns
    -------
    float
        Description of returned object.

    """

    # Process to calculate using Postgres Procedure
    # with connection.cursor() as cursor:
    #     cursor.callproc('cylinder_t', [P, S, D, C_A, E])
    #     return cursor.fetchall()[0][0]

    R = float((D+2*C_A)/2)
    upper_part = float(P * R)
    lower_part = float((S * 1000 * E) - (0.6 * P))
    t_inter = upper_part/lower_part
    t = t_inter + C_A
    # think about how you can save the calculation steps later
    # check if the cylinder is a new one or older
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

    cylinder_state = CylinderState.objects.filter(
        report__id=report_id,
        component__id=component.id).update(
            P=P,
            D=D,
            C_A=C_A,
            R=D/2.0,
            S=S,
            E=E,
            t_inter=t_inter,
            t=t
        )
    if not cylinder_state:
        calc_steps = CylinderState(
            report=Report.objects.get(id=report_id),
            component=component,  # provide the component object here
            P=P,
            D=D,
            C_A=C_A,
            R=D/2.0,
            S=S,
            E=E,
            t_inter=t_inter,
            t=t
        )
        calc_steps.save()
    
    
    return t
    # return (upper_part/lower_part) + C_A


def conical_t(P, S, D_l, D_s, L_c, CA, report_id, E=1.0):
    
    

    D_l += 2 * CA
    D_s += 2 * CA
    alpha = m.atan(0.5 * (D_l - D_s) / L_c)
    t_wo_allowance = (P * D_l) / (2 * m.cos(alpha) * (S * E * 1000 - 0.6 * P))
    return t_wo_allowance + CA


def center_of_gravity(cylinderDiameter, cylinderLength, density,thicknessCylinder):
    cylinderVolumeOuter = (m.pi*m.pow((cylinderDiameter/2.0), 2)*cylinderLength)
    # sum of inidividual CG, S.F. of ellipsoidal head, height of skirt
    cylinderVolumeInner = (m.pi*(m.pow(((float(cylinderDiameter)-float(thicknessCylinder))/2.0), 2.0)*cylinderLength))

    netVolumeOfCylinder = cylinderVolumeOuter-cylinderVolumeInner

    newWeight = netVolumeOfCylinder*density


    return newWeight
