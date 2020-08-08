import unittest
import random
# import datetime  # will use eventually
from task import conv_endian
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

    # Function 2 - simple test 1
    def test1_function2(self):
        self.assertEqual(my_datetime(86486400), "09-27-1972")

    # Function 2 - simple test 2
    def test2_function2(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    # Function 2 - simple test 3
    def test3_function2(self):
        self.assertEqual(my_datetime(0), "01-01-1970")


if __name__ == '__main__':
    unittest.main()
