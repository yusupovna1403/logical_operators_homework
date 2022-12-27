def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    num = a >= 10_000 and a <= 99_000
    return num
print(main(12345))
print(main(234))