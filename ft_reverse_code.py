import ft_straight_code as straight


def ft_reverse_num(number):
    rev = 0
    if number == 1:
        rev = 0
    else:
        rev = 1
    return rev


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


def ft_reverse_code(number):
    pcbin = straight.ft_straight_code(number)
    revbin = 1
    if -128 <= number <= 127:
        if number == -128:
            return 101111111
        if number >= 0:
            return pcbin
        else:
            while pcbin > 11:
                revbin = (revbin * 10) + ft_reverse_num(pcbin % 10)
                pcbin //= 10
            revbin = ft_rev_num(revbin * 100 + 11) // 10
            return revbin
    else:
        return ("invalyd number")




        while lenstr != 0:
            if pcbin[lenstr - 1]:
                revnum = 0
            else:
                revnum = 1
            revcode += str(revnum)
            lenstr -= 1
        return revcode
