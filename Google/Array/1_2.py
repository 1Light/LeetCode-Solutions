# Sort an array in wave form
# Question: Given an unsorted array of integers, sort the array into a wave array. An array arr[0..n-1] is sorted in wave form if: arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >=
# Optimized: Avoiding sort()

def sortInWave(arr):

    for i in range(0, len(arr), 2):
        if (i > 0 and arr[i] < arr[i-1]):
            arr[i-1], arr[i] = arr[i], arr[i-1]
        
        if (i < len(arr)-1 and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

# testing

arr=[1, 2, 3, 4, 5]
result = sortInWave(arr)

# output

for i in range(len(arr)):
    print(arr[i], end=" ")