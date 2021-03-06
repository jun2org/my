import re
from datetime import date

from lib.utils.number import is_integer

EIGHT_DIGIT_DATE_MIN = '00010101'


def parse_date(date_string):
    if date_string == '' or date_string is None:
        return date.min

    if is_yyyy_mm_dd(date_string):
        return convert_to_date_from_yyyy_mm_dd(date_string)

    if len(date_string) == 8:
        _8digit_date_string = date_string
    elif len(date_string) == 4:
        _8digit_date_string = convert_4digit_to_8digit(date_string)
    elif len(date_string) == 6:
        _8digit_date_string = convert_6digit_to_8digit(date_string)
    else:
        raise NotImplementedError()

    return convert_to_date_from_8digit(_8digit_date_string)


def is_yyyy_mm_dd(date_string: str) -> bool:
    return re.match('^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$', date_string) is not None


def convert_to_date_from_yyyy_mm_dd(date_string: str) -> date:
    splited_str = date_string.split('-')
    return date(year=int(splited_str[0]), month=int(splited_str[1]), day=int(splited_str[2]))


def convert_to_date_from_8digit(date_string: str) -> date:
    year = int(date_string[0:4])
    if year is 0:
        year = 1

    month = int(date_string[4:6])
    if month is 0:
        month = 1

    day = int(date_string[6:8])
    if day is 0:
        day = 1

    return date(year, month, day)


def convert_6digit_to_8digit(date_string: str) -> str:
    if not is_integer(date_string):
        return EIGHT_DIGIT_DATE_MIN

    _8digit_date_string = date_string
    if len(date_string) == 6:
        # There can be 6-digit data like 201707.
        # Do not do it correctly and go on trying to make an effort.
        # It seems to be safe until 2020. 200901 => 2009 / 01 /01 or 2020 / 09 / 01
        if 2000 <= int(date_string[0:4]) <= date.today().year:
            _8digit_date_string = date_string + '01'

        elif 2013 <= int(date_string[0:4]):
            _8digit_date_string = date_string + '01'

        elif 1913 <= int(date_string[0:4]):
            _8digit_date_string = date_string + '01'

        # There can be 6-digit data like 150906.
        # Do not do it correctly and go on trying to make an effort.
        # Add 2,000 in the first two places, and if it is bigger than the current date, it is a 20th century book.
        # It seems to be safe until this century (21st century).
        elif int(date_string[0:2]) + 2000 > date.today().year:
            _8digit_date_string = '19' + date_string

        else:
            _8digit_date_string = '20' + date_string

    return _8digit_date_string


def convert_4digit_to_8digit(date_string: str) -> str:
    if not is_integer(date_string):
        return EIGHT_DIGIT_DATE_MIN

    _date_string = date_string
    if len(_date_string) == 4:
        # There can be data with 4 digits like 2015
        # Do not do it correctly and go on trying to make an effort.
        _date_string = date_string + '0101'

    return _date_string
