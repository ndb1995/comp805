"""
print("\nFirst Function: Switch Case\n")
print (lab3.switch_case(['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']))

print("\nSecond Function: Only Even\n")
print (lab3.only_even(['orange', 5, 'pear', 2, 'kiwi', 7, '10']))

print("\nThird Function: Greatest Difference\n")
print (lab3.greatest_difference([1,20,15,5,10,17,34,45,13,65]))

print("\nFourth Function: Make Title\n")
print (lab3.make_title([1,20,15,5,10,17,34,45,13,65]))

print("\nFifth Function: Test Title\n")
print (lab3.test_title(['Orange', 'Apple', 'pear', 'Strawberry', 'kiwi', 'apple', 'banana']))

print("\nSixth Function: Create Word\n")
print (lab3.create_word(['Orange', 'Apple', 'pear', 'Strawberry', 'kiwi', 'apple', 'banana']))

print("\nSeventh Function: Three Times Number\n")
print (lab3.three_times_nums([1,20,15,5,10,17,34,45,13,65]))

print("\nEigth Function: Keep Lowercase\n")
print (lab3.keep_lowercase(['ORANGE', 'APPLE', 'pear', 'STRAWBERRY', 'kiwi', 'apple', 'banana']))

print("\nNinth Function: Multiplication Total Of\n")
print (lab3.multiplication_total_of([1,20,15,5,10,17,34,45,13,65]))

print("\nTenth Function: Square Nums\n")
print (lab3.square_nums([1,20,15,5,10,17,34,45,13,65]))

print("\nEleventh Function: Less Than 5\n")
print (lab3.lessthan_5([1,20,15,5,10,17,34,45,13,65]))
"""
import unittest
class Lab4Test(unittest.TestCase):
    def test_only_even(self):
        """
        tests only even function from lab4
        """

        func = lab4.only_even
        case1 = [1,2,3,4,5]
        expected1 = [2,4]
        self.assertEqual(func(case1), expected1)

if __name__ == '__main__':
    try:
        import lab4
        print ("lab4.py module found, testing")
        unittest.main()
    except ImportError:
        print ("Missing lab4.py module")
