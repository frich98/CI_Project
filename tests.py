import unittest
import random
from task import conv_endian


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


if __name__ == '__main__':
    unittest.main()
