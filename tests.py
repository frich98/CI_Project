import unittest
import random
import datetime
from task import conv_endian
from task import conv_num
from task import my_datetime


class Test(unittest.TestCase):
    # Testing Big Endian
    def test1_function3(self):
        for i in range(0, 10000):
            decimal = random.randint(-999999, 999999)
            negative = bool(decimal < 0)
            num = abs(decimal)
            big_hex = hex(num)[2:].upper()
            if len(big_hex) % 2 == 1:
                big_hex = '0' + big_hex
            big_hex = ' '.join(big_hex[i:i + 2]
                               for i in range(0, len(big_hex), 2))
            if negative:
                big_hex = '-' + big_hex
            self.assertEqual(conv_endian(decimal, 'big'), big_hex)

    # Testing Little Endian
    def test2_function3(self):
        for i in range(0, 10000):
            decimal = random.randint(-999999, 999999)
            negative = bool(decimal < 0)
            num = abs(decimal)
            little_hex = hex(num)[2:].upper()
            if len(little_hex) % 2 == 1:
                little_hex = '0' + little_hex
            little_hex = ' '.join(
                little_hex[i:i + 2]
                for i in range(len(little_hex), -1, -2)).strip()
            if negative:
                little_hex = '-' + little_hex
            self.assertEqual(conv_endian(decimal, 'little'), little_hex)

    # Random Tests - Big Endian
    def test3_function3(self):
        numbers = {-1: "-01", 0: "00", 1: "01"}
        for num in numbers:
            self.assertEqual(conv_endian(num, endian='big'), numbers.get(num))

    # Random Tests - Little Endian
    def test4_function3(self):
        numbers = {-1: "-01", 0: "00", 1: "01"}
        for num in numbers:
            self.assertEqual(
                conv_endian(
                    num,
                    endian='little'),
                numbers.get(num))

    # Instructor examples
    def test5_function3(self):
        numbers = {954786: '0E 91 A2', -954786: '-0E 91 A2'}
        for num in numbers:
            self.assertEqual(conv_endian(num), numbers.get(num))

    # Instructor examples
    def test6_function3(self):
        numbers = {954786: 'A2 91 0E', -954786: '-A2 91 0E'}
        for num in numbers:
            self.assertEqual(conv_endian(num, 'little'), numbers.get(num))

    # Instructor example
    def test7_function3(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    # Instructor example
    def test8_function3(self):
        self.assertEqual(
            conv_endian(
                num=-954786,
                endian='little'),
            '-A2 91 0E')

    # Invalid conversions
    def test9_function3(self):
        numbers = {777: '0309', -777: '03 09',
                   1020: '03 FC ', -1020: ' -03 FC'}
        for num in numbers:
            self.assertNotEqual(conv_endian(num, 'big'), numbers.get(num))

    # Check return None
    def test10_function3(self):
        self.assertEqual(conv_endian(num=-954786, endian='Little'), None)

    # Check return None
    def test11_function3(self):
        numbers = {-1: "-01", 0: "00", 1: "01"}
        for num in numbers:
            self.assertEqual(conv_endian(num, 'Big'), None)

    # Function 2 - checking origin
    def test1_function2(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    # Function 2 - random tests
    # NOTE THAT WINDOWS SYSTEMS HAVE YEAR DATE LIMIT, ~ 2038
    # NEED TO RUN THESE TESTS ON LINUX SYSTEM TO HAVE THEM WORK
    # PROPERLY.
    def test2_function2(self):
        num_tests = 500  # function not very efficient, takes awhile
        for i in range(0, num_tests):
            # year 9999, last second in year
            num = random.randint(0, 253402300799)
            # print("\n" + "Iteration: " + str(i) + ", Rand Num: " + str(num))
            calculated_date = my_datetime(num)
            actual_date = \
                datetime.datetime.utcfromtimestamp(num).strftime("%m-%d-%Y")
            # print(datetime.datetime.fromtimestamp(num))
            # print(", Calculated Date: " + calculated_date
            # + ", Actual Date: " + actual_date)
            self.assertEqual(calculated_date, actual_date)

    # Function 2 - example test1
    def test3_function2(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    # Function 2 - example test2
    def test4_function2(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    # Function 2 - example test1
    def test3_function2a(self):
        self.assertEqual(my_datetime(975539265), "11-29-2000")

    # Function 2 - example test2
    def test4_function2a(self):
        self.assertEqual(my_datetime(16755980865), "12-22-2500")

    # Function 2 - extremity testing 1
    def test5_function2(self):
        self.assertEqual(my_datetime(253370764801), "01-01-9999")

    # Function 2 - extremity testing 2
    def test6_function2(self):
        self.assertEqual(my_datetime(253402300799), "12-31-9999")

    # Testing Convert Number
    def test01_function1(self):
        num_str = "12345"
        expected = 12345
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test02_function1(self):
        num_str = "-12345"
        expected = -12345
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test03_function1(self):
        num_str = "-123.45"
        expected = -123.45
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test04_function1(self):
        num_str = ".45"
        expected = 0.45
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test05_function1(self):
        num_str = "-.45"
        expected = -0.45
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test06_function1(self):
        num_str = "123."
        expected = 123.0
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test07_function1(self):
        num_str = "-123."
        expected = -123.0
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test08_function1(self):
        num_str = "0xAD4"
        expected = 2772
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test09_function1(self):
        num_str = "0XAD4"
        expected = 2772
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test10_function1(self):
        num_str = "0xad4"
        expected = 2772
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test11_function1(self):
        num_str = "0XaD4"
        expected = 2772
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test12_function1(self):
        num_str = "-0xAD4"
        expected = -2772
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test13_function1(self):
        num_str = "12.3.45"
        expected = None
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test14_function1(self):
        num_str = "0xAZ4"
        expected = None
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test15_function1(self):
        num_str = "12345A"
        expected = None
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test16_function1(self):
        num_str = ""
        expected = None
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test17_function1(self):
        num_str = 12345
        expected = None
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))

    def test18_function1(self):
        num_str = 1.2
        expected = None
        self.assertEqual(conv_num(num_str), expected)
        self.assertEqual(type(conv_num(num_str)), type(expected))


if __name__ == '__main__':
    unittest.main()
