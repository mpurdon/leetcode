"""
Leetcode problem

Regular expression matcher

"""


class Solution:
    """
    The final solution

    """
    def check_matches(self, string: str, regex_pattern: str) -> bool:
        """
        Check if the test string matches the provided regex pattern

        Args:
            string: The string to test
            regex_pattern: The regex to try to match.

        Returns:
            A boolean indicating whether the string matched or not.

        """
        print('Checking if {} matches pattern {}'.format(test_string, regex_pattern))
        pattern_index = 0
        end_of_pattern = len(regex_pattern) - 1

        for letter in string:
            print('? checking letter {} against fragment {}'.format(letter, pattern_index))

            if pattern_index > end_of_pattern:
                print('- reached the end of the pattern')
                return False

            pattern_fragment = regex_pattern[pattern_index]

            if pattern_fragment in (letter, '.'):
                print('+ letter was matched by {}'.format(pattern_fragment))
                pattern_index += 1
            elif pattern_index > 0 and pattern_fragment == '*':
                if regex_pattern[pattern_index - 1] in (letter, '.'):
                    print('* wildcard pattern * matched {}'.format(letter))
                    continue
                elif regex_pattern[pattern_index + 1] in (letter, '.'):
                    print('* wildcard only matched one, advancing pattern index.')
                    pattern_index += 2
                else:
                    print('- Wildcard did not match {}'.format(letter))
                    return False
            else:
                print('- {} did not match {}'.format(letter, pattern_fragment))
                return False

        print('! end of string reached')
        return True


if __name__ == '__main__':
    solution = Solution()

    tests = [
        ('..',     '..',     True),
        ('aa',     '..',     True),
        ('aa',     'a',      False),
        ('aa',     'aa',     True),
        ('aaa',    'a*',     True),
        ('aa',     'a*',     True),
        ('a',      'a*',     True),
        ('aa',     '.*',     True),
        ('ab',     '.*',     True),
        ('aab',    'c*a*b',  False),
        ('cab',    'c*a*b',  True),
        ('ccab',   'c*a*b',  True),
        ('caab',   'c*a*b',  True),
        ('cabb',   'c*a*b',  False),
        ('ccaab',  'c*a*b',  True),
        ('ccaabb', 'c*a*b',  False),
        ('ccaabb', 'c*a*b.', True),
        ('ccaabb', 'c*a*b*', True),
    ]

    fails = 0
    for test_string, pattern, expected in tests:
        matches = solution.check_matches(test_string, pattern)

        if matches == expected:
            print('PASSED: string "{}" {} pattern "{}"'.format(test_string,
                                                               'matches' if matches else 'does not match',
                                                               pattern))
        else:
            fails += 1
            print('FAILED: string "{}" {} pattern "{}"'.format(test_string,
                                                               'matches' if matches else 'does not match',
                                                               pattern))

        print('----------------------------------------')

    print('{} tests run, {} fails'.format(len(tests), fails))
