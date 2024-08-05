from problems.problem_1 import StringFrequency
from problems.problem_2 import ArrayProcessor
from input import paragraph, target
from input import data


def main():
    """
    These are only the example test cases, more cases are included in tests
    files.
    """
    problem_num = eval(
        input("Enter a the number of a problem to solve (1 or 2): ")
    )
    output = None
    if problem_num == 1:
        frequency = StringFrequency(paragraph, target)
        output = frequency.get_result()
    if problem_num == 2:
        ordered_array = ArrayProcessor(data, [("weight", "=", 3)])
        output = ordered_array.get_sorted_array()
    print(output)
    return output


if __name__ == "__main__":
    main()
