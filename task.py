def conv_endian(num, endian = 'big'):
    """Accepts an int value as num, converts and returns it as a
    hexadecimal string number"""
    positive = bool(num >= 0)
    num = abs(num)

    hex_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = ""
    result = num
    while result > 0:
        remainder = result % 16
        if remainder >= 10:
            hexadecimal += hex_letters.get(remainder)
        else:
            hexadecimal += str(remainder)
        result = int(result / 16)
    # Add 0 if odd number of hex symbols
    if len(hexadecimal) % 2 == 1:
        hexadecimal += '0'

    # Flip contiguous hex symbols in blocks of 2
    hexadecimal_list = list(hexadecimal)

    # initialize hex string as positive or negative
    if not positive:
        hexadecimal = "-"
    else:
        hexadecimal = ""

    if endian == 'big':
        for i in range(len(hexadecimal_list) - 1, 0, -2):
            temp = hexadecimal_list[i - 1]
            hexadecimal += hexadecimal_list[i]
            hexadecimal += temp
            hexadecimal += ' '
        return hexadecimal.strip()
    elif endian == 'little':
        for i in range(0, len(hexadecimal_list), 2):
            temp = hexadecimal_list[i]
            hexadecimal += hexadecimal_list[i + 1]
            hexadecimal += temp
            hexadecimal += ' '
        return hexadecimal.strip()
    else:
        return "None"
