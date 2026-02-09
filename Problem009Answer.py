def twoSum(nums, target):
    tar = target
    sorted_arr = nums
    low = 0
    high = len(sorted_arr) - 1
    ans_arr = []
    
    
    while low <= high:
        middle = low + (high-low) // 2
        
        if sorted_arr[middle] + sorted_arr[middle+1] == tar:
            ans_arr = [middle+1, middle+2]
            return ans_arr
        elif sorted_arr[middle] + sorted_arr[middle+1] > tar:
            high = middle - 1
        else:
            low = middle + 1
    return -1

example_arr = [1, 2, 3, 4, 5, 6]
tar_example = 11
ans= twoSum(example_arr, tar_example)
print(ans)
    