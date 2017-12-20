import unittest
from hypothesis import given, seed, example, note, strategies as st
from application.run_length_encoder import RunLengthEncoder


class TestEncoding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runLength = RunLengthEncoder()

    @given(input=st.text())
    def test_decode_inverts_encode(self, input):
        self.assertEqual(self.runLength.decode(self.runLength.encode(input)), input)
