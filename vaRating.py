def GetRating(ratings):
    dblRemaining = 100
    dblSubtotal = 0
    for i in ratings[0:]:
        dblSubtotal += dblRemaining * (i / 100)
        dblRemaining -= dblRemaining * (i / 100)
    return dblSubtotal


def GetPayment(
    rating, marStatus, numChildUnder18, numChildOver18=0, numParent=0, spouseAid=False
):
    payTableNoChild = [
        [467.39, 522.39, 566.39, 610.39, 511.39, 555.39],
        [673.28, 747.28, 806.28, 865.28, 732.28, 791.28],
        [958.44, 1050.44, 1124.44, 1198.44, 1032.44, 1106.44],
        [1214.03, 1325.03, 1414.03, 1503.03, 1303.03, 1392.03],
        [1529.95, 1659.95, 1763.95, 1867.95, 1633.95, 1737.95],
        [1778.43, 1926.43, 2045.43, 2164.43, 1897.43, 2016.43],
        [1998.52, 2165.52, 2299.52, 2433.52, 2132.52, 2266.52],
        [3332.06, 3517.84, 3666.94, 3816.04, 3481.16, 3630.26],
    ]

    payTableWithChild = [
        [504.39, 563.39, 607.39, 651.39, 548.39, 592.39],
        [722.28, 801.28, 860.28, 919.28, 781.28, 840.28],
        [1020.44, 1118.44, 1192.44, 1266.44, 1094.44, 1168.44],
        [1288.03, 1407.03, 1496.03, 1585.03, 1377.03, 1466.03],
        [1615.95, 1754.95, 1858.95, 1962.95, 1719.95, 1823.95],
        [1877.43, 2035.43, 2154.43, 2273.43, 1996.43, 2115.43],
        [2109.52, 2287.52, 2421.52, 2555.52, 2243.52, 2243.52],
        [3456.30, 3653.89, 3802.99, 3952.09, 3605.40, 3754.50],
    ]

    dependentPay = [
        [27, 89, 51],
        [36, 119, 68],
        [46, 149, 86],
        [55, 178, 102],
        [64, 208, 119],
        [73, 238, 136],
        [83, 268, 153],
        [92.31, 298.18, 170.38],
    ]

    match rating:
        case 10:
            payment = 152.64
            return payment
            quit()
        case 20:
            payment = 301.74
            return payment
            quit()
        case 30:
            i = 0
        case 40:
            i = 1
        case 50:
            i = 2
        case 60:
            i = 3
        case 70:
            i = 4
        case 80:
            i = 5
        case 90:
            i = 6
        case 100:
            i = 7

    if numChildUnder18 > 0 or numChildOver18 > 0:
        chart = payTableWithChild
    else:
        chart = payTableNoChild

    if marStatus.lower() == "s":
        if numParent == 0:
            j = 0
        elif numParent == 1:
            j = 4
        elif numParent >= 2:
            j = 5
    elif marStatus.lower() == "m":
        if numParent == 0:
            j = 1
        elif numParent == 1:
            j = 2
        elif numParent >= 2:
            j = 3

    under18multiplier = numChildUnder18 - 1
    over18multiplier = numChildOver18 - 1

    dblOutput = chart[i][j]

    if spouseAid:
        dblOutput += dependentPay[i][2]

    if under18multiplier > 0:
        dblOutput += dependentPay[i][0] * under18multiplier

    if over18multiplier > 0:
        dblOutput += dependentPay[i][1] * over18multiplier

    return dblOutput
