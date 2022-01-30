
def counting(arr):
    cnt_list = [0] * (max(arr) + 1)
    for number in arr:
        cnt_list[number] += 1
    
    for i in range(len(cnt_list)):
        if cnt_list[i] > 0:
            print(f"{i}" * cnt_list[i], end=" ")
    
    return cnt_list

arr = [10,5,100,2,30]
res = counting(arr)
