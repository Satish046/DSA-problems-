from typing import List

class Solution:
    def streak(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            max_count = max(max_count, count)
        return max_count



if __name__ == "__main__" :
    nums = [1,1,0,1,1,1,1]
    solution = Solution() 
    ans = solution.streak(nums)
    print(ans)