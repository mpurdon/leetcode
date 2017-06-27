"""
Leetcode Problem

Reverse an integer

"""


class Solution:
    """
    The final solution

    """
    def reverse(self, number: int) -> int:
        """
        Reverse an integer

        Args:
            number: The number to reverse

        Returns:
            An integer

        """
        string = str(number)
        negation = 1
        if string[0] == '-':
            string = string[1:]
            negation = -1

        # We don't have to worry about 32b vs 64b because python
        # automatically casts to 64b
        return int(string[::-1]) * negation

    def hard_reverse(self, number: int) -> int:
        """

        Args:
            number: The number to reverse

        Returns:
            An integer

        """
        sign = 1
        if number < 1:
            sign = -1
            number = abs(number)

        reversed_number = 0
        while number > 0:
            reversed_number = (10 * reversed_number) + number % 10
            number //= 10

        return reversed_number * sign

if __name__ == '__main__':
    solution = Solution()

    tests = [
        123,
        1230,
        -123,
        -2147483647
    ]

    for test in tests:
        print(solution.reverse(test))
        print(solution.hard_reverse(test))
        print('-------------------')
