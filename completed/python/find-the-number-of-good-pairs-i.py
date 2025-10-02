class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        goodPairCount = 0
        for i, numI in enumerate(nums1):
            for j, numJ in enumerate(nums2):
                if (numI % (numJ * k) == 0):
                    goodPairCount += 1

        return goodPairCount