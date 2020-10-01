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


def ft_pow(number, stepen):
    result = 1
    stepen2 = 0
    while stepen2 < stepen:
        stepen2 += 1
        result *= number
    return result


def ft_straight_code(number):
    sign = 0
    pcbin = 0
    if -128 <= number <= 127:
        if number == -128:
            print("10000000")
        if number >= 0:
            sign = 0
        else:
            sign = 1
        pcbin = (ft_bin_num(number) + ft_pow(10, 8)) + sign * ft_pow(10, 7)
        print(pcbin)
    else:
        print("invalyd number")


print(ft_straight_code(-128))



