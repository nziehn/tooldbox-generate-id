import os
import unittest

from readableID import ReadableID as _uut


SLOW_TESTS = os.environ.get('SLOW_TESTS', False)


@unittest.skipUnless(SLOW_TESTS, "slow test")
def test_duplicates():
    existing_values = set()
    generator = _uut()
    number_of_values_to_check = 2 << 24
    for idx in range(number_of_values_to_check):
        new_val = generator.generate_id(idx)
        if new_val in existing_values:
            raise ValueError('FOUND DUPLICATE')

        existing_values.add(idx)

        if idx % int(number_of_values_to_check / 100) == 0:
            print('checked {}% of values, no duplicates so far!'.format(
                round(len(existing_values) * 100 / number_of_values_to_check))
            )

    print('generated {} unique values!!'.format(len(existing_values)))