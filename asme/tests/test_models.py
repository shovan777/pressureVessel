"""Test the models of asme app."""
# external imports
from django.test import TestCase
from model_mommy import mommy

# internal imports
from asme.models import MaximumAllowableStress, NozzleData, PipingSchedule


class AsmeModelsTest(TestCase):

    def test_MaximumAllowableStress_creation(self):
        stress = mommy.make(MaximumAllowableStress)
        self.assertTrue(isinstance(stress, MaximumAllowableStress))
        self.assertTrue(isinstance(stress.__str__(), str))
        self.assertEqual(stress.__str__(), stress.spec_num + "_" + stress.type_grade)

    def test_NozzleData_creation(self):
        n_data = mommy.make(NozzleData)
        self.assertTrue(isinstance(n_data, NozzleData))
        self.assertTrue(isinstance(n_data.__str__(), str))
        self.assertEqual(n_data.__str__(), n_data.type_name + "_" +str(n_data.class_value)+ "_" + str(n_data.nominal_pipe_size))

    def test_PipingSchedule_creation(self):
        pipes = mommy.make(PipingSchedule)
        self.assertTrue(isinstance(pipes, PipingSchedule))
        self.assertTrue(isinstance(pipes.__str__(), str))
        self.assertEqual(pipes.__str__(), str(pipes.nominal_pipe_size) + "_" + pipes.schedules)