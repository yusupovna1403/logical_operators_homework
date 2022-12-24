def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    digit1 = a % 10
    digit2 = a // 10
    sum = digit1 + digit2
    result = sum % 2 == 1
    return result
print(main(45))
print(main(35))