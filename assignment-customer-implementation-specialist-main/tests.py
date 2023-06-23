import unittest
import subprocess


IMPLEMENTATION_SCRIPT = "luhn.py"

class TestLuhn(unittest.TestCase):
    def test_single_digit_strings_can_not_be_valid(self):
        self.run_test_case("1", 42)

    def test_a_single_zero_is_invalid(self):
        self.run_test_case("0", 42)

    def test_a_simple_valid_SIN_that_remains_valid_if_reversed(self):
        self.run_test_case("059", 0)

    def test_a_simple_valid_SIN_that_becomes_invalid_if_reversed(self):
        self.run_test_case("59", 0)

    def test_a_valid_Canadian_SIN(self):
        self.run_test_case("055 444 285", 0)

    def test_invalid_Canadian_SIN(self):
        self.run_test_case("055 444 286", 42)

    def test_invalid_credit_card(self):
        self.run_test_case("8273 1232 7352 0569", 42)

    def test_valid_number_with_an_odd_number_of_digits(self):
        self.run_test_case("095 245 88", 0)

    def test_valid_number_with_an_even_number_of_digits(self):
        self.run_test_case("234 567 891 234", 0)

    def test_valid_strings_with_a_non_digit_added_at_the_end_invalid(self):
        self.run_test_case("059a", 42)

    def test_valid_strings_with_punctuation_included_become_invalid(self):
        self.run_test_case("055-444-285", 42)

    def test_valid_strings_with_symbols_included_become_invalid(self):
        self.run_test_case("055# 444$ 285", 42)

    def test_single_zero_with_space_is_invalid(self):
        self.run_test_case(" 0", 42)

    def test_more_than_a_single_zero_is_valid(self):
        self.run_test_case("0000 0", 0)

    def test_input_digit_9_is_correctly_converted_to_output_digit_9(self):
        self.run_test_case("091", 0)

    def test_using_ascii_value_for_non_doubled_non_digit_isnt_allowed(self):
        self.run_test_case("055b 444 285", 42)

    def test_using_ascii_value_for_doubled_non_digit_isnt_allowed(self):
        self.run_test_case(":9", 42)

    def run_test_case(self, input, expected):
        result = subprocess.run(
            ["python3", IMPLEMENTATION_SCRIPT],
            text=True,
            input=input,
            capture_output=True,
        )
        self.assertIn(
            result.returncode,
            [0, 42],
            f"Invalid exit code {result.returncode} with input {input}!",
        )
        self.assertEqual(
            result.returncode,
            expected,
            f'Input: "{input}", Status: {result.returncode}, Expected: {expected}',
        )


if __name__ == "__main__":
    unittest.main()
