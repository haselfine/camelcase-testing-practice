'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_max_student_is_zero(self): #tests whether StudentError is raised when creating a class size of 0 or less
        with self.assertRaises(StudentError):
            test_class = ClassList(0)

        with self.assertRaises(StudentError):
            test_class = ClassList(-1)

    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    # adds some example students, 
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_add_remove_student_not_in_list(self):
        test_class = ClassList(1)
        test_class.add_student('Lucca')
        with self.assertRaises(StudentError):
            test_class.remove_student('Margot')


    # removes a student from an 
    # empty list, and asserts a StudentError is raised
    def test_remove_from_empty_list(self):
        test_class = ClassList(2)
        with self.assertRaises(StudentError):
            test_class.remove_student('Margot')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## adds some example students to a test class,
    ## then, calls is_enrolled for a student who is not enrolled. 
    # Uses assertFalse to verify is_enrolled returns False.
    def test_is_not_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Lucca')
        test_class.add_student('Margot')
        self.assertFalse(test_class.is_enrolled('Mara'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## tests index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
    def test_index_of_student_list_empty(self):
        test_class = ClassList(3)
        self.assertIsNone(test_class.index_of_student('Lucca'))
 
 
    ## tests index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # asserts that searching for a student name that is not in the list, returns None.
    def test_index_of_student_list_student_is_not_present(self):
        test_class = ClassList(3)
        test_class.add_student('Margot')
        test_class.add_student('Mara')
        self.assertIsNone(test_class.index_of_student('Lucca'))

   
    def test_is_class_full(self): #tests whether is_class_full works as intended
        test_class = ClassList(1)
        test_class.add_student('Jordan')
        self.assertTrue(test_class.is_class_full())

        test_class_two = ClassList(2)
        test_class_two.add_student('Ben')
        test_class_two.add_student('Neb')
        self.assertTrue(test_class_two.is_class_full())
    
    def test_is_class_full_empty(self): #tests that is_class_full returns false with empty class
        test_class = ClassList(3)

        self.assertFalse(test_class.is_class_full())
