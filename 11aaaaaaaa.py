def function(a, b):
    sett = set([1])
    maxx = max(a, b)
    minn = min(a, b)
    temp1 = 1

    for i in range(2, maxx + 1):
        temp1 += i
        if temp1 <= maxx:
            sett.add(temp1)
        else:
            break

    temp = [[0] * (b + 1) for _ in range(a + 1)]

    for i in range(1, b + 1):
        temp[0][i] += temp[0][i - 1]
        if i in sett:
            temp[0][i] += 1

    for i in range(1, a + 1):
        temp[i][0] += temp[i - 1][0]
        if i in sett:
            temp[i][0] += 1

    for i in range(1, minn + 1):
        temp[i][i] = temp[i - 1][i] + temp[i][i - 1]

        for j in range(i + 1, b + 1):
            temp[i][j] = temp[i][j - 1] + temp[i - 1][j] - temp[i - 1][j - 1]

        for j in range(i + 1, a + 1):
            temp[j][i] = temp[j - 1][i] + temp[j][i - 1] - temp[i - 1][j - 1]

    print(sett)
    for i in temp:
        print(i, end='\n')


"""
finction(2, 2) = 4
function(5, 8) = 20
finction(0, 0) = 0
function(1, 1) = 2

function(0, 1) = 1
function(0, 2) = 1
function(0, 3) = 2
"""

function(5, 8)
