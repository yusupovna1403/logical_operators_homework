def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    d1 = x % 10
    d2 = x // 10 % 10 
    d3 = x // 100
    a = x >= 10 and x <= 99 or x >= 100 and x <= 999
    result = d1 == d2 or d1 == d3
    
    
    return result
print(main(12))
print(main(221))