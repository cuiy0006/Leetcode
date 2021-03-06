class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j -1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
       
       
       
       
f[i][j] = min(
    f[i - 1][j - 1] | word1[i - 1] == word2[j - 1],    // word1的第i个字符等于word2的第j个字符 
    f[i - 1][j - 1] + 1,     // 将word1[i - 1]和word2[j - 1]替换为同一个字母
    f[i - 1][j] + 1,         // 删去word1[i - 1] 或 在word2[j - 1]的后面添加一个字母
    f[i][j - 1] + 1          // 在word1[i - 1]的后面添加一个字母 或 删去word1[j - 1]
)
