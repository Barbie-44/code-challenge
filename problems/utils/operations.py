def get_length_of_object(input_object):
    """
    This function is implemented in order to avoid built-in len() function.
    """
    length = 0
    while input_object[length:]:
        length += 1
    return length
