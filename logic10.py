def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    result = a >= 10 and a <= 99
    return result
print(main(3))
print(main(12))