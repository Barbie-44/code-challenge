from problems.utils.operations import get_length_of_object


class StringFrequency:
    """
    GOAL:
        - Calculate the frequency of target str into paragraph str.
    APPROACH:
        - Get the length of the paragraph.
        - Get the length of the target str.
        - Get the number of iterations based on.
         (length of paragraph - length of target + 1).
        - Stablish an int variable counter to zero.
        - Iterate through the paragraph's subtrings.
        - Update the counter each time a subparagraph is equal to target str.
    REMARKS:
        - Paragrah text is given.
        - You cannot use Python native functions like contains, in, find,
          refind, index, etc.
        - Only one target is required.
        - You must ALWAYS return an int or f-string: f"{int:result}
          ocurrencias encontradas".
    """

    def __init__(self, paragraph: str, target):
        self.paragraph = paragraph
        self.target = target

    def validate_data(self):
        return isinstance(self.target, str)

    def get_string_frequency(self):
        frequency = 0
        if not self.validate_data():
            return frequency
        paragraph_length, target_length = get_length_of_object(
            self.paragraph
        ), get_length_of_object(self.target)
        if not paragraph_length or not target_length:
            return frequency
        num_of_iterations = paragraph_length - target_length + 1
        start = 0
        while start < num_of_iterations:
            current_substr = self.paragraph[start : start + target_length]
            if current_substr == self.target:
                frequency += 1
            start += 1
        return frequency

    def get_result(self):
        frequency = self.get_string_frequency()
        return f"{frequency} ocurrencias encontradas."
