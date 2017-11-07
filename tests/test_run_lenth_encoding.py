# test_math.py
from parameterized import parameterized
from application.run_length_encoder import RunLengthEncoder

import unittest


class TestEncoding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runLength = RunLengthEncoder()

    @parameterized.expand([
        ("single char", 'a'),
        ("duplicate chars", 'aaa'),
        ("multiple chars", 'abc'),
        ("single special chars", '('),
        ("duplicate special chars", '(('),
        ("multiple special chars", '(&#'),
    ])
    def test_decode_inverts_encode(self, name, input):
        self.assertEqual(self.runLength.decode(self.runLength.encode(input)), input)


if __name__ == '__main__':
    unittest.main()
