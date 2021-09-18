# #define a function that takes the year
# def is_leap_year(year):
#     # All leap years are divisible by 4
#     if year % 4 == 0:
#     # but not by 100 unless also divisible by 400
#     # (this is why the year 2000 was a leap year)
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def is_leap_year(year):
#     print("refactored function")
#     if year % 4 == 0:
#         if year % 100 == 0 and not year % 400 == 0:
#             return False
#         return True
#     return False

def is_leap_year(year):
    return year % 4 == 0 and not (
        year % 100 == 0 and not year % 400 == 0
        )

# BREAKING UP TOO LONG LINES FOR PEP8

# from test import (
#     test_view, test_leap_year, test_view,
#     test_leap_year, test_view, test_leap_year
#     )


too_long_string = ("This is a very long string that will definitely "
                   "need to be broken up for PEP8 guidelines")

second_string = "Another very long string to break up for PEP8 guidelines, \
so let's try this!"


print(second_string)
