# Ideas
# - Use binary search to create sub arrays depending on whether the median of each array is bigger or smaller than the target
# - Use recursion to iterate through each sub array until the target is found 

# Approach
# - Find median
# - Check for base case: there is one or two numbers in the array
# - If not, check if the median is bigger or smaller than the target
# - For the half where the target is, recurse to the beginning of the problem until the base case is completed

class Solution(object):
    def search(self, nums, target):
        rsi = 0 # Number to remember where we split the array and the possible index associated
        while True:
            if (len(nums) == 1): # only one number left (Base Case 1/2)
                if (nums[0] == target):
                    return 0 + rsi
                else:
                    return -1
            median = len(nums) // 2
            if (len(nums) == 2): # two numbers left (Base Case 2/2)
                if (nums[0] == target):
                    return 0 + rsi
                if (nums[1] == target):
                    return 1 + rsi
                else:
                    return -1
            if (len(nums) == 3):
                if (nums[2] == target):
                    return 2 + rsi
                if (nums[0] == target):
                    return rsi
                if (nums[1] == target):
                    return 1 + rsi
                else:
                    # Screw you for making me check this case!
                    return -1
            if target == nums[median]:
                    return median + rsi
            if (target < nums[median]):
                nums = nums[:(median)]
                # rsi doesn't change bc it is the first half
            else:
                nums = nums[median:]
                rsi = rsi + median
        
        

# Test cases
def test_solution():
    sol = Solution()
    assert sol.search([1], 1) == 0
    assert sol.search([1, 2], 1) == 0
    assert sol.search([1, 2], 2) == 1
    assert sol.search([1, 2, 3], 2) == 1
    assert sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
    assert sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
    assert sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8
    assert sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
    print("All test cases passed!")

test_solution()
