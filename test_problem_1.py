from input import paragraph
from problems.problem_1 import StringFrequency
import random
import string


class TestStringFrequency:
    def __init__(self):
        self.paragraph = paragraph
        self.target = "logística"
        self.random_string = "".join(
            random.choice(string.ascii_lowercase) for i in range(10)
        )
        self.zero_matches = "0"

    def test_base_case(self):
        case = StringFrequency(self.paragraph, self.target)
        expected = self.paragraph.count(self.target)
        assert (
            f"{expected} ocurrencias encontradas."
            == case.get_string_frequency()
        )

    def test_target_not_in_paragraph(self):
        case = StringFrequency(self.paragraph, self.random_string)
        assert self.zero_matches == case.get_string_frequency()[0]

    def test_empty_target_case(self):
        case = StringFrequency(self.paragraph, "")
        assert self.zero_matches == case.get_string_frequency()[0]

    def test_empty_paragraph_case(self):
        case = StringFrequency("", self.target)
        assert self.zero_matches == case.get_string_frequency()[0]

    def test_space_str_case(self):
        case = StringFrequency(self.paragraph, " ")
        expected = self.paragraph.count(" ")
        assert (
            f"{expected} ocurrencias encontradas."
            == case.get_string_frequency()
        )

    def test_validate_target_type(self):
        case = StringFrequency(self.paragraph, 123)
        assert "Tipo de dato inválido." == case.get_string_frequency()

    def run_all_test_cases(self):
        try:
            self.test_base_case()
            self.test_target_not_in_paragraph()
            self.test_empty_target_case()
            self.test_empty_paragraph_case()
            self.test_space_str_case()
            self.test_validate_target_type()
        except Exception as e:
            return e


test_result = TestStringFrequency()
test_result.run_all_test_cases()
