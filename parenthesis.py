"""
Leetcode.com Problem

Determine if the parenthesis in a string are balanced

"""


def check_balanced(test_string: str) -> bool:
    """
    Validate the string
  
    Args:
        test_string: The string to validate
  
    Returns:
        A boolean indicating whether the string was valid or not.
  
    """
    open_parentheses = '([{'
    close_parentheses = ')]}'
    parentheses = dict(zip(open_parentheses, close_parentheses))

    stack = []

    for char in test_string:
        if char in open_parentheses:
            stack.append(char)

        if char in close_parentheses:
            try:
                last_parentheses = stack.pop()
                if parentheses[last_parentheses] != char:
                    return False
            except IndexError:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    strings = [
        ('', True),
        ('(', False),
        ('{([])}', True),
        ('({([]]}', False),
        ('{}}', False),
        ('acb', True),
        ('{ab}c', True),
        ('[{ab}c]]', False),
    ]

    fails = 0
    for test_string, expectation in strings:
        is_balanced = check_balanced(test_string)
        if expectation != is_balanced:
            fails += 1
            print('FAILED: {} {} balanced.'.format(test_string, 'is' if is_balanced else 'is not'))

    print('{} tests ran, {} failed.'.format(len(strings), fails))
