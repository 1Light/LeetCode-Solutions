# Majority Element
# Question: Given an array arr. Find the majority element in the array. If no majority exists, return -1. A majority element in an array is an element that appears strictly more than arr.size() / 2 times in the array.
# Used Boyer-Moore Voting Algorithm to optimize the space complexity form O(n) to O(1)

def majorityElement(arr):

    n = len(arr)

    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        
        count +=  (1 if num == candidate else -1)
    
    if arr.count(candidate) > n // 2:
        return candidate

    return -1

# testing
arr = [1, 1, 2, 1, 3, 5, 1]
result = majorityElement(arr)

#output
print(result)