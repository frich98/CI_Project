import unittest
import random
# import datetime  # will use eventually
from task import conv_endian
from task import my_datetime


class Test(unittest.TestCase):
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

    # Simple check for first merge
    def test1_function2(self):
        expected = "09-27-1972"
        self.assertEqual(my_datetime(1441*1000), expected)


if __name__ == '__main__':
    unittest.main()
