def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    digit1 = a % 10
    digit2 = a // 10 % 10
    digit3 = a // 100
    sum = digit1 + digit2 + digit3
    result = sum % 2 == 1
    return result
print(main(152))
print(main(335))