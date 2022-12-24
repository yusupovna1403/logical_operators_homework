def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    digit1 = a % 10
    digit2 = a // 10 % 10
    digit3 = a // 100 % 10
    digit4 = a // 1000 % 10
    digit5 = a // 10000
    answer = digit5 > digit4 and digit4 > digit3 and digit3 > digit2 and digit2 > digit1
    return answer
print(main(98764))
print(main(29746))
print(main(12345))