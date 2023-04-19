
class classPicker:
    """ The following represents an object similar to testudo, something where 
    you can choose and view the classes taken,
    """
    
    
    def __init__(self, path, credits ):
        """
        Intializes the current objects attributes.
        
        Args:
         path (str) = representing a path to a file which contains all the classes
         available to take.
         
         credits (int) = represents the amount of credits each course is.
        """    
        self.courses = {}
        with open(path, "r", enconding= "utf-8") as f:
            data = f.read()
            
        for classes in data:
            self.courses[classes] = classes.name
            self.credits = self.courses[classes].numcredits
            
            
        
    def getclass(self, name):
        """ Following gets the current class the user wants info on.
        
        Args:
         name (str) = a string representing the name of the class
         
        Returns:
         returns the key in the dictionary of courses matching the name of the class.
        """
        return self.courses[name]
        
        
    def addcourse(self, course):
        """ The following will add a course to the users schedule.
        
        args:
        
        course (Course): A course object which will be the one that will be added to the list.
        
        Side - effects:
        
        Modifies the current objects dictionary of courses and adds the new course.
        """
        self.coures[course] = course.name
        
        
    def required_course_groups():
            """ Loads the required course groups from the text files.

            Args:
                benchmark_file (str): path to the text files containing the benchmark courses
            Returns:
                courses (list): a list of courses for the benchmarks
            """





    def completed_benchmarks():
            """ Prompts the user to input the courses they have completed and returns them as a list.

            Returns:
                completed (list): a list of courses the user has completed
            """





    def incompleted_courses():
            """ Gets the missing courses for a benchmark.

            Args:
                courses (list): a list of courses for the benchmarks
                completed (list): a list of courses the user has completed
            Returns:
                incomplete (list): a list of courses the user has not yet completed
            """





    def prerequisites():
            """ Gets the prerequisite courses for a list of courses.

            Args:
                incomplete (list): a list of courses the user has not yet completed
            Returns:
                prerequisites (list): a list of prerequisites required for the incomplete courses of the user, if any
            """





    def permission_required():
            """ Gets the courses that require permissions for a list of courses.
            Args:
                incomplete (list): a list of courses the user has not yet completed
            Returns:
                permission (list): a list of courses that require permission for the incompleted courses of the user, if any
            """




    def check_benchmarks():
            """ Checks the user's completed and missing courses for each benchmark and prints the results.
            
            """
