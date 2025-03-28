# Subarray with Given Sum
# Question: Given a 1-based indexing array arr[] of non-negative integers and an integer sum. You mainly need to return the left and right indexes(1-based indexing) of that subarray. In case of multiple subarrays, return all the subarries indexes on new lines one after the other. If no such subarray exists return an array consisting of element -1.

def subarraySum(arr, target):

    check = {}
    result = []

    for i in range(len(arr)):
        num = target - arr[i]

        if num in check:
            result.append([check[num] + 1, i + 1])
        
        check[arr[i]] = i

    return result if result else [-1]

# testing

arr=[1, 2, 4, 8, 6, 10]
target = 10
result_arr = subarraySum(arr, target)

# output

for x, y in result_arr:
    print(f'{x} {y}')                       
