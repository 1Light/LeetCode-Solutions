# Subarray with Given Sum
# Question: Given a 1-based indexing array arr[] of non-negative integers and an integer sum. You mainly need to return the left and right indexes(1-based indexing) of that subarray. In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.
# Optimized: Using sliding window and avoiding nested for loops

def subarraySum(arr, target):

    start, end = 0, 0
    result = []
    total = 0

    for i in range(len(arr)):
        total += arr[i]

        if total >= target:
            end = i

            while total > target and start < end:
                total -= arr[start]
                start += 1

            if total == target:

                result.append(start + 1)
                result.append(end + 1)
                return result

    return [-1]

# testing
arr = [15, 2, 4, 8, 9, 5, 10, 23]
target = 23
result = subarraySum(arr, target)

# output
for i in range(len(result)):
    print(result[i], end=" ")
