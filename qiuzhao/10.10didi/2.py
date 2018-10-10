import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    n = values[0]
    m = values[1]
    line = sys.stdin.readline().strip()
    result_list = list(map(int, line.split()))
    # print(result_list)
    for i in range(m):
        min_p = min(result_list)
        min_index = result_list.index(min_p)
        if min_index == 0:
            result_list[min_index] += result_list[min_index + 1]
            result_list.pop(min_index + 1)
        elif min_index == len(result_list) - 1:
            result_list[min_index] += result_list[min_index - 1]
            result_list.pop(min_index - 1)
        else:
            if result_list[min_index - 1] >= result_list[min_index + 1]:
                result_list[min_index] += result_list[min_index + 1]
                result_list.pop(min_index + 1)
            else:
                result_list[min_index] += result_list[min_index - 1]
                result_list.pop(min_index - 1)
    print(min(result_list))
