
# INST 326-0106 Final Project (Benchmark Checker): Irene Song, Alexander Martini, Kevin Agbedi

""" Documentation:

Our motivation behind this project is to address the challenges that students face in keeping track of the various courses they need to complete,
respective to benchmark 1, benchmark 2, core courses, and the capstone for the information science major. We wrote an interactive command-line tool
that asks for user input on what courses they have completed. For conformity, we renamed the core courses and capstone requirements as benchmark 3 and benchmark 4.
Our program then informs the user of which benchmarks they have completed, which benchmarks they have not completed, and which courses they must complete in order
to fulfill the required benchmarks that have not yet been completed.Our program then informs the user of which benchmarks they have completed, which
benchmarks they have not completed, and which courses they must complete in order to fulfill the required benchmarks that have not yet been completed.

To run the program from the command line, make sure to set your working directory to wherever our program is stored, along with the 4 text files.
Next, you can write 'python3 benchmark_checker.py' if you have a Mac device or 'python benchmark_checker.py' if you don't in the command line in a terminal to run the program.

We did not require any outside sources to develop the program, other than knowledge from the class and previous classes, as well as the INST 326 class slides.
"""

import unittest

class Checker:
    """ A class to check which benchmarks the user has and has not completed according to which courses they have taken.
    """
    
    def __init__(self):
        """ Initializes a Checker object with benchmark data read in from text files.

        Args:
            benchmark_files (list): a list of file names containing benchmark data
        """
        self.benchmark_files = ['benchmark1.txt', 'benchmark2.txt', 'benchmark3.txt', 'benchmark4.txt']
        self.benchmarks = {}
        for file in self.benchmark_files:
            with open(file, 'r') as f:
                benchmark_name = file.split('.')[0]
                self.benchmarks[file] = f.read().splitlines()



    def completed_courses(self):
        """ Prompts the user to enter the names of their completed courses.

        Returns:
            completed (list): a list of the user's completed course names
        """
        completed = []
        while True:
            course = input('Enter the name of the courses you have completed one by one (or "done" when finished): ')
            if course == 'done':
                break
            completed.append(course)
        return completed



    def check_benchmark_completion(self, benchmark_courses, completed_courses):
        """ Checks if all the courses within a benchmark have been completed.

        Args:
            benchmark_courses (list): a list of course names required for the benchmark
            completed_courses (list): a list of course names completed by the user

        Returns:
            boolean: True if all benchmark courses are completed, False if otherwise
        """
        return all(course in completed_courses for course in benchmark_courses)



    def get_completed_benchmarks(self, completed_courses):
        """ Returns a list of completed benchmarks based on the completed courses entered by the user.

        Args:
            completed_courses (list): a list of course names completed by the user

        Returns:
            completed_courses (list): a list of course names completed by the user
        """
        completed_benchmarks = []
        for benchmark_name, benchmark_courses in self.benchmarks.items():
            if self.check_benchmark_completion(benchmark_courses, completed_courses):
                completed_benchmarks.append(benchmark_name)
        return completed_benchmarks



    def get_incomplete_benchmarks(self, completed_courses):
        """ Returns a list of incomplete benchmarks based on completed courses entered by the user.

        Args:
            completed_courses (list): a list of course names completed by the user

        Returns:
            incomplete_benchmarks (list): a list of benchmark names that have not been completed by the user
        """
        incomplete_benchmarks = []
        for benchmark_name, benchmark_courses in self.benchmarks.items():
            if not self.check_benchmark_completion(benchmark_courses, completed_courses):
                incomplete_benchmarks.append(benchmark_name)
        return incomplete_benchmarks



    def print_completed_benchmarks(self, completed_benchmarks):
        """ Prints the names of completed benchmarks to the console.

        Args:
            completed_benchmarks (list): a list of benchmark names completed by the user
        """
        print('Completed benchmarks:')
        for benchmark_name in completed_benchmarks:
            print(f'- {benchmark_name}')



    def print_incomplete_benchmarks(self, incomplete_benchmarks):
        """ Prints the names of incomplete benchmarks to the console.

        Args:
            incomplete_benchmarks (list): a list of benchmark names that have not been completed by the user

        Returns:
            None
        """
        print('Incomplete benchmarks:')
        for benchmark_name in incomplete_benchmarks:
            print(f'- {benchmark_name}')



class CourseProgress:
    """ A class to track a user's progress in completing a set of courses.
    """

    def __init__(self, completed_courses, incomplete_courses):
        """ Initializes a CourseProgress object.

        Parameters:
            completed_courses (list): a list of courses the user has completed.
            incomplete_courses (list): a list of courses the user has yet to complete.
        """
        self.completed_courses = completed_courses
        self.incomplete_courses = incomplete_courses

    def print_remaining_courses(self):
        """ Prints the list of courses that the user has yet to complete.
        """
        print("Remaining courses to complete:")
        for course in self.incomplete_courses:
            print(course)



class TestChecker(unittest.TestCase):
    """ A class to perform unit tests.
    """
    def setUp(self):
        self.checker = Checker()

    def test_check_benchmark_completion(self):
        
        completed_courses = ['INST 201', 'INST 126', 'STAT 100']
        benchmark_courses = ['INST 201', 'INST 126', 'STAT 100']
        self.assertTrue(self.checker.check_benchmark_completion(benchmark_courses, completed_courses))

        benchmark_courses = ['PSYC 100', 'MATH 115']
        self.assertFalse(self.checker.check_benchmark_completion(benchmark_courses, completed_courses))

    def test_get_completed_benchmarks(self):
        
        completed_courses = ['PSYC 100', 'MATH 115']
        completed_benchmarks = self.checker.get_completed_benchmarks(completed_courses)
        self.assertListEqual(completed_benchmarks, ['benchmark1.txt'])

        completed_courses = ['PSYC 100', 'MATH 115', 'INST 201', 'INST 126', 'STAT 100']
        completed_benchmarks = self.checker.get_completed_benchmarks(completed_courses)
        self.assertListEqual(completed_benchmarks, ['benchmark1.txt', 'benchmark2.txt'])

    def test_get_incomplete_benchmarks(self):
        
        completed_courses = ['PSYC 100', 'MATH 115']
        incomplete_benchmarks = self.checker.get_incomplete_benchmarks(completed_courses)
        self.assertListEqual(incomplete_benchmarks, ['benchmark2.txt', 'benchmark3.txt', 'benchmark4.txt'])

        completed_courses = ['PSYC 100', 'MATH 115', 'INST 201', 'INST 126', 'STAT 100']
        incomplete_benchmarks = self.checker.get_incomplete_benchmarks(completed_courses)
        self.assertListEqual(incomplete_benchmarks, ['benchmark3.txt', 'benchmark4.txt'])

class TestCourseProgress(unittest.TestCase):

    def test_print_remaining_courses(self):
        
        completed_courses = ['PSYC 100', 'MATH 115', 'INST 201', 'INST 126', 'STAT 100', 'INST 335', 'INST 326', 'INST 327', 'INST 314', 'INST 311', 'INST 362', 'INST 346', 'INST 352']
        incomplete_benchmarks = ['benchmark4.txt']
        course_progress = CourseProgress(completed_courses, incomplete_benchmarks)

        expected_output = "Remaining courses to complete: INST 490"
        with captured_output() as (out, err):
            course_progress.print_remaining_courses()
        self.assertEqual(out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()


