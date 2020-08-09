def conv_endian(num, endian='big'):
    """Accepts an int value as num, converts and returns it as a
    hexadecimal string"""

    # Check if valid endian
    if endian != 'big' and endian != 'little':
        return "None"

    # Check for 0 value
    if num == 0:
        return "00"

    # Check if number is positive
    positive = bool(num > 0)
    num = abs(num)

    # Dictionary for integer (10 thru 15) to corresponding hex symobl
    hex_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = ""
    result = num

    # Compute decimal base 10 number to hex
    while result > 0:
        remainder = result % 16
        if remainder >= 10:
            hexadecimal += hex_letters.get(remainder)
        else:
            hexadecimal += str(remainder)
        result = int(result / 16)

    # Add 0 if odd number of hex symbols to have 2 characters per byte
    if len(hexadecimal) % 2 == 1:
        hexadecimal += '0'

    # Split hex symbols into a list
    hexadecimal_list = list(hexadecimal)

    # Re-initialize hex string as positive or negative
    if positive:
        hexadecimal = ""
    else:
        hexadecimal = "-"

    # Big Endian - flip contiguous hex symbols in blocks of two and reverse
    if endian == 'big':
        for i in range(len(hexadecimal_list) - 1, 0, -2):
            temp = hexadecimal_list[i - 1]
            hexadecimal += hexadecimal_list[i]
            hexadecimal += temp
            hexadecimal += ' '
        return hexadecimal.strip()
    # Little Endian - Flip contiguous hex symbols in blocks of two
    else:
        for i in range(0, len(hexadecimal_list), 2):
            temp = hexadecimal_list[i]
            hexadecimal += hexadecimal_list[i + 1]
            hexadecimal += temp
            hexadecimal += ' '
        return hexadecimal.strip()
