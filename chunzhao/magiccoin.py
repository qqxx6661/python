def coin(number, result):
    print number, result
    if number == 0:
        return result
    while number != 0:
        if number % 2 == 0:
            result = '2' + result
            coin((number - 2) / 2, result)
        else:
            result = '1' + result
            coin((number - 1) / 2, result)


if __name__ == '__main__':
    while True:
        n = raw_input()
        if not n:
            break
        result = ''
        result = coin(int(n), result)
        print result
