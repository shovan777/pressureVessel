"""Calculate inner thickness."""
from math import exp, atan, cos, pi

def head_t(P, S, D, C_A, report_id,E=1.0):
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
    lower_part = float( (2 * S * 1000 * E) - (0.2 * P) )
    return (upper_part/lower_part) + float(C_A)

def center_of_gravity(headDiameterOutside,density,skirtHeight,headThickness,Sf=2):
    headHeightOutside = headDiameterOutside/4
    headVolumeOutside = ((2*pi*pow((headDiameterOutside/2.0),2)*(headHeightOutside))/3)+(pi*pow((headDiameterOutside/2.0),2)*Sf)
    headIndividualCGOutside = (4*headHeightOutside)/(3*pi)
    cgFromDatumOutside = (skirtHeight-headIndividualCGOutside)

    headDiameterInside = headDiameterOutside-headThickness
    headHeightInside = headDiameterInside/4
    headVoulmeInside = ((2*pi*pow((headDiameterInside/2.0),2)*(headHeightInside))/3)+(pi*pow((headDiameterInside/2.0),2)*Sf)
    headIndividualCGInside = (4*headHeightInside)/(3*pi)
    cgFromDatumInside = (skirtHeight-headIndividualCGInside)

    netHeadVolume = headVolumeOutside-headVoulmeInside
    netCGFromDatum = (cgFromDatumInside+cgFromDatumOutside)/2.0

    newWeight = netHeadVolume * density
    weightTimesCG = newWeight*netCGFromDatum

    return weightTimesCG,newWeight
