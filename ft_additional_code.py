import ft_reverse_code as ft


def ft_pow(number, stepen):
    result = 1
    stepen2 = 0
    while stepen2 < stepen:
        stepen2 += 1
        result *= number
    return result


def ft_rev_num(number):
    r = 0
    while number > 0:
        r = (r * 10) + (number % 10)
        number = number // 10
    return r


def ft_len(str):
    length = 0
    while str > 0:
        length += 1
        str //= 10
    return length


def ft_additional_code(number):
    revbin = ft.ft_reverse_code(number)
    addbin = 1
    lengthaddbin = 0
    if -128 <= number <= 127:
        if number == -128:
            return 100000000
        if number >= 0:
            return revbin
        else:
            while revbin > 11:
                if revbin % 10 + 1 >= 2:
                    addbin = addbin * 10 + 0
                    revbin //= 10
                else:
                    addbin = addbin * 10 + 1
                    break
        revbin = ft.ft_reverse_code(number)
        addbin = ft_rev_num(addbin)
        lengthaddbin = ft_len(addbin)
        addbin = (revbin // ft_pow(10, lengthaddbin - 1)) * (ft_pow(10, lengthaddbin - 1)) + addbin // 10
        return addbin
    else:
        return ("invalyd number")


