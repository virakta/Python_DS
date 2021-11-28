import pytest
class Solution(object):
    def __bsearch(self,nums,l,r,t):
        if l<=r:
            mid=l+(r-l+1)//2
            if nums[mid]==t:
                    self.result_index=mid
            elif t> nums[mid]:
                self.__bsearch(nums,mid+1,r,t)
            elif t< nums[mid]:
                self.__bsearch(nums,l,mid-1,t)
        else:
            self.result_index=-1
        return self.result_index
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.__bsearch(nums,0,len(nums)-1,target)
        return self.result_index


def test_solution():
    test=Solution()
    assert test.search([-1,0,3,5,9,12],9) == 4
    