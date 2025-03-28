# Sort an array in wave form
# Question: Given an unsorted array of integers, sort the array into a wave array. An array arr[0..n-1] is sorted in wave form if: arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >=

def sortInWave(arr):

    arr.sort()

    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr

# testing

arr = [10, 90, 49, 2, 1, 5, 23]
result = sortInWave(arr)

# output

for i in range(len(arr)):
    print(arr[i], end=" ")
