# https://www.youtube.com/watch?v=vGsyTE4s34w
# nums[1] <= nums[2] >= nums[3] <= nums[4] >= nums[5] ...

def wiggleSort(arr):
    for i in range(1, len(arr)):
        if ((i % 2 == 1 and arr[i] < arr[i - 1]) or
            (i % 2 == 0 and arr[i] > arr[i - 1])):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr

before = [3,5,2,1,6,4]
print(*before, end=" ")
print("\n")
after = wiggleSort(before)
print(*after, end=" ")