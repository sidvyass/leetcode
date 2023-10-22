def two_sum(self, nums: list[int], target: int) -> list[int]:  # brute force
    for i in range(len(nums)):
        x = i+1
        while x < len(nums):
            if (nums[i] + nums[x]) == target:
                return [i, x]
            else:
                x += 1
                
