import unittest
import random
from task import conv_endian


class Test(unittest.TestCase):
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
