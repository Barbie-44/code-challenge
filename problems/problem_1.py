from problems.utils.operations import get_length_of_object


class StringFrequency:
    """
    GOAL:
        - Calculate the frequency of target str into paragraph str.
    APPROACH:
        - Get the length of the paragraph.
        - Get the length of the target str
        - Get the number of iterations based on
         (length of paragraph - length of target + 1)
        - Stablish an int variable counter to zero
        - Iterate through the paragraph's subtrings
        - Update the counter each time a subparagraph is equal to target str
    REMARKS:
        - Paragrah text is given.
        - You cannot use Python native functions.
        - Only one target is required.
        - You must ALWAYS return an int or f-string: f"{int:result}
          ocurrencias encontradas".

    POSSIBLE TEST CASES:
        - Target doesn't exists in input.
        - Validate input.
        - Validate string is not empty (length of string
            is different from zero)
        - Concatenated strings (Ex. logísticadeoperaciones).
        - target length > paragraph length
    """

    def __init__(
        self, paragraph: str, target: str, case_sensitive: bool = True
    ):
        self.paragraph = paragraph
        self.target = target

    def _get_length_of_str(self, input_string: str):
        length = 0
        while input_string[length:]:
            length += 1
        return length

    def get_string_frequency(self):
        paragraph_length, target_length = get_length_of_object(
            self.paragraph
        ), get_length_of_object(self.target)
        num_of_iterations = paragraph_length - target_length + 1
        frequency = 0
        start = 0
        while start < num_of_iterations:

            current_substr = self.paragraph[start : start + target_length]
            if current_substr == self.target:
                frequency += 1
            start += 1
        return print(f"{frequency} ocurrencias encontradas.")
