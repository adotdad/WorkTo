def normalize(string):
    persian_numbers = ('۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    for i in range(len(string)):
        if string[i] in persian_numbers:
            string = string[: i] + str(persian_numbers.index(string[i]) + 1) + string[i + 1:]
    return string