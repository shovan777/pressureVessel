# """Test the calculations of asme app."""
# from django.test import SimpleTestCase
# from exceptionapp.exceptions import newError

# from asme.models import MaximumAllowableStress
# from asme.utils.calculators import max_stress_calculator


# class AsmeUtilsTest(SimpleTestCase):
#     row_dict = MaximumAllowableStress.objects.filter(
#     spec_num='SA-516').filter(type_grade='60').values()[0]

#     def test_temp_below_min_val(self):
#         temp1 = 20
#         expected_val = self.row_dict['max_stress_20_100']
#         ret_val = max_stress_calculator(self.row_dict, temp1)
#         self.assertEqual(expected_val, ret_val)

#     def test_temp_exact_val(self):
#         temp1 = 900
#         expected_val = self.row_dict['max_stress_900']
#         ret_val = max_stress_calculator(self.row_dict, temp1)
#         self.assertEqual(expected_val, ret_val)

#     def test_temp_interpolate_val(self):
#         temp1 = 350
#         expected_val = 17.1
#         ret_val = max_stress_calculator(self.row_dict, temp1)
#         self.assertEqual(expected_val, ret_val)

#     def test_temp_interpolate_lessthan_150(self):
#         temp1 = 110
#         expected_val = 17.1
#         ret_val = max_stress_calculator(self.row_dict, temp1)
#         self.assertEqual(expected_val, ret_val)

#     def test_temp_above_max_val(self):
#         temp1 = 2000
#         error_msg = 'Temperatue is too high for the material'
#         with self.assertRaises(newError) as error:
#             max_stress_calculator(self.row_dict, temp1)
#         # TODO: manage access to error code and message
#         self.assertEqual(error.exception.get_full_details()['temp_error']['message'], error_msg)

