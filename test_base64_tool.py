import unittest
from base64_tool import encode_base64, decode_base64, parse_mode

class TestBase64Tool(unittest.TestCase):

    # --- Tests Noyau Métier ---

    def test_encode_simple_text(self):
        self.assertEqual(encode_base64("Hello World"), "SGVsbG8gV29ybGQ=")

    def test_decode_simple_base64(self):
        self.assertEqual(decode_base64("SGVsbG8gV29ybGQ="), "Hello World")

    def test_decode_with_internal_newlines_and_spaces(self):
        multiline_b64 = "SGVs\nbG8g\r\nV29ybGQ=\n"
        self.assertEqual(decode_base64(multiline_b64), "Hello World")

    def test_decode_invalid_base64_raises_value_error(self):
        with self.assertRaises(ValueError):
            decode_base64("Invalid!Base64Payload###")

    def test_decode_non_utf8_payload_raises_value_error(self):
        non_utf8_b64 = "//8="
        with self.assertRaises(ValueError):
            decode_base64(non_utf8_b64)

    # --- Tests Parser CLI ---

    def test_parse_mode_returns_none_when_empty(self):
        self.assertIsNone(parse_mode([]))

    def test_parse_mode_detects_encode(self):
        self.assertEqual(parse_mode(["-e"]), "encode")
        self.assertEqual(parse_mode(["--encode"]), "encode")

    def test_parse_mode_detects_decode(self):
        self.assertEqual(parse_mode(["-d"]), "decode")
        self.assertEqual(parse_mode(["--decode"]), "decode")

    def test_parse_mode_accepts_redundant_flags(self):
        self.assertEqual(parse_mode(["-d", "--decode"]), "decode")

    def test_parse_mode_raises_on_unknown_arg(self):
        with self.assertRaises(ValueError):
            parse_mode(["--foo"])

    def test_parse_mode_raises_on_conflicting_args(self):
        with self.assertRaises(ValueError):
            parse_mode(["-e", "-d"])


if __name__ == "__main__":
    unittest.main()
