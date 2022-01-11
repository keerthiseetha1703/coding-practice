def RangeSearch(nums,target):
    """
        :type nums: List[]
        :type target: int
        :rtype: List[]
    """
    p=get_insert_index(nums,target)
    if nums[p]!=target:
            return 1,-1
    q=get_insert_index(nums,target-1)
    if q<len(nums)-1 and nums[q]!=target:
            q=q+1
    return p,q
def get_insert_index(nums,target):
    lo,hi=0,len(nums)
    mid=int((lo+hi)/2)
    while mid!=lo:
        if nums[mid]==target and (mid==len(nums)-1 or nums[mid+1]>target):
            return mid
        elif nums[mid]<=target:
            lo=mid
        else: hi=mid
        mid=int((lo+hi)/2)
    return mid
if __name__=="__main__":
       n= RangeSearch([0,1,3,5,7,8,8,8,9,10],8)
       print(n)