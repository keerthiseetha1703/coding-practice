
def removeElement(nums,val):
        """
        :type nums:List[int]
        :type val:int
        :rtype:int
        """
        j=0
        for n in nums:
            if n!=val:
                nums[j]=n
                j+=1
        return nums

if __name__ == "__main__":
        print(removeElement([4,5,6,7,4,9,8],4))


        