from test_cases import pre_sorted_two_sum
"""
From: https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function two_sum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:
  Input       :  numbers = [2,7,11,15], target = 9
  Output      :  [1,2]
  Explanation :  The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

def two_sum(nums_list, target):
  pass


if __name__ == '__main__':
  for case in pre_sorted_two_sum:
    print('\nexpected: ', case.get('assert_result'))
    print('result  : ', two_sum(case['param_1'], case['param_2']))
