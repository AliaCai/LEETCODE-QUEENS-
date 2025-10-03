# A futuristic research facility is racing to develop cutting-edge artificial intelligence, "AURA", which requires a carefully balanced ecosystem of computing power. The facility has acquired a collection of n advanced servers, each with a unique health rating and belonging to a specific model series. The AI core, however, can only harmonize with a limited diversity of server models at once due to compatibility constraints.

# To stabilize AURA's neural matrix, your engineering team must choose a subset of servers for installation. Your goal is to select servers of at most k different model series to maximize the combined health rating of all active servers. Note that every server's health rating contributes to the system's reliability, but introducing too many models will destabilize AURA's learning algorithms.

# Given two integer arrays health and serverType, and an integer k, return the maximum possible sum of health ratings for any group of servers using no more than k distinct model series.

# Constraints:

# 1 <= k <= n <= 
# 10
# 3
# 10 
# 3
 
# 1 <= health[i] <= 
# 10
# 5
# 10 
# 5
 
# 1 <= serverType[i] <= n
# Example 1:

# Input: health = [1, 3, 1, 5, 3, 2, 4], serverType = [1, 2, 1, 3, 1, 4, 5], k = 3
# Output: 14
# Explanation:

# Type 1 total health: 1 + 1 + 3 = 5.
# Type 2 total health: 3.
# Type 3 total health: 5.
# Type 4 total health: 2.
# Type 5 total health: 4.
# With k = 3, selecting type 1, type 3, and type 5 yields the maximum health sum of 5 + 5 + 4 = 14.

# Example 2:

# Input: health = [1, 2, 3, 10, 10], serverType = [3, 3, 1, 2, 5], k = 2
# Output: 20

# Example 3:

# Input: health = [4, 5, 5, 6], serverType = [1, 2, 1, 2], k = 1
# Output: 11



def solve(health, serverType, k):
    hasmap=dict()
    for i in range(len(serverType)) :
        val=serverType[i]
        hasmap[val]=hasmap.get(val,0)+health(val)
    print(hasmap)
solve([1, 3, 1, 5, 3, 2, 4],[1, 2, 1, 3, 1, 4, 5],3 )