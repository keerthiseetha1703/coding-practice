def searchElement(nums,val):
    """
     :type nums:List[int]
     :type val:int
     :rtype:List[int]
    """
    # to store values of indices of search element
    pos=[] 
    numsize=len(nums)
    for i in range (numsize):
            if nums[i]==val:
                pos.append(i)
                
            i+=1
    return pos

if __name__=="__main__":
    n=searchElement([1,2,3,4,5,3],3)
    print(n)
