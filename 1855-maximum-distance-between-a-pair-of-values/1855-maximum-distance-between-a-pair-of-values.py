class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        md=0
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums2[j]>=nums1[i]:
                md=max(md,j-i)
                j=j+1
            else:
                i=i+1
            if i>=j:
                j=j+1
        return md
