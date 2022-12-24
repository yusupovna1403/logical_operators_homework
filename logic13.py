def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    digit1 = a % 10
    digit2 = a // 10
    sum = digit1 + digit2
    result = sum % 2 == 0
    return result
print(main(35))
print(main(49))
    