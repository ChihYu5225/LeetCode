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

/*
    用動態規劃方法將問題切分，n3 = n1 + n2, n4 = n2 + n3，並把結果存起來放入List避免重複計算
*/