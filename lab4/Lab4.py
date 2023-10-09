def vectorsSum(vec1, vec2, dim):
    resVec = []
    for i in range(dim):
        resVec.append(vec1[i] + vec2[i])
    return resVec

def vectorsSumConst(vec1, val, dim):
    resVec = []
    for i in range(dim):
        resVec.append(vec1[i] + val)
    return resVec

def multVect(vec, val, dim):
    resVec = []
    for i in range(dim):
        resVec.append(vec[i] * val)
    return resVec

def multVectConst(vec1, vec2, dim):
    res = 0
    for i in range(dim):
        res = res + vec1[i] * vec2[i]
    return res

def percepton(x, c):
    dim = len(x)
    w = [[0 for i in range(dim)] for j in range(dim)]
    flag = False
    while(not flag):
        flag = True
        for i in range(dim):
            d = []  # Значения M решающих функций
            tempFlag = False
            for j in range(dim):
                d.append(multVectConst(w[j], x[i], dim))
            for j in range(dim):
                if(i == j):
                    continue
                if(d[j] >= d[i]):
                    tempFlag = True
            if(tempFlag):
                flag = False
                for j in range(dim):
                    if(i == j):
                        w[j] = vectorsSum(w[j], multVect(x[i], c, dim), dim)
                    else:
                        w[j] = vectorsSum(w[j], multVect(x[i], c * -1, dim), dim)
    for i in range(dim):
        tempStr = "d(" + str(i + 1) + ")="
        for j in range(dim - 1):
            if(w[i][j] == 0):
                continue
            else:
                tempStr = tempStr + str(w[i][j]) + "x" + str(j + 1)
        if(w[i][dim - 1] != 0):
            tempStr = tempStr + str(w[i][dim - 1])
        print(tempStr)

c = 1
v = [[0,0,1],[1,1,1],[-1,1,1]]
percepton(v, c)