from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = result = nums[0]

        for i in range(1, len(nums)):
            candidates = (nums[i], max_prod * nums[i], min_prod * nums[i])
            max_prod = max(candidates)
            min_prod = min(candidates)
            result = max(result, max_prod)

        return result

print(Solution().maxProduct([2, -3, -4]))