import math as m

def skirtCalc():
    
    '''
    From example problems Manual VIII 1.pdf
    page number 260
    4.15 Supports and Attachments
    4.15.1 Example E4.15.1 - Horizontal Vessel with Zick's Analysis
    '''

    response_text = {}
    '''
    Vessel Data:
    Material = SA-516-70, 2007
    Design Conditions = 2074 psig @ 175 degree F
    Outside Diameter = 66.0 in
    Thickness = 3.0 in
    Corrosion Allowance = 0.125 in
    Formed Head Type = 2:1 Elliptical
    Head Height (Based on OD) = 16.5 in
    Allowable Stress = 20000 psi
    Weld Joint Efficiency = 1.0
    Shel Tangent to Tangent Length = 292.0 in
    '''

    vessel_inside_diameter = 60.0 # inch
    corrosion_allowance = 0.125 # inch
    thickness_with_corrosion_allowance = 3.0 # inch
    vessel_outside_diameter = 66.0 # inch
    vessel_overall_length = 292.0 # inch (L) Shell Tangent to Tangent Length
    head_heigth = 16.5 # in (h2) Head Height (Based on OD)
    design_pressure = 2074 # psig (P) Design Conditions
    allowable_stress = 20000 # psi (S) Allowable Stress
    weld_joint_efficiency = 1.0 # (E) Weld Joint Efficiency
    
    '''
    Saddle Data:
    Material = SA-516-70, 2007
    Saddle Center Line to Head Tangent Line = 41.0 in
    Saddle Contact Angle = 123.0 deg
    Width of Saddles = 8.0 in 
    Vessel Load per Saddle = 50459.0 lbs
    '''

    theta_given = 123.0 # Saddle Contact Angle
    saddle_center_line_to_head_tangent_line = 41.0 # inch (a) Saddle Center Line to Head Tangent Line
    vessel_load_per_saddle = 50459.0 # lbs (Q) Vessel Load per Saddle
    width_of_saddle = 8.0 # inch (b) Width of Saddles.
    '''
    Adjust the vessel inside diameter and thickness by the corrosion allowance.
    '''
    vessel_inside_diameter_with_corrosion_allowance = vessel_inside_diameter + 2 * corrosion_allowance
    thickness_without_corrosion_allowance = thickness_with_corrosion_allowance - corrosion_allowance # 2.875 inch (t)
    Rm = (vessel_outside_diameter + vessel_inside_diameter_with_corrosion_allowance)/4.0

    '''
    Section VIII, Division 1 Solution
    VIII-1 does not provide rules for saddle supported vessels. However, 
    UG-22 requires consideration of such loadings and the provisions of 
    U-2(g) apply. This example provides one possible method of satisfying 
    U-2(g); however, other methods may also be deemed accepatable by the 
    Manufacturer and accepted by the Authorized Inspector.

    Zick's analysis is one of the accepted analysis procedures for determining
    the stresses in the shell of a horizontal drum support on two saddle supports.
    The Zick's analysis procedure is provided in VII-2, paragraph 4.15.3, and this 
    procedure will be used in this example problem.
    '''

    '''
    VIII-2, paragraph 4.15.3.1, Application of Rules
    a) The stress calculation method is based on linear elastic mechanics and
    covers modes of failure by excessive deformation and elastic instability.
    b) Saddle supports for horizontal vessels shall be configured to provide
    continuous support for at least one-third of the shell circumference, or 
    theta = 120.0 deg.
    Since {theta=123.0 deg} >= {theta_required = 120.0 deg } the geometry is acceptable
    '''
    
    theta_required = 120.0 # deg

    if theta_given >= theta_required:
        # response_text = "The geometry is acceptable."
        response_text.update({"1":"The geometry is acceptable"})
    else:
        # response_text = "The geometry is not acceptable i.e theta is below 120 degree."
        response_text.update({"1":"The geometry is not acceptable i.e theta is below 120 degree."})

    '''
    VIII-2, paragraph 4.15.3.2, Moment and Shear Force
    The vessel is composed of a cylindrical shell with formed heads at each end
    that is supported by two equally spaced saddle supports. The moment at the
    saddle, M1, the moment at the center of the vessel, M2, and the shear force
    at the saddle, T, may be computed if the distance between the saddle centerline 
    and head tangent line satisfies the following limit.
    {a=41.0 in} <= {0.25L = 0.25(292.0)=73.0 in} Satisfied
    '''

    if saddle_center_line_to_head_tangent_line <= 0.25 * vessel_overall_length:
        # response_text = "Position of saddle Satisfied"
        response_text.update({"2":"Position of saddle Satisfied"})
    else:
        # response_text = "Position of saddle Should be changed away from the head."
        response_text.update({"2":"Position of saddle Should be changed away from the head."})

    '''
    Bending Moment at the Saddle
    '''

    moment_one_upper_part_2 = saddle_center_line_to_head_tangent_line/vessel_overall_length
    moment_one_upper_part_3 = (m.pow(Rm, 2) - m.pow(head_heigth, 2))/(2*saddle_center_line_to_head_tangent_line*vessel_overall_length)

    moment_one_upper_part = 1 - moment_one_upper_part_2 + moment_one_upper_part_3

    moment_one_lower_part = 1 + (4 * head_heigth)/(3 * vessel_overall_length)

    moment_one = - vessel_load_per_saddle * saddle_center_line_to_head_tangent_line * (1- (moment_one_upper_part/moment_one_lower_part))

    '''
    Bending Moment at the Center of the Vessel
    '''

    moment_two_upper_part_2 = 2 *  (m.pow(Rm, 2) - m.pow(head_heigth, 2))/(m.pow(vessel_overall_length, 2))

    moment_two_upper_part = 1 + moment_two_upper_part_2

    moment_two_lower_part = moment_one_lower_part

    moment_two_middle_part = 4 * moment_one_upper_part_2

    moment_two = ((vessel_load_per_saddle * vessel_overall_length)/4) * ((moment_two_upper_part/moment_two_lower_part)-moment_two_middle_part)

    '''
    Shear Force at the Saddle
    '''

    shear_force_upper_part = vessel_load_per_saddle * (vessel_overall_length - (2 * saddle_center_line_to_head_tangent_line))

    shear_force_lower_part = vessel_overall_length + ((4 * head_heigth)/3)

    shear_force = shear_force_upper_part/shear_force_lower_part # 33746.5 lbs (T)

    '''
    VIII-2, paragraph 4.15.3.3, Longitudinal Stress
    a) The longitudinal membrance plus bending stresses in the cylindrical shell
    between the supports are given by the following equations.
    At the top of shell:
    '''

    sigma_part_one = (design_pressure * Rm) / (2 * thickness_without_corrosion_allowance)
    sigma_part_two = moment_two /(m.pi * m.pow(Rm, 2) * thickness_without_corrosion_allowance)
    sigma_one = sigma_part_one - sigma_part_two

    '''
    Note: A load combination that includes zero internal pressure and the vessel
    full of contents would provide the largest compressive stress at the top of
    the shell, and should be checked as part of the design.
    At the bottom of the shell:
    '''

    sigma_two = sigma_part_one + sigma_part_two

    '''
    b) The longitudinal stresses in the cylindrical shell at the support location
    are given by the following equations. The values of these strsses depend on
    the rigidity of the saddle support. The cylindrical shell may be considered
    as suitably stiffened if it incorporates stiffening rings at, or on both sides
    of the saddle support, or if the support is sufficiently close defined as 
    a <= 0.5 Rm to the elliptical head.
    Since {a=41.0 in} > {0.5Rm = 0.5(31.5625) = 15.7813 in}, the criterion is not satisfied.
    '''

    if saddle_center_line_to_head_tangent_line > 0.5 * Rm:
        # response_text = "The criterion is not satisfied."
        response_text.update({"3":"The criterion is not satisfied."})
    else:
        # response_text = "The criterion is satisfied."
        response_text.update({"3":"The criterion is satisfied."})

    '''
    Therefore, for an unstiffened shell, calculate the maximum values of longitudinal
    membrance plus bending stresses at the saddle support as follows.
    At points A and B in VIII-2, Figure 4.15.5:
    '''

    delta = (m.pi/6) + ((5 * (theta_given*(m.pi/180.0)))/12) # 1.4181 rad

    '''
    Where the coefficient K1 is found in VIII-2, Table 4.15.1,
    '''

    K1_upper_part = delta+m.sin(delta)*m.cos(delta)-((2*m.pow(m.sin(delta), 2))/delta)
    K1_lower_part = m.pi * ((m.sin(delta)/delta)-m.cos(delta))

    K1 = K1_upper_part/K1_lower_part # 0.1114

    sigma_three_astrick_second_part = moment_one /(K1 * m.pi * m.pow(Rm, 2) * thickness_without_corrosion_allowance)

    sigma_three_astrick = sigma_part_one - sigma_three_astrick_second_part # 11740.5 psi

    '''
    At the bottom of the shell:
    '''

    '''
    Where the coefficient K1_astrick is found in VIII-2, Table 4.15.1,
    '''

    K1_upper_part_astrick = K1_upper_part
    K1_lower_part_astrick = m.pi * (1 - (m.sin(delta)/delta))

    K1_astrick = K1_upper_part_astrick/K1_lower_part_astrick


    sigma_four_astrick_second_part = moment_one /(K1_astrick * m.pi * m.pow(Rm, 2) * thickness_without_corrosion_allowance)

    sigma_four_astrick = sigma_part_one + sigma_four_astrick_second_part

    '''
    c) Acceptance Criteria:
    '''

    acceptance_criteria = allowable_stress * weld_joint_efficiency

    if abs(sigma_one) <= acceptance_criteria:
        # response_text = "Sigma One criteria is satisfied."
        response_text.update({"4":"Sigma One criteria is satisfied."})
    else:
        # response_text = "Sigma One criteria is not satisfied."
        response_text.update({"4":"Sigma One criteria is not satisfied."})

    if abs(sigma_two) <= acceptance_criteria:
        # response_text = "Sigma two criteria is satisfied."
        response_text.update({"5":"Sigma two criteria is satisfied."})
    else:
        # response_text = "Sigma two criteria is not satisfied."
        response_text.update({"5":"Sigma two criteria is not satisfied."})

    if abs(sigma_three_astrick) <= acceptance_criteria:
        # response_text = "Sigma three astrick criteria is satisfied."
        response_text.update({"6":"Sigma three astrick criteria is satisfied."})
    else:
        # response_text = "Sigma three astrick criteria is not satisfied."
        response_text.update({"6":"Sigma three astrick criteria is not satisfied."})

    if abs(sigma_four_astrick) <= acceptance_criteria:
        # response_text = "Sigma four astrick criteria is satisfied."
        response_text.update({"7":"Sigma four astrick criteria is satisfied."})
    else:
        # response_text = "Sigma four astrick criteria is not satisfied."
        response_text.update({"7":"Sigma four astrick criteria is not satisfied."})

    '''
    Since all calculated stresses are positive (tensile), the compressive stress
    check per VIII-2, paragraph 4.15.3.3.c.2 is not required.
    '''

    '''
    VIII-2, paragraph 4.15.3.4, Shear Stresses
    The shear stress in the cylindrical shell without stiffening rings that is not
    stiffened by a formed head,
    {a=41.0 in} > { 0.5Rm = 0.5(31.5625) = 15.7813 in}, is calculated as follows:
    '''

    if saddle_center_line_to_head_tangent_line > 0.5 * Rm:
        # response_text = "The criterion is not satisfied."
        response_text.update({"8":"The criterion is not satisfied."})
    else:
        # response_text = "The criterion is satisfied."
        response_text.update({"8":"The criterion is satisfied."})

    alpha = 0.95 * (m.pi-((theta_given*(m.pi/180.0))/2)) # rad 1.9648 (alpha)

    '''
    Where the coefficient K2 is found in VIII-2, Table 4.15.1,
    '''

    K2 = m.sin(alpha)/(m.pi-alpha+(m.sin(alpha)*m.cos(alpha)))

    tilde_2 = (K2*shear_force)/(Rm*thickness_without_corrosion_allowance)

    '''
    Acceptance Criteria, where C = 0.8 for ferritic materials:
    '''

    C = 0.8

    if tilde_2 <= C*allowable_stress:
        # response_text = "The acceptance criteria for shear stresses is satisfied."
        response_text.update({"9":"The acceptance criteria for shear stresses is satisfied."})
    else:
        # response_text = "The acceptance criteria for shear stresses is not satisfied."
        response_text.update({"9":"The acceptance criteria for shear stresses is not satisfied."})

    '''
    Per VIII-2, paragraph 4.15.3.5, Circumferential Stress
    a) Maximum circumferential bending moment - the distribution of the circumferential
    bending moment at the saddle support is dependent on the use of stiffeners at the
    saddle location. For a cylindrical shell without a stiffening ring, the maximum
    circumferential bending moment is shown in VIII-2, Figure 4.15.6 Sketch (a) and 
    is calculated as follows.
    '''

    beta = m.pi - ((theta_given*(m.pi/180))/2)

    K6_upper_part_part_1 = ((3*m.cos(beta))/4.0) * m.pow((m.sin(beta)/beta), 2)
    K6_upper_part_part_2 = (5*m.sin(beta)*m.pow(m.cos(beta), 2))/(4*beta)
    K6_upper_part_part_3 = m.pow(m.cos(beta), 3)/2.0
    K6_upper_part_part_4 = m.sin(beta)/(4.0*beta)
    K6_upper_part_part_5 = m.cos(beta)/4.0
    K6_common_part = m.pow((m.sin(beta)/beta), 2)-0.5-(m.sin(2*beta)/(4*beta))
    K6_upper_part_part_6 = beta * m.sin(beta) * K6_common_part

    K6_upper_part = K6_upper_part_part_1-K6_upper_part_part_2+K6_upper_part_part_3-K6_upper_part_part_4+K6_upper_part_part_5-K6_upper_part_part_6

    K6_lower_part = 2 * m.pi * K6_common_part
    
    K6 = K6_upper_part/K6_lower_part

    K7 = 0

    if saddle_center_line_to_head_tangent_line/Rm >= 1.0:
        K7 = K6
    else:
        K7 = 0

    moment_beta = K7 * vessel_load_per_saddle * Rm


    '''
    b) Width of cylindrical shell - the width of the cylindrical shell that contributes
    to the strength of the cylindrical shell at the saddle location shall be determined
    as follows.
    '''

    x1 = 0.78*m.sqrt(Rm*thickness_without_corrosion_allowance)
    x2 = x1

    '''
    If the width (0.5b+x1) extends beyond the limit of a, as shown in VIII-2,
    Figure 4.15.2, then the width x1 shall be reduced such as not to exveed a.
    {(0.5b+x1) = 0.5(8.0) + 7.4302=11.4302in}<={a=41.0in} Satisfied
    '''
    if ((0.5*width_of_saddle)+x1) <= saddle_center_line_to_head_tangent_line:
        # response_text = "Width of Cylindrical Shell is satisfied."
        response_text.update({"10":"Width of Cylindrical Shell is satisfied."})
    else:
        # response_text = "Width of Cylindrical Shell is not satisfied."
        response_text.update({"10":"Width of Cylindrical Shell is not satisfied."})

    '''
    c) Circumferential Stresses in the cylindical shell without stiffening rings.
    The maximum compressive circumferential membrane stress in the cylindrical 
    shell at the base of the saddle support shall be calculated as follows:
    '''

    '''
    Where the coefficient K5 is found in Table 4.15.1,
    '''

    K5 = (1+m.cos(alpha))/(m.pi-alpha+(m.sin(alpha)*m.cos(alpha)))

    k = 0.1 # when the vessel is welded to the saddle support

    sigma_six = -(K5*vessel_load_per_saddle*k)/(thickness_without_corrosion_allowance*(width_of_saddle+x1+x2))

    '''
    The circumferential compressive membrance plus bending stress at Points G
    and H of VIII-2,
    Figure 4.15.6 Sketch (a) is determined as follows.
    If L>=*Rm, then the circumferential compressive membrance plus bending stress
    shall be computed using VIII-2, Equation 4.15.24
    Since {L=292.0 in} >= {8*Rm = 8(31.5625)=252.5in}, the criterion is satisfied.
    '''

    if vessel_overall_length >= 8*Rm:
        # response_text = "Circumferential Compressive membrance criterion is satisfied."
        response_text.update({"11":"Circumferential Compressive membrance criterion is satisfied."})
    else:
        # response_text = "Circumferential Compressive membrance criterion is not statisfied."
        response_text.update({"11":"Circumferential Compressive membrance criterion is not statisfied."})

    sigma_seven_first_part = -vessel_load_per_saddle/(4*thickness_without_corrosion_allowance*(width_of_saddle+x1+x2))
    sigma_seven_second_part = (3*K7*vessel_load_per_saddle)/(2*m.pow(thickness_without_corrosion_allowance, 2))

    sigma_seven = sigma_seven_first_part+sigma_seven_second_part

    '''
    The stresses at sigma_6 and sigma_7 may be reduced by adding a reinforcement or
    wear plate at the saddle location that is welded to the cylinderical shell.
    A wear plate was not specified in this problem.
    Acceptance Criteria:
    '''

    if sigma_six <= allowable_stress:
        # response_text = "Circumferential Compressive membrane plus bending stress acceptance criteria is satisfied sigma six."
        response_text.update({"12":"Circumferential Compressive membrane plus bending stress acceptance criteria is satisfied sigma six."})
    else:
        # response_text = "Circumferential Compressive membrane plus bending stress acceptance criteria is not satisfied sigma six."
        response_text.update({"12":"Circumferential Compressive membrane plus bending stress acceptance criteria is not satisfied sigma six."})

    if sigma_seven <= (1.25*allowable_stress):
        # response_text = "Circumferential Compressive membrane plus bending stress acceptance criteria is satisfied sigma seven."
        response_text.update({"13":"Circumferential Compressive membrane plus bending stress acceptance criteria is satisfied sigma seven."})
    else:
        # response_text = "Circumferential Compressive membrane plus bending stress acceptance criteria is not satisfied sigma seven."
        response_text.update({"13":"Circumferential Compressive membrane plus bending stress acceptance criteria is not satisfied sigma seven."})

    '''
    VIII-2, paragraph 4.15.3.6, Horizontal Splitting Force
    The horizontal force at the minimum section at the low point of the saddle is
    given by VIII-2, Equation (4.15.42). The saddle shall be designed to resist this
    force.
    '''

    force_h_upper_part = 1+m.cos(beta)-(0.5*m.pow(m.sin(beta), 2))
    force_h_lower_part = m.pi-beta+(m.sin(beta)*m.cos(beta))
    force_h = vessel_load_per_saddle * (force_h_upper_part/force_h_lower_part)

    '''
    Note: The horizontal splitting force is equal to the sum of all of the horizontal
    reactions at the saddle due to the weight loading of the vessel. The splitting force
    is used to calculate tension stress and bending stress in the web of the saddle.
    The following provides one possible method of calculationg the tension and bending
    stress in the web and its acceptance criteria. However, other methods may also be 
    deemed acceptable by the Manufacturer and accepted by the Authorized Inspector.
    The membrance stress is given by,
    '''
    As = 1
    '''
    Where As is the cross-sectional area of the web at the low point of the saddle
    with units of in^2,
    '''
    sigma_t = force_h/As
    Sy = 1 
    '''
    Sy is the yield stress of the saddle material with units of psi
    '''
    if sigma_t <= 0.6*Sy:
        # response_text = "Fh/As is satisfied."
        response_text.update({"14":"Fh/As is satisfied."})
    else:
        # response_text = "Fh/As is not satisfied."
        response_text.update({"14":"Fh/As is not satisfied."})

    '''
    The bending stress is given by,
    '''
    d = 1
    c = 1
    I = 1
    '''
    where d is the moment arm of the horizontal splitting force, measured from the 
    center of gravity of the saddle arc to the bottom of the saddle baseplate with
    units of in, c is the distance from the centroid of the saddle composite section
    to the extreme fiber with units of in, I is the moment of inertia of the composite
    section of the saddle with units in in^4 , and Sy is the yield stress of the saddle
    material with units in psi.
    '''
    sigma_b = (force_h*d*c)/I

    if sigma_b<=0.66*Sy:
        # response_text = "sigma_b and Sy is satisfied."
        response_text.update({"15":"sigma_b and Sy is satisfied."})
    else:
        # response_text = "sigma_b and Sy is not satisfied."
        response_text.update({"15":"sigma_b and Sy is not satisfied."})

    return response_text