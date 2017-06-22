


class Solution:
    def reverse(self, x):
        string = str(x)
        negation = 1
        if string[0] == '-':
            string = string[1:]
            negation = -1

        return int(string[::-1]) * negation

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(-2147483647))
