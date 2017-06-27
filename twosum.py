"""
Leetcode problem

Find two numbers in a list that sum to the target number

"""
import contextlib
import dis
import random
import sys
import time


@contextlib.contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


class Solution:
    """
    The final solution

    """
    def two_sum_pointers(self, numbers: list, target: int) -> tuple:
        """
        Find the indexes of the two numbers that add up to the target

        Note:
            This only really works if the list is sorted

        Args:
            numbers: The list of numbers
            target:  The target number

        """
        left = 0
        last_index = len(numbers) - 1
        right = last_index

        iterations = 0
        while right > left:
            iterations += 1
            left_item = numbers[left]
            right_item = numbers[right]

            if left_item + right_item == target:
                return iterations, left, right

            right -= 1

            if right == left:
                left += 1
                right = last_index

        return iterations, -1, -1

    def two_sum_index(self, numbers: list, target: int) -> tuple:
        """
        Find the indexes of the two numbers that add up to the target

        Args:
            numbers: The list of numbers
            target: the target number

        """
        local_abs = abs
        iterations = 0
        for index, value in enumerate(numbers):
            iterations += 1
            with ignored(ValueError):
                # print('checking for {} in numbers'.format(difference))
                return iterations, index, numbers[index:].index(local_abs(value - target))

        return iterations, -1, -1

    def two_sum_map(self, numbers: list, target: int) -> tuple:
        """
        Find the indexes of the two numbers that add up to the target

        Args:
            numbers: The list of numbers
            target: the target number

        """
        sum_map = {}
        iterations = 0
        for index in range(len(numbers)):
            iterations += 1
            if numbers[index] in sum_map:
                return iterations, sum_map[numbers[index]], index

            sum_map[target - numbers[index]] = index

        return iterations, -1, -1

    def two_sum_my_map(self, numbers: list, target: int) -> tuple:
        """
        Find the indexes of the two numbers that add up to the target

        Args:
            numbers: The list of numbers
            target: the target number

        """
        sum_map = {}
        iterations = 0
        for index in range(len(numbers)):
            iterations += 1
            current_num = numbers[index]
            if current_num in sum_map:
                return iterations, sum_map[current_num], index

            sum_map[target - current_num] = index

        return iterations, -1, -1

if __name__ == '__main__':

    # print(dis.dis(Solution.two_sum_my_map))
    # sys.exit(1)

    solution = Solution()

    # print(dis.dis(Solution.twoSum))
    # print(dis.dis(Solution.twoSum2))
    # print(dis.dis(Solution.twoSum4))

    # print(solution.two_sum_map([15, 2, 5, 7, 11], 20))
    # print(solution.two_sum_my_map([15, 2, 5, 7, 11], 20))
    # print(solution.two_sum_index([15, 2, 5, 7, 11], 20))
    # print(solution.two_sum_pointers([15, 2, 5, 7, 11], 20))
    # print(solution.twoSum4([2, 5, 7, 11, 15], 21))
    # print('----------------------------------------------')

    # print(solution.twoSum([2, 5, 7, 11, 15], 9))
    # print(solution.twoSum2([2, 5, 7, 11, 15], 9))
    # print('----------------------------------------------')

    iterations = 10
    num_nums = 100

    results = {}

    random.seed(123456789)

    nums = list(range(1, num_nums))
    random.shuffle(nums)
    target = (num_nums-3) * 2

    print('Getting pairs for {} in {} numbers'.format(target, num_nums))
    print('Map', solution.two_sum_map(nums, target))
    print('My Map', solution.two_sum_my_map(nums, target))
    print('Index', solution.two_sum_index(nums, target))
    print('Pointers', solution.two_sum_pointers(nums, target))
    print('------------------------------')

    for num_nums in [100, 1000, 10000]:
        nums = list(range(1, num_nums))
        random.shuffle(nums)
        target = (num_nums - 3) * 2
        print('finding {} in {} random numbers.'.format(target, len(nums)))

        start = time.time()
        for i in range(iterations):
            solution.two_sum_pointers(nums, target)
        results['Pointers'] = time.time() - start

        start = time.time()
        for i in range(iterations):
            solution.two_sum_map(nums, target)
        results['Hash Map'] = time.time() - start

        start = time.time()
        for i in range(iterations):
            solution.two_sum_my_map(nums, target)
        results['My Hash Map'] = time.time() - start

        start = time.time()
        for i in range(iterations):
            solution.two_sum_index(nums, target)
        results['List Index'] = time.time() - start

        for method in sorted(results, key=results.get):
            print('> {m:{p}} {r:.9f}'.format(m=method, r=results[method], p=11))

        print('------------------------------\n')

    for num_nums in [100, 1000, 10000]:
        nums = list(range(1, num_nums))
        target = (num_nums - 3) * 2
        print('finding {} in {} sorted numbers.'.format(target, len(nums)))

        start = time.time()
        for i in range(iterations):
            solution.two_sum_pointers(nums, target)
        results['Pointers'] = time.time() - start

        start = time.time()
        for i in range(iterations):
            solution.two_sum_map(nums, target)
        results['Hash Map'] = time.time() - start

        start = time.time()
        for i in range(iterations):
            solution.two_sum_my_map(nums, target)
        results['My Hash Map'] = time.time() - start

        start = time.time()
        for i in range(iterations):
            solution.two_sum_index(nums, target)
        results['List Index'] = time.time() - start

        for method in sorted(results, key=results.get):
            print('> {m:{p}} {r:.9f}'.format(m=method, r=results[method], p=11))

        print('------------------------------')


    # print(solution.twoSum([9, 2, 7, 11, 15], 11))
    # print(solution.twoSum2([9, 2, 7, 11, 15], 11))
    # print(solution.twoSum2([9, 2, 7, 11, 15], 11))
    # print('----------------------------------------------')

    # print(solution.twoSum([2, 5, 7, 7, 11, 15], 14))
    # print(solution.twoSum2([2, 5, 7, 7, 11, 15], 14))
    # print('----------------------------------------------')

    # print(solution.twoSum([2, 5, 7, 7, 11, 15], 26))
    # print(solution.twoSum2([2, 5, 7, 7, 11, 15], 26))
    # print(solution.twoSum4([2, 5, 7, 7, 11, 15], 26))
    # print('----------------------------------------------')

    print('Done.')
