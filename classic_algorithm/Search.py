MAXSIZE = 20

def fibonacci():  # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    f = [0] * MAXSIZE
    f[0] = 1
    f[1] = 1
    for i in range(2, MAXSIZE):
        f[i] = f[i-1] + f[i-2]
    return f

def fibonacciSearch(array, value):
    low, mid, high = 0, 0, len(array)-1
    k = 0
    f = fibonacci()
    while len(array) > f[k]-1:
        k += 1
    temp = array + [array[-1] * (f[k]-1-len(array))]
    while low <= high:
        mid = low + f[k-1] - 1
        if temp[mid] > value:
            high = mid - 1
            k = k - 1
        elif temp[mid] < value:
            low = mid + 1
            k = k - 2
        else:
            if mid <= high:
                return mid
            else:
                return high
    return -1

if __name__ == '__main__':
    a = [1, 3, 5, 6, 7, 88]
    print(fibonacciSearch(a, 2))
