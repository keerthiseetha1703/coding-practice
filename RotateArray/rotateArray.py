def rotateArray(nums,k):
    """
    :type nums:List[int]
    :type k:int
    :rtype:List[int]
    """
    n=len(nums)-k
    i=n
    newa=[]
    m=0
    for i in range(n,len(nums)):
        newa.append(nums[i])
    
    for m in range(0,n):
        newa.append(nums[m])
    
    return newa

if __name__=="__main__":
    print(rotateArray([1,2,3,4,5],2))