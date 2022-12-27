def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    x >= 10 and x <= 99
    d1 = x % 10
    d2 = x // 10 % 10 
    return d1 == d2
def main1(n):
    n >= 100 and n <= 999
    n1 = n % 10
    n2 = n // 10 % 10 
    n3 = n // 100
    return n1 == n3
print(main(20))
print(main(11))
print(main1(121))
