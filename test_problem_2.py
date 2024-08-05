from input import data
from problems.problem_2 import ArrayProcessor


class TestArrayProcessor:
    def __init__(self) -> None:
        self.data = data
        self.operations = {
            "=": lambda x, y: x == y,
            "<=": lambda x, y: x <= y,
            ">=": lambda x, y: x >= y,
        }

    def _get_elements_with_criteria(self, entry, criteria):
        result = True
        for condition in criteria:
            variable = condition[0]
            operator = condition[1]
            value = condition[2]
            if not self.operations[operator](entry[variable], value):
                result = False
        return result

    def test_base_case(self):
        criteria = [("weight", "=", 3)]

        frequency = 0
        for element in self.data:
            if self._get_elements_with_criteria(element, criteria):
                frequency += 1
        result_class = ArrayProcessor(self.data, criteria)
        result = result_class.get_sorted_array()
        for i in range(frequency):
            assert result[i]["weight"] == 3

    def test_multiple_criteria(self):
        criteria2 = [("weight", ">=", 2), ("length", "<=", 20)]
        frequency = 0
        for element in self.data:
            if self._get_elements_with_criteria(element, criteria2):
                frequency += 1
        result_class = ArrayProcessor(self.data, criteria2)
        result = result_class.get_sorted_array()
        for i in range(frequency):
            assert result[i]["weight"] >= 2
            assert result[i]["length"] <= 20

    def test_empty_criteria(self):
        result_class = ArrayProcessor(self.data, [])
        result = result_class.get_sorted_array()
        assert self.data == result

    def test_invalid_criteria(self):
        criteria = [("cost", "==", 125)]
        result_class = ArrayProcessor(self.data, criteria)
        result = result_class.get_sorted_array()
        assert self.data == result

    def test_invalid_operator(self):
        criteria = [("cost", ">>", 125)]
        result_class = ArrayProcessor(self.data, criteria)
        result = result_class.get_sorted_array()
        assert self.data == result

    def run_all_test_cases(self):
        try:
            self.test_base_case()
            self.test_multiple_criteria()
            self.test_empty_criteria()
            self.test_invalid_criteria()
            self.test_invalid_operator()
        except Exception as e:
            return e


test_result = TestArrayProcessor()
test_result.run_all_test_cases()
