
import unittest

class Checker:
    
    def __init__(self, benchmark_files):
        """ Initializes a Checker object with benchmark data read in from text files.

        Args:
            benchmark_files (list): a list of file names containing benchmark data
        """
        self.benchmarks = {}
        for filename in benchmark_files:
            with open(filename, 'r') as f:
                benchmark_name = filename.split('.')[0]
                self.benchmarks[benchmark_name] = [line.strip() for line in f]



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





class TestChecker(unittest.TestCase):
    
    def setUp(self):
        self.checker = Checker(['benchmark1.txt', 'benchmark2.txt', 'benchmark3.txt', 'benchmark4.txt'])

    def test_check_benchmark_completion_all_completed(self):
        benchmark_courses = ['course1', 'course2', 'course3']
        completed_courses = ['course1', 'course2', 'course3']
        self.assertTrue(self.checker.check_benchmark_completion(benchmark_courses, completed_courses))

    def test_check_benchmark_completion_not_completed(self):
        benchmark_courses = ['course1', 'course2', 'course3']
        completed_courses = ['course1', 'course2']
        self.assertFalse(self.checker.check_benchmark_completion(benchmark_courses, completed_courses))

    def test_get_completed_benchmarks(self):
        completed_courses = ['course1', 'course2', 'course3', 'course4']
        expected = ['benchmark1', 'benchmark3']
        self.assertEqual(self.checker.get_completed_benchmarks(completed_courses), expected)

    def test_get_incomplete_benchmarks(self):
        completed_courses = ['course1', 'course2', 'course3']
        expected = ['benchmark2', 'benchmark4']
        self.assertEqual(self.checker.get_incomplete_benchmarks(completed_courses), expected)

if __name__ == '__main__':
    unittest.main()

