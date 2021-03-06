import re
import math
import testutils

# Parses a string that represents either decimal or sexagesimal
# degrees into a decimal degrees value.  Returns None if invalid.
#
# Valid strings:
#    decimal degrees: -19.234    25.6  (just a regular float number without exponents)
#
#    sexagesimal degrees:
#    15d
#    15d30m
#    15d30m6s
#    all the above can be negative as well.  All need to end in either of d/m/s.

def parse_degrees (value):
    decimal_re = re.compile (r"^[-+]?\d*\.?\d+$")
    if decimal_re.match (value):
        return float(value)

    sexagesimal_re = re.compile (r"^([-+]?\d+)d((\d+)m((\d+)s)?)?$")
    m = sexagesimal_re.match (value)

    if m == None:
        return None

    (deg, min, sec) = m.group (1, 3, 5)

    deg = float (deg)

    if min == None:
        min = 0.0
    else:
        min = float(min)

    if sec == None:
        sec = 0.0
    else:
        sec = float(sec)

    decimals = min / 60.0 + sec / 3600.0

    if deg < 0:
        return deg - decimals
    else:
        return deg + decimals

def parse_degrees_value (value):
    if isinstance(value, str):
        return parse_degrees (value)
    elif isinstance(value, float):
        return value
    else:
        raise ValueError ("value must be a float or a string")

########## tests ##########


class TestParseDegrees (testutils.TestCaseHelper):
    def test_parse_degrees_deals_with_invalid_values (self):
        self.assertIsNone (parse_degrees (""))
        self.assertIsNone (parse_degrees (" "))
        self.assertIsNone (parse_degrees ("19.5d"))
        self.assertIsNone (parse_degrees ("19dms"))

    def test_parse_degrees_deals_with_decimal_degrees (self):
        self.assertFloatEquals (parse_degrees ("19"), 19)
        self.assertFloatEquals (parse_degrees ("-19"), -19)
        self.assertFloatEquals (parse_degrees ("19.5"), 19.5)
        self.assertFloatEquals (parse_degrees ("-19.5"), -19.5)

    def test_parse_degrees_deals_with_sexagesimal_degrees (self):
        self.assertFloatEquals (parse_degrees ("19d"), 19.0)
        self.assertFloatEquals (parse_degrees ("-19d"), -19.0)
        self.assertFloatEquals (parse_degrees ("19d30m"), 19.5)
        self.assertFloatEquals (parse_degrees ("-19d30m"), -19.5)
        self.assertFloatEquals (parse_degrees ("19d20m15s"), 19 + 20.0 / 60 + 15.0 / 3600)
        self.assertFloatEquals (parse_degrees ("-19d20m15s"), -(19 + 20.0 / 60 + 15.0 / 3600))

    def test_parse_degrees_can_parse_float_value (self):
        self.assertFloatEquals (parse_degrees_value (19.5), 19.5)

    def test_parse_degrees_can_parse_string_value (self):
        self.assertFloatEquals (parse_degrees_value ("-19d30m"), -19.5)
