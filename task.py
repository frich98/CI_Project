def conv_num(num_str):
    """This function takes in a string and converts it into a base 10 number and returns it."""
    # If num_str is not a string
    if not type(num_str) == str:
        return None

    # If num_str doesn't have at least length 1
    if len(num_str) <= 0:
        return None

    neg_num = False
    hex_num = False
    float_num = False

    # See if negative
    if num_str[0] == "-":
        neg_num = True

    # See if hexadecimal
    if not neg_num:
        if num_str[0:2].lower() == "0x":
            hex_num = True
    else:
        if num_str[1:3].lower() == "0x":
            hex_num = True

    # See if float
    if "." in num_str:
        float_num = True

    # Set index for positive or negative
    start_index = 0
    if neg_num:
        start_index = 1

    # If hexadecimal
    valid_hex_chars = "0123456789ABCDEF"
    valid_hex_letters = "ABCDEF"
    if hex_num:
        start_index += 2
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
        if neg_num:
            hex_value *= -1
        return hex_value

    # If float
    if float_num:
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
        if neg_num:
            float_value *= -1
        return float_value

    # If integer
    int_value = 0
    n = 0
    for i in range(len(num_str) - 1, start_index - 1, -1):
        if not num_str[i].isdigit():
            return None
        else:
            int_value += ((ord(num_str[i]) - 48) * (10 ** n))
            n += 1
    if neg_num:
        int_value *= -1
    return int_value


def conv_endian(num, endian='big'):
    """Accepts an int value as num, converts and returns it as a
    hexadecimal string"""
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

    # Split hex symbols into a list
    hexadecimal_list = list(hexadecimal)

    # Re-initialize hex string as positive or negative
    if positive:
        hexadecimal = ""
    else:
        hexadecimal = "-"

    # Flip contiguous symbols in blocks of two
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
