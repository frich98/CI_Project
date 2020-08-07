import unittest
import random
import datetime
from task import conv_endian
from task import my_datetime


class TestCase(unittest.TestCase):

    # Testing Big Endian
    def test1_function3(self):
        for i in range(0, 1000):
            decimal = random.randint(1, 999999)
            big_hex = hex(decimal)[2:].upper()
            if len(big_hex) % 2 == 1:
                big_hex = '0' + big_hex
            big_hex = ' '.join(big_hex[i:i + 2]
                               for i in range(0, len(big_hex), 2))
            self.assertEqual(conv_endian(decimal, 'big'), big_hex)

    # Simple check for first merge
    def test1_function2(self):
        expected = "09-27-1972"
        self.assertEqual(my_datetime(1441*1000), expected)


if __name__ == '__main__':
    unittest.main()
