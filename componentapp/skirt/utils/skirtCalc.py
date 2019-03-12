import math as m

def skirtCalculation(diameter,thickness,corossionAllowance,stress,reportId):

    diameterInside = diameter + 2 * corossionAllowance
    radiusInside = 0.5 * diameterInside
    thicknessCorroded  = thickness - corossionAllowance
    diameterOutside = diameter + 2 * thicknessCorroded
    radiusOutside = 0.5 * diameterOutside

    '''
    In accordance with VIII-2, paragraph 4.3.10.2, the following procedure shall be used to design cylindrical, spherical, and conical shells subjected to internal pressure plus supplemental loads of applied net section axial force, bending moment, and torsional moment. By inspection of the results shown in Table E4.15.2.2 and Table E4.15.2.3, Load Case 6 is determined to be a potential governing load case. The pressure, net section axial force, and bending moment at the location of interest for Load Case 6 are: So
    P = Ps = 0.0 psi
    F6 = -427775 lbs
    M6 = 21900435 in - lbs
    '''
    # TODO: given need to know what it is
    P = 0.0
    F6 = -437775
    M6 = 21900435
    '''
    STEP 1 – Calculate the membrane stress for the cylindrical shell. Note that the circumferential membrane stress, sigmaThetam , is determined based on the equations in UG-27(c)(1) and the exact strength of materials solution for the longitudinal membrane stress, sigmasm , is used in place of the approximate solution provided in UG-27(c)(2). The shear stress is computed based on the known strength of materials solution. For the skirt, weld joint efficiency is set as E = 1.0 .
    Note: theta is defined as the angle measured around the circumference from the direction of the applied bending moment to the point under consideration. For this example problem theta = 0.0 deg to maximize the bending stress
    '''
    # TODO: given need to know what it is
    theta = 0.0
    E = 1.0

    sigmaThetam = ( ( (P*radiusInside)/thicknessCorroded ) + 0.6 * P )/E

    sigmasmSection1 = (P* m.pow(diameterInside,2))/(m.pow(diameterOutside,2)-m.pow(diameterInside,2))
    sigmasmSection2 = (4*F6)/(m.pi*(m.pow(diameterOutside,2)-m.pow(diameterInside,2)))
    sigmasmSection3 = (32 * M6 * diameterOutside * m.cos(theta))/ (m.pi*(m.pow(diameterOutside,4)-m.pow(diameterInside,4)))

    sigmasmadd = (sigmasmSection1+sigmasmSection2+sigmasmSection3) / E
    sigmasmsub = (sigmasmSection1+sigmasmSection2-sigmasmSection3) / E

    # TODO: given need to know what it is
    Mt = 0.0
    
    tilde = (16 * Mt * diameterOutside) / (m.pi*(m.pow(diameterOutside,4)-m.pow(diameterInside,4)))

    '''
    STEP 2 – Calculate the principal stresses
    '''
    sigma1 = 0.5 * (sigmaThetam+sigmasmsub+m.sqrt(m.pow((sigmaThetam-sigmasmsub),2)+4*m.pow(tilde,2)))
    sigma2 = 0.5 * (sigmaThetam+sigmasmsub-m.sqrt(m.pow((sigmaThetam-sigmasmsub),2)+4*m.pow(tilde,2)))
    sigma3 = -0.5 * P

    '''
    STEP 3 – Check the allowable stress acceptance criteria.
    '''
    sigmae = (1/m.sqrt(2))* m.sqrt(m.pow((sigma1-sigma2),2)+m.pow((sigma2-sigma3),2)+m.pow((sigma3-sigma1),2))

    if sigmae <= stress :
        pass
    else :
        return 'need to change the parameters'

    '''
    STEP 4 – For cylindrical and conical shells, if the meridional stress, sigmasm is compressive, then check the allowable compressive stress per UG-23(b).Sincesigmasm is compressive, {sigmasm = -3421.0021 psi < 0 } , a compressive stress check is required. sigmasm <= Fxa (Fxa =0)
    '''
    # TODO: need to be verified
    Fxa = 0.0
    if sigmasmsub < Fxa:
        pass
    else :
        return 'not compressive'

    '''
    Evaluate per paragraph UG-23(b). The maximum allowable longitudinal compressive stress to be used in the design of cylindrical shells or tubes, either seamless or butt welded, subjected to loadings that produce longitudinal compression in the shell or tube shall be the smaller of the maximum allowable tensile stress value shown in STEP 3 or the value of the factor B determined by the following procedure where the joint efficiency for butt welded joints shall be taken as unity.
    '''
    # weldJointEffiency = 1.0 # as above paragraph

    '''
    STEP 4.1 – Using the selected values of thicknessCorroded and radiusOutside , calculate the value of factor A using the following formula
    '''
    factorA = (0.125*thicknessCorroded)/radiusOutside

    '''
    STEP 4.2 – Using the value of A calculated in STEP 4.1, enter the applicable material chart in Subpart 3 of Section II, Part D for the material under consideration. Move vertically to an intersection with the material/temperature line for the design temperature. Interpolation may be made between lines for intermediate temperatures. In cases where the value of A falls to the right of the material/temperature line, assume and intersection with the horizontal projection of the upper end of the material/temperature line. For values of A falling to the left of the material/temperature line, see STEP 4.4. Per Section II Part D, Table 1A, a material specification of SA-516-70 N is assigned an External Pressure Chart No. CS-2.
    STEP 4.3 – From the intersection obtained in Step 4.2, move horizontally to the right and read the value of factor B . This is the maximum allowable compressive stress for the values of t and R o used in STEP 4.1.
    '''
    factorB = 12300 #psi

    '''
    STEP 4.4 – For values of A falling to the left of the applicable material/temperature line, the value of B shall be calculated using the following formula:
    factorB = (factorA * E) / 2 Not required
    '''

    '''
    STEP 4.5 – Compare the calculated value of factorB obtained in STEPS 4.3 or 4.4 with the computed longitudinal compressive stress in the cylindrical shell or tube, using the selected values of thicknessCorroded and radiusOutside . If the value of factorB is smaller than the computed compressive stress, a greater value of thicknessCorroded must be selected and the design procedure repeated until a value of factorB is obtained that is greater than the compressive stress computed for the loading on the cylindrical shell or tube.
    '''

    if abs(sigmasmsub) <= factorB :
        return 'The allowable compressive stress criterion is satisfied.'
    else:
        return 'The allowable compressive stress criterion is not satisfied.'