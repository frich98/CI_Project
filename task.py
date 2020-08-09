def is_negative(num_str):
    """Returns true if number in string is negative, false otherwise"""
    if num_str[0] == "-":
        return True
    else:
        return False


def is_hexadecimal(num_str):
    """Returns true if number in string is hexadecimal, false otherwise"""
    if not is_negative(num_str):
        if num_str[0:2].lower() == "0x":
            return True
    else:
        if num_str[1:3].lower() == "0x":
            return True
    return False


def is_float(num_str):
    """Returns true if number in string is a float, false otherwise"""
    if "." in num_str:
        return True
    else:
        return False


def convert_hexadecimal(num_str):
    """Converts a string with a hexadecimal into an integer"""
    start_index = 2
    if is_negative(num_str):
        start_index = 3

    valid_hex_chars = "0123456789ABCDEF"
    valid_hex_letters = "ABCDEF"

    hex_str = num_str.upper()
    hex_value = 0
    n = 0
    for i in range(len(hex_str) - 1, start_index - 1, -1):
        if not hex_str[i] in valid_hex_chars:
            return None
        else:
            if hex_str[i] in valid_hex_letters:
                index_value = ord(hex_str[i]) - 55
            else:
                index_value = ord(hex_str[i]) - 48
            hex_value += index_value * (16 ** n)
            n += 1
    if is_negative(num_str):
        hex_value *= -1
    return hex_value


def convert_float(num_str):
    """Converts a string with a float into an actual float"""
    start_index = 0
    if is_negative(num_str):
        start_index = 1

    float_value = 0.0
    dec_index = num_str.find(".")
    n = 0
    for i in range(dec_index - 1, start_index - 1, -1):
        if not num_str[i].isdigit():
            return None
        float_value += ((ord(num_str[i]) - 48) * (10 ** n))
        n += 1
    n = -1
    for j in range(dec_index + 1, len(num_str)):
        if not num_str[j].isdigit():
            return None
        float_value += ((ord(num_str[j]) - 48) * (10 ** (n)))
        n -= 1
    if is_negative(num_str):
        float_value *= -1
    return float_value


def convert_integer(num_str):
    """Converts a string with an integer into an actual integer"""
    start_index = 0
    if is_negative(num_str):
        start_index = 1

    int_value = 0
    n = 0
    for i in range(len(num_str) - 1, start_index - 1, -1):
        if not num_str[i].isdigit():
            return None
        else:
            int_value += ((ord(num_str[i]) - 48) * (10 ** n))
            n += 1
    if is_negative(num_str):
        int_value *= -1
    return int_value


def conv_num(num_str):
    """This function takes in a string and converts it into a base 10 number
    and returns it."""
    # If num_str is not a string
    if not type(num_str) == str:
        return None

    # If num_str doesn't have at least length 1
    if len(num_str) <= 0:
        return None

    # Convert string to number
    if is_hexadecimal(num_str):
        return convert_hexadecimal(num_str)
    elif is_float(num_str):
        return convert_float(num_str)
    else:
        return convert_integer(num_str)


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

    # Big Endian - flip contiguous hex symbols in blocks of two
    if endian == 'big':
        for i in range(len(hexadecimal_list) - 1, 0, -2):
            temp = hexadecimal_list[i - 1]
            hexadecimal += hexadecimal_list[i]
            hexadecimal += temp
            hexadecimal += ' '
        return hexadecimal.strip()
    # Little Endian - Flip contiguous hex symbols in blocks of two and reverse
    else:
        for i in range(0, len(hexadecimal_list), 2):
            temp = hexadecimal_list[i]
            hexadecimal += hexadecimal_list[i + 1]
            hexadecimal += temp
            hexadecimal += ' '
        return hexadecimal.strip()
