class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temps = []
        for i in range(len(nums)) :
            for j in range(i+1 ,len(nums)):
                if nums[i] + nums[j] == target :
                    temps.append(i)
                    temps.append(j)
                    return temps

        return []  