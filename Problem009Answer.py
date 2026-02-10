#Version 2 of Problem Solution
def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    ans_arr = []

    # Iterate while left pointer is less than right
    while left < right:
        sum = nums[left] + nums[right]

        # Check if the sum matches the target
        if sum == target:
            ans_arr = [left+1, right+1]
            return ans_arr
        elif sum < target:
            
            # Move left pointer to the right
            left += 1
        else:
            
            # Move right pointer to the left
            right -= 1

    # If no pair is found
    return -1

example_arr = [1, 2, 3, 4, 5, 6]
tar_example = 11
ans= twoSum(example_arr, tar_example)
print(ans)
    
