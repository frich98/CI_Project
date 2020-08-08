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


def my_datetime(num_sec):
    """ This function takes an integer value that represents the number
    of seconds since the epoch: Jan 1, 1970. Function takes num_sec,
    converts it into a date, and returns it as a string with the following
    format: MM-DD-YYYY. num_sec will always be an int, num_sec will always
    be positive, and this function must be able to handle leap years."""

    # Figuring out number of days starting with EPOCH = 1
    num_sec_per_day = 24 * 60 * 60  # 1440 * 60 = 86,400
    if num_sec == 0:
        num_days = 1
    if not num_sec % num_sec_per_day == 0:
        num_days_int, num_days_dec = divmod(num_sec / num_sec_per_day, 1)
        num_days = int(num_days_int + 1)
    else:
        num_days = int(num_sec / num_sec_per_day)

    # ("\n Num Days: " + str(num_days))

    # List of # of days per year by year starting with 1970
    # need to handle up to year 9999 per Piazza post
    # cumulatively sum each consecutive year's # days in a new list
    list_years = range(1970, 9999 + 1)
    list_days_since_epoch_by_year = []
    for i in list_years:
        if leap_year_tf(i):
            list_days_since_epoch_by_year.append(366)
        else:
            list_days_since_epoch_by_year.append(365)
    cum_sum_list_days_by_year = \
        cum_sum_list(list_days_since_epoch_by_year)

    # finding closest year by finding min >= 0
    diff = [x - num_days for x in cum_sum_list_days_by_year]
    min_diff = min(i for i in diff if i >= 0)
    year_of_date = list_years[diff.index(min_diff)]

    # print("\n CumSum Year: " + (str(cum_sum_list_days_by_year)))
    # print("\n Diff Year: " + (str(diff)))

    # print("\n Year? " + str(year_of_date))
    # print("\n Leap Year? " + str(leap_year_tf(year_of_date)))
    # num_days_of_year = list_days_since_epoch_by_year[diff.index(min_diff)]

    # finding number of days that have elapsed in prior years
    if diff.index(min_diff) > 0:
        num_days_of_prior_years = \
            cum_sum_list_days_by_year[(diff.index(min_diff) - 1)]
    else:
        num_days_of_prior_years = 0

    # print("\n Number of days in prior years: " +
    # str(num_days_of_prior_years))

    # num days elapsed in current year
    num_days_in_actual_year = num_days - num_days_of_prior_years

    # days_in_month
    if leap_year_tf(year_of_date):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cum_sum_days_in_month = cum_sum_list(days_in_month)

    # print("\n Cum Sum Months: " + str(cum_sum_days_in_month))

    # finding closest month by finding min >= 0
    diff = [x - num_days_in_actual_year for x in cum_sum_days_in_month]
    min_diff = min(i for i in diff if i >= 0)
    month_of_date = diff.index(min_diff) + 1  # indexing starts at 0
    # num_days_of_month = days_in_month[diff.index(min_diff)]

    # finding days that have elapsed since month in question
    if diff.index(min_diff) > 0:
        num_days_prior_months = \
            cum_sum_days_in_month[(diff.index(min_diff) - 1)]
    else:
        num_days_prior_months = 0

    # print("\n Number of days in prior months: " + str(num_days_prior_months))

    # num days elapsed in current month = day of date
    day_of_date = num_days_in_actual_year - num_days_prior_months

    # formatting date and returning
    if num_sec == 0:
        return format_date(1, 1, 1970)
    elif num_sec == "":
        return None
    else:
        return format_date(month_of_date, day_of_date, year_of_date)


def format_date(mth, dy, yr):
    day_of_date = format_with_leading_zero(dy)
    month_of_date = format_with_leading_zero(mth)
    year_of_date = format_with_leading_zero(yr)
    date_value = month_of_date + "-"
    date_value = date_value + day_of_date + "-"
    date_value = date_value + year_of_date
    return date_value


def format_with_leading_zero(num):
    if num < 10:
        return "0" + str(int(num))
    else:
        return str(int(num))


def cum_sum_list(list_values):
    """Source: https://www.geeksforgeeks.org/
    python-program-to-find-cumulative-sum-of-a-list/"""
    cu_list = []
    length = len(list_values)
    cu_list = [sum(list_values[0:x:1]) for x in range(0, length + 1)]
    return cu_list[1:]


def leap_year_tf(yr):
    """Deciding if a year is a leap year or not.
    Source:https://www.timeanddate.com/date/leapyear.html"""
    if yr % 4 == 0 and yr % 100 == 0 and not yr % 400 == 0:
        return False
    elif yr % 4 == 0:
        return True
    else:
        return False
