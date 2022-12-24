def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    result = a % 2 == 0 or b % 2 == 0
    return result
print(main(3 , 6))
print(main(1 , 7))