"""Test the models of asme app."""
# external imports
from django.test import TestCase
from model_mommy import mommy

# internal imports
from componentapp.component.models import Component
from reporter.models import Report


class ComponentModelsTest(TestCase):
    pass

    # def create_report(self,
    #     created_at=,
    #     report_type="vessel",
    #     location= "dfasd",
    #     location_state="",
    #     author="",
    #     projectName="",
    #     orientation=""
    #     ):

    #     return Report.objects.create()

    # def create_component(self,
    #     report='1',
    #     react_component_id = 1,
    #     type = 1,
    #     name = 'calcgen'
    #     ):
    #     return Component.objects.create(
    #         report=report,
    #         react_component_id=react_component_id,
    #         type=type,
    #         name=name
    #         )

    # def test_Component_creation(self):
    #     component = self.create_component()
    #     self.assertTrue(isinstance(component, Component))
    #     self.assertTrue(isinstance(component.__str__(), str))
    #     self.assertEqual(component.__str__(), component.report.__str__() + "--" + component.type)
