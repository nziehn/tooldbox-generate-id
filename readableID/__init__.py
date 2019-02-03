import math
import logging

logger = logging.getLogger(__name__)

DEFAULT_CHARSET = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
DEFAULT_CHARSET_LOWER = DEFAULT_CHARSET.lower()
DEFAULT_MINIMAL_LENGTH = 4
DEFAULT_PRIME = 2000177
DEFAULT_XOR = 674223


class ReadableID(object):
    def __init__(self, charset=DEFAULT_CHARSET, min_length=DEFAULT_MINIMAL_LENGTH, prime=DEFAULT_PRIME, xor=DEFAULT_XOR):
        self.charset = charset
        self.min_length = min_length
        self.prime = prime
        self.xor = xor
        charset_power = math.log(len(charset), 2)

        if charset_power - math.floor(charset_power) > 0:
            raise ValueError('Charset length must be power of 2!')

        if xor > pow(len(charset), min_length):
            logger.warning('choice of xor will produce ids longer than min_length!')

    def generate_id(self, idx):
        idx = idx ^ self.xor
        required_chars_for_idx = math.log(idx + 1, len(self.charset))
        required_chars = int(math.ceil(max(self.min_length, required_chars_for_idx)))
        modulo = 1 << int(math.ceil(required_chars * math.log(len(self.charset), 2)))
        value = (self.prime * idx) % modulo

        result = ''
        for _ in range(required_chars):
            c_idx = value % len(self.charset)
            result += self.charset[int(c_idx)]
            value = (value - c_idx) / len(self.charset)

        return result
