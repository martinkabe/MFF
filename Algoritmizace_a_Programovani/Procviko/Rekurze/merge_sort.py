from typing import List

def merge_sort_algo(arr: List) -> None:
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort_algo(left_arr)
        merge_sort_algo(right_arr)

        # merge
        i = 0 # left arr idx
        j = 0 # right arr idx
        k = 0 # merged array inx
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [2,3,5,1,7,-10,20,100,99,8]
merge_sort_algo(arr_test)
print(arr_test)
