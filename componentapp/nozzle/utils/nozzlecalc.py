import math as m

def calculation_thick():
    
    # Available datas 
    # Design Conditions = 356 psig@ 300 degree F
    # Corrosion Allowance = 0.125 in
    # Weld Joint Efficiency = 1.0
    # Shell Material = SA-516-70N, 2007
    # Shell Allowable Stress = 20000 psi
    # Yield Strength = 33600 psi
    # Nozzle Material = SA-105, 2007
    # Nozzle Allowable Stress = 20000 psi
    # Cylinder Inside Diameter = 150.0 in
    # Cylinder Thickness = 1.8125 in
    # Nozzle Outside Diameter = 25.5 in 
    # Nozzle Thickness = 4.75 in
    # External Nozzle Projection = 14.1875 in
    # Internal Nozzle Projection = 0.0 in
    
    # The nozzle is inserted thorough the shell, i.e set-in type nozzle

    # variable meanings - 
    CDi = 150.0 # inch
    # CDi = Cylinder inside Diameter.
    C_A = 0.125
    # C_A = corrosion Allowance
    # CRi = Cylinder inside Radius
    Ct = 1.8125
    # Ct = Cylinder Thickness
    Nt = 4.75
    # Nt = Nozzle Thickness
    # Nr = Nozzle Radius
    ND = 25.5
    # ND = Nozzle Diameter
    # Nd = ---
    # Ctr = Cylinder Required Thickness
    DP = 351
    # DP = Design Pressure
    SAS = 20000 
    # SAS = Shell Allowable Stress
    WJE = 1.0
    # WJE = Weild Joint Efficiency
    # Ntr = Nozzle Required Thickness
    Sn = 20000
    # Sn = Nozzle Allowable Stress
    Sv = 20000
    # Sv = Shell Allowable Stress
    Sp = 20000
    # Sp = Shell Allowable Stress

    # Establish the corroded dimensions
    CDi = CDi + 2 * (C_A) # Di
    CRi = (CDi/2.0) # R
    Ct = Ct - C_A # t
    Nt = Nt - C_A # tn
    Nr = (ND - 2*(Nt))/2.0 # Rn
    Nd = 2 * Nr # d

    # Calculation as per Section VIII, Division I Solution

    # Evaluate per UG-37

    # The required thickness of the shell based on circumferential stress is give by UG-27 (c)(1).

    Ctr = float( (DP*CRi) / ((SAS * WJE) - (0.6*DP)) ) # tr

    # The required thickness of the nozzle based on circumferential stress is given by UG-27(c)(1).

    Ntr = float( (DP * Nr) / ((SAS * WJE) - (0.6*DP)) ) # trn

    # STEP 1: - Calculate the Limits of Reinforcement per UG-40
    
    # 1) Reinforcing dimensions for an integrally reinforced nozzle per Fig. UG-40(e), UG-40(e-1), UG-40(e-2)

    # tx = Radius of Pipe used (assumed using figure4.5.1)
    tx = 4.75 
    # L = Length of pipe projecting outside (assumed using figure4.5.1)
    '''
    From UG-37 Nomenclature (pg 40) (102)
    L = length of projection defining the thickened portion of integral reinforcement of a nozzle neck beyond the outside surface of the vessel wall [see Figure UG-40 sketch (e)]
    '''
    L = 7.1875
    '''
    From UG-37 Nomenclature (pg 40) (102)
    tn = nozzle wall thickness. 29 Except for pipe, this is the wall thickness not including forming allowances.
    For pipe, use the nominal thickness [see UG-16(d)]
    '''
    tn = 0
    '''
    From UG-37 Nomenclature (pg 40) (102)
    te = thickness or height of reinforcing element (see Figure UG-40)
    '''
    te = 0
    # From UG-37 Nomenclature (pg 40) (102)
    # Dp = outside diameter of reinforcing element 
    # actual size of reinforcing element may exceed the limits of reinforcement established by UG-40; 
    # however, credit cannot be taken for any material outside these limits
    Dp = 0
    # check condition
    if (L < 2.5*tx) :
        # use UG-40(e-1)
        tn = 9.5 - 8.0 - C_A
        te = (tx - 1.5 ) / m.tan(30)
        Dp = 2 * (12.75)
    else:
        # Left to be done
        print("need to do something")

    # 2) The limits of reinforcement, measured parallel to the vessel wall in the corroded condition:
    maxValue = max(Nd, (Nr + Nt + Ct))

    # 3) The limits of reinforcement, measured normal to the vessel wall in the corroded condition:
    minValue = min(2.5*Ct, 2.5*Nt + te)

    # STEP 2 - Calculate reinforcement strength parameters per UG-37

    # 1) Strength Reduction Factors:
    '''
    From UG-37 Nomenclature (pg 40) (102)
    fr = strength reduction factor, not greater than 1.0 [see UG-41(a)]
    fr1 = Sn/Sv for nozzle wall inserted through the vessel wall
    fr1 = 1.0 for nozzle wall abutting the vessel wall and for nozzles shown in Figure UG-40,sketch (j), (k), (n) and (o).
    fr2 = Sn/Sv
    fr3 = (lesser of Sn or Sp )/Sv
    fr4 = Sp/Sv
    '''
    '''
    From UG-37 Nomenclature (pg 40) (102)
    S = allowable stress value in tension (see UG-23),psi (MPa)
    Sn = allowable stress in nozzle, psi (MPa) (see S above)
    Sp = allowable stress in reinforcing element (plate), psi (MPa) (see S above)
    Sv = allowable stress in vessel, psi (MPa) (see S above)
    '''
    fr1 = Sn/Sv
    fr2 = Sn/Sv
    fr3 = min(Sn,Sp)/Sv
    fr4 = Sp/Sv

    # 2) Joint Efficiency Parameter: For a nozzle located in a solid plate 
    '''
    From UG-37 Nomenclature (pg 40) (102)
    E 1 = 1 when an opening is in the solid plate or in a Category B butt joint
        = 0.85 when an opening is located in an ERW or autogenously welded pipe or tube. 
        If the ERW or autogenously welded joint is clearly identifiable and it can be shown that the opening does not pass through this weld joint, then E1 may be determined using the other rules of this paragraph
        = joint efficiency obtained from Table UW-12 when any part of the opening passes through any other welded joint
    '''

    E1 = 1.0

    # 3) Correction Factor for variation of internal pressure stresses on different planes with respect to the axis of the vessel: 
    # For a radial nozzle in a cylinder shell
    '''
    From UG-37 Nomenclature (pg 40) (102)
    F = correction factor that compensates for the variation in internal pressure stresses on different planes with respect to the axis of a vessel. 
    A value of 1.00 shall be used for all configurations except that Figure UG-37 may be used for integrally reinforced openings in cylindrical shells and cones. [See UW-16(c)(1).]
    '''
    F =1.0

    # STEP 3 - Calculate the Areas of Reinforcement, see Fig. UG-37.1 (With Reinforcing Element, per Fig. UG-40(e-1)).

    # 1) Area Required, A
    # From UG-37 Nomenclature (pg 39) (101)
    # A = total cross-sectional area of reinforcement required in the plane under consideration (see Figure UG-37.1)
    # includes consideration of nozzle area through shell if Sn/Sv < 1.0
    A = Nd * Ctr * F + 2* Nt * Ctr * F * (1 - fr1)

    # 2) Area Available in the Shell, A1. Use larger value
    A11 = Nd * ( (E1 * Ct) - (F * Ctr) ) - 2 * Nt * ((E1 * Ct ) - (F * Ctr) ) * (1 - fr1)
    A12 = 2 * ( Ct - Nt) * ( (E1 * Ct) - (F * Ctr) ) - 2 * Nt * ( (E1 * Ct) - (F * Ctr) ) * (1 - fr1)
    
    # From UG-37 Nomenclature (pg 39) (101)
    # A1 = area in excess thickness in the vessel wall available for reinforcement (see Figure UG-37.1)
    # includes consideration of nozzle area through shell if Sn/Sv < 1.0
    A1 = max(A11,A12)

    # 3) Area Available in the Nozzle projecting Outward A2, Use Smaller value
    A21 = 5 * (Nt - Ntr) * fr2 * Ct
    A22 = 2 * (Nt - Ntr) * ( (2.5 * Nt) + te) * fr2

    # From UG-37 Nomenclature (pg 39) (101)
    # A2 = area in excess thickness in the nozzle wall available for reinforcement (see Figure UG-37.1)
    A2 = min(A21,A22)

    # 4) Area Available in the Nozzle Projecting Inward, A3. Use smaller value.
    '''
    From UG-37 Nomenclature (pg 40) (102)
    ti = nominal thickness of internal projection of nozzle wall
    '''
    ti = 0 # ??? # Given in example
    '''
    From UG-37 Nomenclature (pg 40) (102)
    h = distance nozzle projects beyond the inner surface of the vessel wall.
    (Extension of the nozzle beyond the inside surface of the vessel wall is not limited; however, for reinforcement calculations, credit shall not be taken for material outside the limits of reinforcement established by UG-40.)
    '''
    h = 0 # ??? 
    Cm1 = 5 * Ct * ti * fr2
    Cm2 = 5 * ti * ti * fr2
    Cm3 = 2 * h * ti * fr2

    # From UG-37 Nomenclature (pg 40) (102)
    # A3 = area available for reinforcement when the nozzle extends inside the vessel wall (see Figure UG-37.1)
    A3 = min (Cm1,Cm2,Cm3)

    # 5) Area Available in Welds, A41,A42,A43, Use the following minimum specified weld leg dimensions, see Figure E4.5.1 of the example:

    # Outer Nozzle Fillet Weld leg : 0.375 in
    Onfwl = 0.375 # leg
    # Outer Element Fillet Weld leg : 0.0 in
    Oefwl = 0.0
    # Inner Element Fillet Weld leg : 0.0 in
    Iefwl = 0.0

    # From UG-37 Nomenclature (pg 40) (102)
    # A41,A42,A43 = cross‐sectional area of various welds available for reinforcement (see Figure UG-37.1)
    A41 = m.pow(Onfwl,2) * fr3
    A42 = m.pow(Oefwl,2) * fr4 # might be in example 0.0 given # 
    A43 = m.pow(Iefwl,2) * fr2 # might be in example 0.0 given

    # 6) Area Available in Element, A5:
    # From UG-37 Nomenclature (pg 40) (102)
    # A5 = cross‐sectional area of material added as reinforcement (see Figure UG-37.1)
    A5 = (Dp - Nd - 2 * Nt) * te * fr4

    # Note: The thickness of the reinforcing pad, te , exceed the outer vertical reinforcement zone limit. Therefore, the reinforcement area in the pad is limited to within the zone.

    # 7) Total Available Area, Aavail :
    Aavail = A1 + A2 + A3 + (A41 + A42 + A43) + A5 

    # STEP 4 - Nozzle reinforcement acceptance criterion:
    if Aavail > A :
        # Therefore, the nozzle is adequately reinforced
        print('Therefore, the nozzle is adequately reinforced')
    else:
        # need to be done something
        print('Need to be done at last')

         