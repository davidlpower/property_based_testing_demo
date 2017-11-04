import unittest
from hypothesis import given, seed, example, note, strategies as st
from application.run_length_encoder import RunLengthEncoder


class TestEncoding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runLength = RunLengthEncoder()

    @given(s=st.text())
    def test_decode_inverts_encode(self, s):
        self.assertEqual(self.runLength.decode(self.runLength.encode(s)), s)


if __name__ == '__main__':
    unittest.main()
