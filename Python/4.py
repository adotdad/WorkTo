def three_digits_separator(n):
    if n == 0:
        return str(n)
    result = ''
    while True:
        if int(n / 1000) == 0:
            result = str(n) + result
            return result
        else:
            for i in range(3):
                result = str(n - 10 * int(n / 10)) + result
                n = int(n / 10)
            result = ',' + result


