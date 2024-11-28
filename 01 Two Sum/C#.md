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

//------

public class Solution {
    public int[] TwoSum(int[] nums, int target)
    {
        var temp = new Dictionary<int, int>();

        var ans = new int[2];

        for (var index = 0; index < nums.Length; index++)
        {
            int c = nums[index];

            int left = target - c;
            
            if (temp.ContainsKey(left))
            {
                ans = [temp[left], index];

                break;
            }
            else{
                if (!temp.ContainsKey(c))
                {
                    temp.Add(c, index);
                }
            }
        }

        return ans;
    }
}