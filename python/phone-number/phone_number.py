import re

class PhoneNumber:

    _pattern = re.compile(r'''
        ^\+?1?              # optional literal `+` and country code
        (?:[-. ]+)?         # optional separators
        \(?([2-9]\d{2})\)?  # the area code, with or without surrounding parens
        (?:[-. ]+)?         # optional separators
        ([2-9]\d{2})        # the exchange code
        (?:[-. ]+)?         # optional separators
        (\d{4})$            # the subscriber number
    ''', re.VERBOSE)

    def __init__(self, phone_number):
        self.phone_number = phone_number
        try:
            self.area_code, self.exchange_code, self.subscriber_code = \
                self._pattern.search(self.phone_number.strip()).groups()
        except AttributeError:
            raise ValueError("Invalid phone number")

    @property
    def number(self):
        return self.area_code + self.exchange_code + self.subscriber_code

    def pretty(self):
        #pretty(), "(223) 456-7890")
        return "({}) {}-{}".format(self.area_code, self.exchange_code, self.subscriber_code)
