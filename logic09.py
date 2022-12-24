def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    result = a % 2 == 1 or b % 2 == 1
    return result
print(main(3 , 6))
print(main(4 , 6))