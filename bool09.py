from cgi import print_arguments


def main(a):
    """Check the natural number.Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a % 2 == 0 and a > 0 
print(main(1.2))