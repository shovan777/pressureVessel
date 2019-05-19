from django.test import TestCase
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key, related

from pressureVessel import settings

from reporter.models import Report
from componentapp.component.models import Component

from state.models import CylinderState, NozzleState, HeadState, LiftingLugState, SkirtState, CentreOfGravity


class CylinderStateModelTest(TestCase):

    def setUp(self):
        self.report_data =  Recipe(Report,
            report_type ="vessel",
            author = "john",
            projectName = "ironthrone",
            orientation = "vertical",
            location_state = settings.STATIC_ROOT + 'states/user_john/ironthrone/data.json',
            location = settings.STATIC_ROOT + 'reports/user_john/'
        )
        self.component_data = Recipe(Component,
            report = self.report_data.make(),
            react_component_id = 1,
            type = "vessel",
            name = "test1"
        )
        self.cylinder_state = Recipe(
            CylinderState,
            report = self.report_data.make(),
            component = self.component_data.make()
        )

        self.nozzle_state = Recipe(
            NozzleState,
            report = self.report_data.make(),
            component = self.component_data.make()
        )

        self.head_state = Recipe(
            HeadState,
            report = self.report_data.make(),
            component = self.component_data.make()
        )

        self.lifting_lug_state = Recipe(
            LiftingLugState,
            report = self.report_data.make(),
            component = self.component_data.make()
        )

        self.skirt_state = Recipe(
            SkirtState,
            report = self.report_data.make(),
            component = self.component_data.make()
        )

    def test_CylinderState_string(self):
        cylinder_state_actual = self.cylinder_state.make()
        self.assertTrue(isinstance(cylinder_state_actual, CylinderState))
        self.assertTrue(isinstance(cylinder_state_actual.__str__(), str))
        self.assertTrue(cylinder_state_actual.__str__(), cylinder_state_actual.report.__str__() + " " + cylinder_state_actual.component.__str__())

    def test_NozzleState_string(self):
        nozzle_state_actual = self.nozzle_state.make()
        self.assertTrue(isinstance(nozzle_state_actual, NozzleState))
        self.assertTrue(isinstance(nozzle_state_actual.__str__(), str))
        self.assertTrue(nozzle_state_actual.__str__(), nozzle_state_actual.report.__str__() + " " + nozzle_state_actual.component.__str__())

    def test_HeadState_string(self):
        head_state_actual = self.head_state.make()
        self.assertTrue(isinstance(head_state_actual, HeadState))
        self.assertTrue(isinstance(head_state_actual.__str__(), str))
        self.assertTrue(head_state_actual.__str__(), head_state_actual.report.__str__() + " " + head_state_actual.component.__str__())

    def test_LiftingLugState_string(self):
        lifting_lug_state_actual = self.lifting_lug_state.make()
        self.assertTrue(isinstance(lifting_lug_state_actual, LiftingLugState))
        self.assertTrue(isinstance(lifting_lug_state_actual.__str__(), str))
        self.assertTrue(lifting_lug_state_actual.__str__(), lifting_lug_state_actual.report.__str__() + " " + lifting_lug_state_actual.component.__str__())

    def test_SkirtState_string(self):
        skirt_state_actual = self.skirt_state.make()
        self.assertTrue(isinstance(skirt_state_actual, SkirtState))
        self.assertTrue(isinstance(skirt_state_actual.__str__(), str))
        self.assertTrue(skirt_state_actual.__str__(), skirt_state_actual.report.__str__() + " " + skirt_state_actual.component.__str__())
