from django.test import TestCas

class StudentTestCase(TestCase):
    def test_student(self):
        student = Student.objects.create(name='John Doe')
        self.assertEqual(student.name, 'John Doe')

