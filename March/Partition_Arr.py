#2161. Partition Array According to Given Pivot March-03/2025
class Solution(object):
    def pivotArray(self, nums, pivot):
        smaller = []
        larger= []
        pivot_list=[]
        for i in range(len(nums)):
            if nums[i] < pivot:
                smaller.append(nums[i])
            elif nums[i] > pivot:
                larger.append(nums[i])
            else:
                pivot_list.append(nums[i])
        return smaller + pivot_list + larger
        