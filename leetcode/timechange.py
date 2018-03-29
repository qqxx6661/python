import sys


def time_min(time_list, time_min_str, index):
    print('new loop:', index, time_min_str, time_list)
    if index == 5 or index == 3 or index == 1:
        for num in range(len(time_list)-1, -1, -1):
            time_min_str += str(time_list.pop(num))
            print(index, time_min_str, time_list)
            return time_min(time_list, time_min_str, index-1)
    if index == 2 or index == 4:
        for num in range(len(time_list)-1, -1, -1):
            if time_list[num] <= 5:
                time_min_str += str(time_list.pop(num))
                print(index, time_min_str, time_list)
                return time_min(time_list, time_min_str, index-1)
    if index == 0:
        for num in range(len(time_list)-1, -1, -1):
            if time_list[num] <= 2:
                time_min_str += str(time_list.pop(num))
                print(index, time_min_str, time_list)
                return time_min_str
    # return 'N/A'

# def time_max(time_list, time_max_str, index):
#     print('new loop:', index, time_max_str, time_list)
#     if index == 3 or index == 1:
#         for num in range(len(time_list)-1, -1, -1):
#             time_max_str += str(time_list.pop(num))
#             print(index, time_max_str, time_list)
#             return time_max(time_list, time_max_str, index+1)
#     if index == 2 or index == 4:
#         for num in range(len(time_list)-1, -1, -1):
#             if time_list[num] <= 5:
#                 time_max_str += str(time_list.pop(num))
#                 print(index, time_max_str, time_list)
#                 return time_max(time_list, time_max_str, index+1)
#     if index == 0:
#         for num in range(len(time_list)-1, -1, -1):
#             if time_list[num] <= 2:
#                 time_max_str += str(time_list.pop(num))
#                 print(index, time_max_str, time_list)
#                 return time_max(time_list, time_max_str, index + 1)
#     if index == 5:
#         for num in range(len(time_list)-1, -1, -1):
#             time_max_str += str(time_list.pop(num))
#             print(index, time_max_str, time_list)
#             return time_max_str
    return 'N/A'

if __name__ == '__main__':
    while True:
        # s = sys.stdin.readline().strip()
        number = input().strip()
        if not number:
            break
        time_list = []
        for i in range(int(number)):
            s = input().strip()
            time_list.append(int(s))
        a = sorted(time_list)
        b = sorted(time_list, reverse=True)
        time_max_str = ''
        time_min_str = ''
        # time_min(a, time_min_str, 5)
        # print(time_min_str[::-1], time_max_str)
        print('----------------------------')
        time_min(b, time_max_str, 5)
        print(time_min_str[::-1], time_max_str)
