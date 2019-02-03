import os
import unittest
from nose import tools as _tools

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


def test_backwards_compatibility():
    knowns = [
        {
            'params': {'prime': 3},
            'data': {
                0: 'PJZ7',
                1824: 'P747',
                74991: 'A8TE',
                9528658492615: '2BJQP2893',
            }
        },
        {
            'params': {'xor': 3},
            'data': {
                0: 'V6DZ',
                1824: 'VFDB',
                74991: 'NKM7',
                9528658492615: 'ENPQDBH2Q',
            }
        },
        {
            'params': {'min_length': 3, 'xor': 0},
            'data': {
                0: 'AAA',
                1824: 'AK9',
                74991: '9FRW',
                9528658492615: 'ZJTFKBH2Q',
            }
        },
        {
            'params': {'charset': 'ABCD4567', 'xor': 123},
            'data': {
                0: 'DBC7',
                1824: 'D557',
                74991: '4CBC6B',
                9528658492615: '4775A6ACBA7A45D',
            }
        }
    ]
    for known in knowns:
        params = known['params']
        data = known['data']
        uut = _uut(**params)

        for idx, expected in data.items():
            _tools.assert_equal(expected, uut.generate_id(idx))