from django.test import TestCase

from model_mommy import mommy
from model_mommy.recipe import Recipe

from pressureVessel import settings

from reporter.models import Report,report_path

class ReportTestModel(TestCase):
    
    def setUp(self):
        self.report_one = mommy.make('reporter.Report',
            report_type ="vessel",
            author = "john",
            projectName = "ironthrone",
            orientation = "vertical",
            location_state = settings.STATIC_ROOT + 'states/user_john/ironthrone/data.json',
            location = settings.STATIC_ROOT + 'reports/user_john/'
        )

    def test_report_model(self):
        self.assertTrue(isinstance(self.report_one, Report))
        self.assertTrue(isinstance(self.report_one.__str__(), str))
        
    def test_report_path(self):
        expected_val = '{0}{1}/{2}/{3}/{4}.pdf'.format(
            settings.STATIC_ROOT+'reports/',
            'user_'+self.report_one.author,
            self.report_one.created_at.date(),
            self.report_one.created_at.time().strftime('%H-%M-%S'),
            self.report_one.projectName
        )
        self.assertEqual(expected_val,self.report_one.location)

    def test_state_path(self):
        expected_val = '{0}{1}/{2}/data.json'.format(
            settings.STATIC_ROOT+'states/',
            'user_'+self.report_one.author,
            self.report_one.projectName
        )
        self.assertEqual(expected_val, self.report_one.location_state)

    def test_string(self):
        expected_val = '{0} {1} {2}'.format(
            self.report_one.author,
            self.report_one.projectName,
            self.report_one.orientation
        )
        self.assertEqual(expected_val, self.report_one.__str__())

    def test_false_pass(self):
        returned_val = report_path(self.report_one)
        expected_val = 'user_{0}/{1}/{2}/{3}.pdf'.format(
            self.report_one.author, 
            self.report_one.created_at.date(), 
            self.report_one.created_at.time().strftime('%H-%M-%S'), 
            'report'
        )
        self.assertEqual(expected_val, returned_val)