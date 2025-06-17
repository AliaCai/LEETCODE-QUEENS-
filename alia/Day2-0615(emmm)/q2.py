#11. Container With Most Water: https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-100-liked
#worst time efficiency
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max=0;
#         for f in range (0, len(height)-1):
#             for t in range (1, len(height)):
#                 if ((t-f)*min(height[f], height[t]))>max:
#                     max=(t-f)*min(height[f], height[t])


#         return max;


# 2 pointers issue
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right =len(height)-1
        max=0
        size=0
        while left<=right:
            size=(right-left)*min(height[right], height[left])
            if(size>max):
                max=size
            

            if(height[right]>height[left]):
                left=left+1;
            else:
                right=right-1;  