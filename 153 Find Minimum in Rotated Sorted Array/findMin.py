from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

print(Solution().findMin([4,5,6,7,0,1,2]))