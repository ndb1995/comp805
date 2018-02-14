from django.test import TestCase
from .models import Resume
# Create your tests here.
class ResumeTestCases(TestCase):
    def setup(self):
        """
        This runs at the beginning of every single test
        """
        my_resume = Resume(first_name="Joe", last_name="Smith")
        my_resume.save()

    def test_last_name_first(self):
        r = Resume.objects.first()
        self.assertEqual(r.last_name_first(),'Smith Joe')
