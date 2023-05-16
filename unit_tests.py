import io
import unittest
from unittest.mock import patch
from benchmark_checker import Checker, CourseProgress

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Checker()

    def test_check_benchmark_completion(self):
        completed_courses = ['INST 201', 'INST 126', 'STAT 100']
        benchmark_courses = ['INST 201', 'INST 126', 'STAT 100']
        self.assertTrue(self.checker.check_benchmark_completion(benchmark_courses, completed_courses))

        benchmark_courses = ['PSYC 100', 'MATH 115']
        self.assertFalse(self.checker.check_benchmark_completion(benchmark_courses, completed_courses))

    def test_get_completed_benchmarks(self):
        completed_courses = ['PSYC 100', 'MATH 115', 'INST 201', 'INST 126', 'STAT 100']
        completed_benchmarks = self.checker.get_completed_benchmarks(completed_courses)
        expected_benchmarks = []
        self.assertCountEqual(completed_benchmarks, expected_benchmarks)

    def test_get_incomplete_benchmarks(self):
        completed_courses = ['PSYC 100', 'MATH 115', 'INST 201', 'INST 126', 'STAT 100']
        incomplete_benchmarks = self.checker.get_incomplete_benchmarks(completed_courses)
        expected_benchmarks = []
        self.assertCountEqual(incomplete_benchmarks, expected_benchmarks)


class TestCourseProgress(unittest.TestCase):
    def test_print_remaining_courses(self):
        completed_courses = [
            'PSYC 100', 'MATH 115', 'INST 201', 'INST 126', 'STAT 100',
            'INST 335', 'INST 326', 'INST 327', 'INST 314', 'INST 311',
            'INST 362', 'INST 346', 'INST 352'
        ]
        incomplete_courses = ['INST 490']
        course_progress = CourseProgress(completed_courses, incomplete_courses)

        expected_output = "Remaining courses to complete:\nINST 490\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            course_progress.print_remaining_courses()
        self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
