class Solution(object):
    def singleNonDuplicate(self, nums):
        while True:
            if (len(nums) == 1):
                return nums[0]
            median = len(nums) // 2
            m = nums[median]
            # Checking if median is answer
            mL = nums[median - 1]
            mR = nums[median + 1]
            if (mL != m and mR != m):
                ans = m
                break
            if (len(nums) == 3):
                if (mR == m):
                    ans =  mL
                    break
                else:
                    ans =  mR 
                    break

            # Begin Recursion
            # if median matches to the right
            if (mL == m): # right side has answer
                gR = nums[(median + 1):]
                gL = nums[:(median - 1)]
                if(len(gL) % 2 == 1):
                    nums = gL
                else:
                    nums = gR
            else:
                print(median, nums)
                gR = nums[(median + 2):]
                gL = nums[:median]
                if(len(gL) % 2 == 1):
                    nums = gL
                else:
                    nums = gR
        return ans


# Test cases
def test_solution():
    sol = Solution()
    assert sol.singleNonDuplicate([1]) == 1
    assert sol.singleNonDuplicate([1,1,2,2,3]) == 3
    assert sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2
    assert sol.singleNonDuplicate([3,3,7,7,10,11,11]) == 10
    assert sol.singleNonDuplicate([1,1,2,2,3,4,4]) == 3
    assert sol.singleNonDuplicate([2,3,3,4,4,5,5,6,6]) == 2
    print("All test cases passed!")

test_solution()
