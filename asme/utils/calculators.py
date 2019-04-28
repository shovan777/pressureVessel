from exceptionapp.exceptions import newError

def max_stress_calculator(row_dict,temp):
    temp_list = [100, 150, 200, 250, 300, 400, 500, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    # temp = data1.get('temp1')
    max_stress = 0
    for temperature_index in range(len(temp_list)):
        if temp <= temp_list[0]:
            max_stress = row_dict['max_stress_20_100']
            return max_stress
        elif temp > temp_list[len(temp_list)-1]:
            raise newError({
                "temp_error":["Temperatue is too high for the material"]
            })
        elif temp_list[temperature_index] ==temp:
            max_stress = row_dict['max_stress_'+ str(temp)]
            return max_stress
        elif temp_list[temperature_index] > temp:
            max_stress1 = 0
            if temp_list[temperature_index-1] == temp_list[0]:
                max_stress1 = row_dict['max_stress_20_100']
            else:
                max_stress1 = row_dict['max_stress_'+ str(temp_list[temperature_index-1])]
            max_stress2 = row_dict['max_stress_' + str(temp_list[temperature_index])]
            temperature1 = temp_list[temperature_index-1]
            temperature2 = temp_list[temperature_index]
            max_stress = (((max_stress2-max_stress1)*(temp-temperature1))/(temperature2-temperature1)) + max_stress1
            return max_stress
        
