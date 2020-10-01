import ft_straight_code as straight


def ft_len_str(num):
    a = 0
    for c in num:
        a += 1
    return a


def ft_reverse_code(number):
    pcbin = straight.ft_straight_code(number)
    revcode = pcbin[0]
    revnum = 0
    lenstr = ft_len_str(pcbin)
    if -128 <= number <= 127:
        if number < 0:
            if number == -128:
                return ("01111111")
            else:
                for i in range(1, lenstr):
                    if pcbin[i] == '1':
                        revnum = 0
                    else:
                        revnum = 1
                    revcode += str(revnum)
                return revcode
        else:
            return pcbin
    else:
        return ("invalyd number")





