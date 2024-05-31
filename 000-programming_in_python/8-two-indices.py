def two_indices(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
        return[]

if __name__ == "__main__":
    print(two_indices([2, 7, 11, 15], 9)) 
    print(two_indices([3, 2, 4], 6))       
    print(two_indices([1, 2, 3, 4, 5], 9)) 
   
