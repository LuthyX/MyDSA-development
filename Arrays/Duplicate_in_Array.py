#finding duplicate iitems in a one dimensional array with O(N) linear time complexity
# The problem is that we want to find duplicates in a one-dimensional array of integers in O(N) running time where the integer values are smaller than the length of the array!

# For example: if we have a list [1, 2, 3, 1, 5] then the algorithm can detect that there are a duplicate with value 1.

# Note: the array can not contain items smaller than 0 and items with values greater than the size of the list. This is how we can achieve O(N) linear running time complexity!

def find_duplicate(nums):
    for num in nums:
        if nums[abs(num)] > 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print("Repetition found: %s" %str(abs(num))
            )
if __name__ == "__main__":
    find = [1,2,4,1,1,4,5,6,9]     
    find_duplicate(find)       