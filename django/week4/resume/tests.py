from django.test import TestCase
from . models import resume, education, experience
# Create your tests here.
class ResumeTestCases(TestCase):
    def setUp(self):
        """
        This runs at the beginning of every single test
        Here we explicitly create new resume, experience and education objects
        I also could have done self.resume, self.experience, self.educuation
        If i did that I wouldn't have had to declare variables in the
        testing functions. I could just refer to the object itself Instead
        of assigning it to another variable, if I understand that correctly
        """
        resume.objects.create(
            first_name='Nicholas',
            last_name='Bielinski',
        )
        experience.objects.create(
            title='Helpdesk Technician',
            location='L3 Technologies',
            start_date='6/26/2017',
            end_date='present',
            description='blah blah blah'
        )
        education.objects.create(
            institution_name='UNH Manchester',
            location='Manchester',
            degree='Bachelor',
            major='CIS',
            gpa = '3.5'
        )

    def test_full_name(self):
        """
        This method will grab the first resume object
        and compare it to our test case and what we expect
        using the method defined in our resume model full_name
        """
        current_resume = resume.objects.first()
        expected = 'Nicholas Bielinski'
        case = current_resume.full_name()
        self.assertEqual(case, expected)

    def test_last_name_first_name(self):
        """
        This method will grab the first resume object
        and compare it to our test case and what we expect
        using the method defined in our resume model last_name_first_name
        """
        current_resume = resume.objects.first()
        expected = 'Bielinski, Nicholas'
        case = current_resume.last_name_first_name()
        self.assertEqual(case, expected)

    def test_get_experience(self):
        """
        This method will grab the first resume object
        and compare it to our test case and what we expect
        using the method defined in our resume model get_experience
        """
        current_resume = resume.objects.first()
        expected = list(current_resume.get_experience())
        case = list(current_resume.experience_set.all())
        self.assertEqual(case,expected)

    def test_get_education(self):
        """
        This method will grab the first resume object
        and compare it to our test case and what we expect
        using the method defined in our resume model get_education
        """
        current_resume = resume.objects.first()
        expected = list(current_resume.get_education())
        case = list(current_resume.education_set.all())
        self.assertEqual(case,expected)
