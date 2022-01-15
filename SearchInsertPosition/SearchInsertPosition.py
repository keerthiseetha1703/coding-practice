class Solution(object):
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)
        mid=int(low+(high-low)/2)
        while mid!=low:
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid
            else: high=mid
            mid=int(low+(high-low)/2)
        return mid if target<nums[mid] else mid+1
    
    if __name__=="__main__":
        print(searchInsert([1,2,3,4,5],4))
