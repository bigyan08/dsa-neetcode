class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
       
        for i in range(len(nums)):
            temp = nums[:]
            s = 1
            temp.remove(nums[i])
            for j in range(len(temp)):
                s = s* temp[j]
            output.append(s)
        return output
        