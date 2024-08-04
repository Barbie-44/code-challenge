from input import data
from typing import List
from utils import get_length_of_object


class ArrayProcessor:
    """
    GOAL:
        - Order an array according to priority (descending order) for elements
          that match a criteria.
    APPROACH:
        - Check the length of data array and criteria inputs
        - Check which items satisfy ALL criteria conditions and append them to
          top items array.
        - Append the rest of the items to last_items array.
        - Sort the items in top_items array according to priority property
          (descending order)
    REMARKS:
        - Array and criteria are given
        - The array or criteria might be empty
        - You can't use python native funcs.
        - Criteria array might contain more than one condition.
          Ex. criteria2 = [('width', '=', 2), ('length', '<=', 20)]
    """

    def __init__(self, input_array: List, criteria: List):
        self.input_array = input_array
        self.criteria = criteria
        self.operations = {
            "=": lambda x, y: x == y,
            "<=": lambda x, y: x <= y,
            ">=": lambda x, y: x >= y,
        }

    def _check_criteria(self, item):
        satisfies_conditions = True
        len_of_criteria = get_length_of_object(self.criteria)
        for i in range(len_of_criteria):
            if not satisfies_conditions:
                break
            curr_criteria = self.criteria[i]
            param = curr_criteria[0]
            operator = curr_criteria[1]
            expected_value = curr_criteria[2]
            if not self.operations[operator](item[param], expected_value):
                satisfies_conditions = False
        return satisfies_conditions

    def get_items(self):
        top_items = []
        last_items = []
        len_input_array = get_length_of_object(self.input_array)
        for i in range(len_input_array):
            curr_item = self.input_array[i]
            satisfies_conditions = self._check_criteria(curr_item)
            if satisfies_conditions:
                top_items += curr_item
                continue
            last_items.append(curr_item)
        return top_items, last_items

    def sort_top_items(self, arr: List):
        lenght_of_arr = get_length_of_object(arr)
        if lenght_of_arr > 1:
            middle_term = lenght_of_arr // 2
            left_chunk = arr[:middle_term]
            right_chunk = arr[middle_term:]

            self.sort_top_items(left_chunk)
            self.sort_top_items(right_chunk)

            i = j = k = 0
            len_left_chunk = get_length_of_object(left_chunk)
            len_right_chunk = get_length_of_object(right_chunk)
            while i < len_left_chunk and j < len_right_chunk:
                left_priority = left_chunk[i]["priority"]
                right_priority = right_chunk[j]["priority"]
                if left_priority >= right_priority:
                    arr[k] = left_chunk[i]
                    i += 1
                else:
                    arr[k] = right_chunk[j]
                    j += 1
                k += 1

            while i < len_left_chunk:
                arr[k] = left_chunk[i]
                i += 1
                k += 1

            while j < len_right_chunk:
                arr[k] = right_chunk[j]
                j += 1
                k += 1
        return arr

    def get_sorted_array(self):
        top_items, last_items = self.get_items()
        final_result = self.sort_top_items(top_items) + last_items
        return final_result


final_arr = ArrayProcessor(data, [("weight", "=", 3)])
print(final_arr.get_sorted_array())
