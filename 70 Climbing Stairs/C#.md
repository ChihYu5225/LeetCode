"# LeetCode"

public class Solution
{
    public int ClimbStairs(int n)
    {
        var dp = new List<int>() { 0, 1, 2 };

        for (var i = 3; i <= n; i++)
        {
            dp.Add(dp[i - 2] + dp[i - 1]);
        }

        return dp[n];
    }
}