#початкова матриця
A = [[4,2,0],[1,3,2],[-1, 3, 10]]

#міняємо перший та другий рядок місцями
A[0],A[1]= A[1],A[0]

#до 2ого рядка додаэмо 1ий, помножений на -4; до 3ого рядка додати перший
result = []
result2 = []
for i in range(len(A[0])):
    temp = A[0][i] * -4 + A[1][i]
    result.append(int(temp))
    temp2 = A[2][i] + A[0][i]
    result2.append(int(temp2))
A[1],A[2] = result, result2

#2ий рядок поділити на -2, третій рядок ділимо на 6
result3 = []
result4 = []
for i in range(len(A[0])):
    temp3 = A[1][i] / -2
    result3.append(int(temp3))
    temp4 = A[2][i] / 6
    result4.append(int(temp4))
A[1],A[2] = result3, result4

#поміняємо другий та третій рядок місцями
A[1],A[2] = A[2],A[1]

#до 3ого рядка додамо 2ий, помножений на -5
result5 = []
for i in range(len(A[0])):
    temp5 = A[2][i] + A[1][i] * -5
    result5.append(int(temp5))
A[2] = result5
#прінт
for i in A:
    print(i)