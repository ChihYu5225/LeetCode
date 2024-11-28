"# LeetCode" 

public class Solution {
    public int[] TwoSum(int[] nums, int target)
    {
        var temp = new Dictionary<int, int>();

        for (var index = 0; index < nums.Length; index++)
        {
            int left = target - nums[index];
            
            if (temp.ContainsKey(left))
            {
                return new int[]{temp[left], index};
            }       

            if (!temp.ContainsKey(nums[index]))
            {
                temp.Add(nums[index], index);
            }
        }

        return null;
    }
}