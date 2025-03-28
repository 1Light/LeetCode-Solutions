# Majority Element
# Question: Given an array arr. Find the majority element in the array. If no majority exists, return -1. A majority element in an array is an element that appears strictly more than arr.size() / 2 times in the array.

def majorityElement(arr):

    my_dict = {key:0 for key in arr}

    major_marker = len(arr) // 2

    for i in range(len(arr)):
        if arr[i] in my_dict:
            my_dict[arr[i]] += 1
    
    for key, value in my_dict.items():
        if value > major_marker:
            return key

        return [-1]

# testing
arr = [1, 1, 2, 1, 3, 5, 1]
result = majorityElement(arr)

#output
print(result)
