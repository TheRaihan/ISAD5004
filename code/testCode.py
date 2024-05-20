import unittest, sys,os, io
import Person, Helper


class TestHelper(unittest.TestCase):
    
    def testParseBirthday(self):
        # Test case 1: valid date format "dd-mm-yyyy"
        self.assertEqual(Utils.parse_birthday("25-12-2020"), "25122020")
        
        # Test case 2: valid date format "dd Month yyyy"
        self.assertEqual(Utils.parse_birthday("25 December 2020"), "25122020")
        
        # Test case 3: invalid date format
        self.assertFalse(Utils.parse_birthday("2020-12-25"))
        
        # Test case 4: invalid date with non-date string
        self.assertFalse(Utils.parse_birthday("not a date"))
        
        # # Test case 5: invalid date format with invalid month
        # self.assertFalse(Utils.parse_birthday("25-13-2020"))
        
        # # Test case 6: invalid date format with invalid day
        # self.assertFalse(Utils.parse_birthday("32-12-2020"))
        
        # # Test case 7: invalid date format "Month dd, yyyy"
        # self.assertFalse(Utils.parse_birthday("December 25, 2020"))
        
        # Test case 8: valid date format with leading zero in day
        self.assertEqual(Utils.parse_birthday("01-01-2020"), "01012020")
        self.assertEqual(Utils.parse_birthday("01 January 2020"), "01012020")

if __name__ == '__main__':
    unittest.main()
