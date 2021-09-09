class Solution(object):
    def threeSum(self, nums):
        
        res = []
        amount = [0] * 200001
        nums2 = sorted(nums)

        for v in nums:
            amount[v + 100000] += 1

        # 3 different numbers
        for i in range(len(nums2)):
            
            if i > 0 and nums2[i] == nums2[i - 1]:
                continue

            for j in range(i+1, len(nums2)):

                if nums2[j] == nums2[i] or nums2[j] == nums2[j - 1]:
                    continue

                diff = 0 - nums2[i] - nums2[j]
                if diff <= nums2[j]:
                    continue
                if diff >= -100000 and diff <= 100000 and amount[diff + 100000] >0:
                    res.append([nums2[i], nums2[j], diff])


        # at least two equal numbers
        for i in range(len(nums2)):
            if i > 0 and nums2[i] == nums2[i - 1]:
                continue
            if i + 1 < len(nums2) and nums2[i + 1] == nums2[i]:
                diff = 0 - nums2[i] - nums2[i]
                if diff >= -100000 and diff <= 100000 and (nums2[i] != 0 and amount[diff + 100000] >0 or nums2[i] == 0 and amount[diff + 100000] > 2):
                    res.append([nums2[i], nums2[i], diff])

        return res