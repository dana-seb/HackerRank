arr = [1, 3, 5, 7, 9]

def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    mini_sum = sorted_arr[:4]
    max_sum = sorted_arr[1:]

    mini = sum(mini_sum)
    maxi = sum(max_sum)
    print(mini, maxi)

miniMaxSum(arr)