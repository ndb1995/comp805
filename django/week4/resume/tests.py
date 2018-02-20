from django.test import TestCase
from . models import resume, education, experience
# Create your tests here.
class ResumeTestCases(TestCase):
    def setUp(self):
        """
        This runs at the beginning of every single test
        """
        self.resume = resume.objects.create(
            first_name='Nicholas',
            last_name='Bielinski',
        )
        self.experience = experience.objects.create(
            parent_resume=self.resume,
            title='Helpdesk Technician',
            location='L3 Technologies',
            start_date='6/26/2017',
            end_date='present',
            description='blah blah blah'
        )
        self.education = education.objects.create(
            parent_resume=self.resume,
            institution_name='UNH Manchester',
            location='Manchester',
            degree='Bachelor',
            major='CIS',
            gpa = '3.5'
        )

    def test_full_name(self):
        '''

        '''
        self.assertEqual(resume.full_name(self.resume), 'Nicholas Bielinski')

    def test_last_name_first_name(self):
        '''
        '''
        self.assertEqual(resume.last_name_first_name(self.resume), 'Bielinski, Nicholas')

    def test_get_experience(self):
        '''
        '''
        case = list(self.resume.get_experience())
        expected = list(self.resume.experience_set.all())
        self.assertEqual(case,expected)

    def test_get_education(self):
        '''
        '''
        case = list(self.resume.get_education())
        expected = list(self.resume.education_set.all())
        self.assertEqual(case,expected)
