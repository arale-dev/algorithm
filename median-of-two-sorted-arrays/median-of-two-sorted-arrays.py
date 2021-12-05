class Solution:
    def findMedian(self, nums: List[int]) -> float:
        if len(nums)%2 == 1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2;
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # print(nums1, nums2)
        if nums1 == []:
            return self.findMedian(nums2)
        elif nums2 == []:
            return self.findMedian(nums1)
        
        med1 = self.findMedian(nums1)
        med2 = self.findMedian(nums2)
        
        cutLength = min((len(nums1) - 1)//2, (len(nums2) - 1)//2)
        if cutLength == 0:
            return self.findMedian(sorted(nums1 + nums2))
        
        if med1 > med2:
            return self.findMedianSortedArrays(nums1[:len(nums1) - cutLength:], nums2[cutLength::])
        elif med1 < med2:
            return self.findMedianSortedArrays(nums1[cutLength::], nums2[:len(nums2) - cutLength:])
        else:
            return med1