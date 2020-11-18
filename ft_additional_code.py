import ft_reverse_code as rev
import ft_straight_code as straight


def ft_len_str(num):
    a = 0
    for c in num:
        a += 1
    return a


def ft_rev_num(number):
    r = 0
    if number > 0:
        while number > 0:
            r = (r * 10) + (number % 10)
            number = number // 10
        return r
    else:
        number *= -1
        while number > 0:
            r = (r * 10) + (number % 10)
            number = number // 10
        return -r


def ft_bin_num(number):
    bin = 1
    while number > 0:
        bin = (bin * 10) + (number % 2)
        number //= 2
    bin = ft_rev_num(bin)
    bin //= 10
    return bin


def ft_pow(number, stepen):
    result = 1
    stepen2 = 0
    while stepen2 < stepen:
        stepen2 += 1
        result *= number
    return result


def ft_rev_bin_num(number):
    dec = 0
    stepen = -1
    while number > 0:
        stepen += 1
        dec = dec + (number % 10) * ft_pow(2, stepen)
        number //= 10
    return dec


def ft_additional_code(number):
    revcode = rev.ft_reverse_code(number)
    addcode = revcode[0]
    pcbin = straight.ft_straight_code(number)
    if -128 <= number <= 127:
        if number == -128:
            return ("10000000")
        if number >= 0:
            return pcbin
        else:
            tenss = ft_rev_bin_num(int(revcode)) + 1
            twoss = ft_bin_num(tenss)
        return twoss
    else:
        return ("invalyd number")







