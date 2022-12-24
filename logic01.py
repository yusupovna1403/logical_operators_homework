def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    result = a > b and b > c or a < b and b < c
    return result
print(main(1,2,3))
print(main(3,2,4))
print(main(6,4,1))