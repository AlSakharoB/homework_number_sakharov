def ft_len(num):
    a = 0
    while num > 0:
        a += 1
        num //= 10
    return a


def ft_bin_num(number):
    bin = 1
    if number < 0:
        number = -number
    while number > 0:
        bin = (bin * 10) + (number % 2)
        number //= 2
    bin = ft_rev_num(bin)
    bin //= 10
    return bin


def ft_rev_num(number):
    r = 0
    while number > 0:
        r = (r * 10) + (number % 10)
        number = number // 10
    return r


def ft_straight_code(number):
    sign = 0
    pcbin = ""
    bin = 0
    if -128 <= number <= 127:
        if number == -128:
            return ("10000000")
        else:
            if number >= 0:
                sign = 0
            else:
                sign = 1
            bin = ft_bin_num(number)
            lengbin = ft_len(bin)
            return (str(sign) + ("0" * (7 - lengbin)) + str(bin))
    else:
        return ("invalyd number")





