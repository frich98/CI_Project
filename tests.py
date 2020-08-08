import unittest
import random
from task import conv_endian


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
            big_hex = ' '.join(big_hex[i:i + 2] for i in range(0, len(big_hex), 2))
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
            little_hex = ' '.join(little_hex[i:i + 2] for i in range(len(little_hex), -1, -2)).strip()
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
            self.assertEqual(conv_endian(num, endian='little'), numbers.get(num))

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
        self.assertEqual(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    # Invalid conversions
    def test9_function3(self):
        numbers = {777: '0309', -777: '03 09', 1020: '03 FC ', -1020: ' -03 FC'}
        for num in numbers:
            self.assertNotEqual(conv_endian(num, 'big'), numbers.get(num))

    # Check return None
    def test10_function3(self):
        self.assertEqual(conv_endian(num=-954786, endian='Little'), 'None')

    # Check return None
    def test11_function3(self):
        numbers = {-1: "-01", 0: "00", 1: "01"}
        for num in numbers:
            self.assertEqual(conv_endian(num, 'Big'), 'None')
