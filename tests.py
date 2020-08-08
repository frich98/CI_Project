import unittest
import random
import datetime
from task import conv_endian
from task import conv_num
from task import my_datetime


class TestCase(unittest.TestCase):
    # Testing Big Endian
    def test1_function3(self):
        for i in range(0, 1000):
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

    # Function 2 - checking origin
    def test1_function2(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    # Function 2 - random tests
    def test2_function2(self):
        num_tests = 100
        for i in range(0, num_tests):
            num = random.randint(0, 9999*24*60*60)
            # print("\n" + "Iteration: " + str(i) + ", Rand Num: " + str(num))
            calculated_date = my_datetime(num)
            actual_date = \
                datetime.datetime.utcfromtimestamp(num).strftime("%m-%d-%Y")
            # print(datetime.datetime.fromtimestamp(num))
            # print(", Calculated Date: " + calculated_date
            # + ", Actual Date: " + actual_date)
            self.assertEqual(calculated_date, actual_date)

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
