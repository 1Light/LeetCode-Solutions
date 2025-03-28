# Subarray with Given Sum
# Question: Given a 1-based indexing array arr[] of non-negative integers and an integer sum. You mainly need to return the left and right indexes(1-based indexing) of that subarray. In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

def subarraySum(arr, target):

    result = []

    for i in range(len(arr)):
        total = 0

        for j in range(i, len(arr)):
            total += arr[j]
            if total == target:
                result.append(i + 1)
                result.append(j + 1)
                return result
    
    return [-1]

# testing

arr=[15, 2, 4, 8, 9, 5, 10, 23]
target = 23
result_arr = subarraySum(arr, target)

# output

for i in range(len(result_arr)):
    print(result_arr[i], end=" ")