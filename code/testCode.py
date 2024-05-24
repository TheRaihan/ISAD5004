import unittest, sys,os, io
from unittest.mock import Mock
from datetime import datetime

from main import Person, Helper


class TestPerson(unittest.TestCase):

    '''
    change it to file input
    '''

    def test_life_path_number(self):
        # Test case #1: Enters While loop
        birthday = datetime.strptime("01-01-1901","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test1", birthday)
        self.assertEqual(4, self.main.get_life_path_number(), msg = "Test Case #1 Failed")

        # Test case #2: Enters if in while loop
        birthday = datetime.strptime("20 April 1998","%d %B %Y").strftime("%d%m%Y")
        self.main = Person("test2", birthday)
        self.assertEqual(33, self.main.get_life_path_number(), msg = "Test Case #2 Failed")


    
    def test_get_generation(self):
        # Test case #1: year falls within the Silent Generation (1901-1945)

        birthday = datetime.strptime("01-01-1901","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test1", birthday)
        self.assertEqual("Silent Generation", self.main.get_generation(), msg = "Test Case #1 Failed (Lower Boundary)")

        birthday = datetime.strptime("31-12-1945","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test1", birthday)
        self.assertEqual("Silent Generation", self.main.get_generation(), msg = "Test Case #1 Failed (Higher Boundary)")
        
        # Test case #2: year falls within the Baby Boomers

        birthday = datetime.strptime("01 January 1946","%d %B %Y").strftime("%d%m%Y")
        self.main = Person("test2", birthday)
        self.assertEqual("Baby Boomers", self.main.get_generation(), msg = "Test Case #2 Failed (Lower Boundary)")

        birthday = datetime.strptime("31-12-1964","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test2", birthday)
        self.assertEqual("Baby Boomers", self.main.get_generation(), msg = "Test Case #2 Failed (Higher Boundary)")

        # Test case #3: year falls within the Generation X

        birthday = datetime.strptime("01-01-1965","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test3", birthday)
        self.assertEqual("Generation X", self.main.get_generation(), msg = "Test Case #3 Failed (Lower Boundary)")

        birthday = datetime.strptime("31 December 1979","%d %B %Y").strftime("%d%m%Y")
        self.main = Person("test3", birthday)
        self.assertEqual("Generation X", self.main.get_generation(), msg = "Test Case #3 Failed (Higher Boundary)")

        # Test case #4: year falls within the Millennials

        birthday = datetime.strptime("01 February 1980","%d %B %Y").strftime("%d%m%Y")
        self.main = Person("test4", birthday)
        self.assertEqual("Millennials", self.main.get_generation(), msg = "Test Case #4 Failed (Lower Boundary)")

        birthday = datetime.strptime("30 November 1994","%d %B %Y").strftime("%d%m%Y")
        self.main = Person("test4", birthday)
        self.assertEqual("Millennials", self.main.get_generation(), msg = "Test Case #4 Failed (Higher Boundary)")

        # Test case #5: year falls within the Generation Z

        birthday = datetime.strptime("01-01-1995","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test5", birthday)
        self.assertEqual("Generation Z", self.main.get_generation(), msg = "Test Case #5 Failed (Lower Boundary)")

        birthday = datetime.strptime("31-12-2009","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test5", birthday)
        self.assertEqual("Generation Z", self.main.get_generation(), msg = "Test Case #5 Failed (Higher Boundary)")

        # Test case #6: year falls within the Generation Alpha

        birthday = datetime.strptime("01-01-2010","%d-%m-%Y").strftime("%d%m%Y")    
        self.main = Person("test6", birthday)
        self.assertEqual("Generation Alpha", self.main.get_generation(), msg = "Test Case #6 Failed (Lower Boundary)")

        birthday = datetime.strptime("31-12-2024","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test6", birthday)
        self.assertEqual("Generation Alpha", self.main.get_generation(), msg = "Test Case #6 Failed (Higher Boundary)")

        # Test case #7: year outside known generations
        birthday = datetime.strptime("31-12-2025","%d-%m-%Y").strftime("%d%m%Y")
        self.main = Person("test6", birthday)
        self.assertEqual("Unknown Generation", self.main.get_generation(), msg = 'Test Case #7 Failed')


class TestHelper(unittest.TestCase):
    
    def test_valid_birthday(self):
        # Test case 1: valid input in "DD-MM-YYYY" format
        sys.stdin = io.StringIO("01-01-2000\n")
        result = Helper.get_valid_birthday_input()
        self.assertEqual(result, "01012000")
        sys.stdin = sys.__stdin__

        # Test case 2: valid input in "DD Month YYYY" format
        sys.stdin = io.StringIO("15 June 1995\n")
        result = Helper.get_valid_birthday_input()
        self.assertEqual(result, "15061995")
        sys.stdin = sys.__stdin__

        # Test case 3: invalid input followed by valid input
        sys.stdin = io.StringIO("invalid\n10-20-2000\n30 February 2022\n05 May 2023\n")
        result = Helper.get_valid_birthday_input()
        self.assertEqual(result, "05052023")
        sys.stdin = sys.__stdin__
        
    def test_sum_digits(self):
        # Test case 1: sum of digits of a single digit number
        self.assertEqual(Helper.sum_digits(5), 5)

        # Test case 2: sum of digits of a multi-digit number
        self.assertEqual(Helper.sum_digits(123), 6)  # 1 + 2 + 3 = 6
        
        # Test case 3: sum of digits of a large number
        self.assertEqual(Helper.sum_digits(987654321), 45) # 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
        
        # Test case 4: sum of digits of zero
        self.assertEqual(Helper.sum_digits(0), 0)

    def test_is_master_number(self):
        
        # Test case 1: num is a master number (33)
        self.assertTrue(Helper.is_master_number(33))
        
        # Test case 2: num is not a master number (10)
        self.assertFalse(Helper.is_master_number(10))
        
        # Test case 3: num is a string
        self.assertFalse(Helper.is_master_number("eleven"))
        
        # Test case 4: num is None
        self.assertFalse(Helper.is_master_number(None))
        
        # Test case 5: num is a list
        self.assertFalse(Helper.is_master_number([11]))

    def test_life_path_compare(self):
        # Test case 1: num is a master number (11)
        person1 = Mock()
        person2 = Mock()

        # Test case 1: Same life path number
        person1.life_path_num = 5
        person2.life_path_num = 5
        self.assertTrue(Helper.lifePathCompare(person1, person2))

        # Test case 2: Different life path numbers
        person1.life_path_num = 1
        person2.life_path_num = 9
        self.assertFalse(Helper.lifePathCompare(person1, person2))

        # Test case 3: String life path number
        person1.life_path_num = "5"
        person2.life_path_num = 5
        self.assertFalse(Helper.lifePathCompare(person1, person2))

        # Test case 4: None as life path number
        person1.life_path_num = None
        person2.life_path_num = 5
        self.assertFalse(Helper.lifePathCompare(person1, person2))

if __name__ == '__main__':
    unittest.main()





# boundary value unit test
#file input output
