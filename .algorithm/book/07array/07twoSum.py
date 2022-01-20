# leetcode 1
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# # Input : nums = [2,7,11,15], target = 9
# # Output: [0,1]

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.useBruteForce(nums, target)
        return self.useDict(nums, target)
        return self.useTwoPointer(nums, target)

    # bruteforce : 모든 조합을 대입해보며 확인하는 방법. 효율 꽝
    def useBruteForce(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # dict가 탐색에서 훨씬 빠름
    def useDict(self, nums, target):
        # solution이 무조건 한쌍이기 때문에,
        # complement를 먼저 구한 후 해당하는 원소를 찾는 현재 상황에서는 오류 없음
        val2idx = {v: k for k, v in enumerate(nums)}
        for i, v in enumerate(nums):
            complement = target - v
            if (complement in val2idx) and (i != val2idx[complement]):
                return [i, val2idx[complement]]

    # 투포인터 사용
    def useTwoPointer(self, nums, target):
        enum = enumerate(nums)
        enum.sort(key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while left < right:
            tempSum = enum[left][1] + enum[right][1]
            if tempSum < target:
                left += 1
            elif tempSum > target:
                right -= 1
            elif tempSum == target:
                return [enum[left][0], enum[right][0]]
