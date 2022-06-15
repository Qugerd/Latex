from matrix import *
import numpy as np
import numpy.linalg


# QR_START________________________________

# РєР°Рє sign С‚РѕР»СЊРєРѕ РІ 0 РІРѕР·РІСЂР°С‰Р°РµС‚ 1
def deta(a):
    return -1 if a < 0 else 1


# РЎРѕР·РґР°РЅРёРµ
def generate_P(p):
    I = ones(len(p))
    # print(I)
    newp = [p]
    a = -2 / dot(p)[0][0]
    m = dot(transpose(newp), newp)
    P = mul(m, a)
    P = plus(I, P)
    return P


def qr_razloj(matrix):
    if (len(matrix) != len(matrix[0])):
        return None
    r = [m[:] for m in matrix]
    n = len(r)
    q = ones(len(matrix))

    for k in range(0, len(r) - 1):
        
        p = [0] * len(r)
        
        akk = (sum([r[l][k] ** 2 for l in range(k, n)])) ** 0.5

        p[k] = r[k][k] + deta(akk) * akk

        for i in range(k + 1, n):
            p[i] = r[i][k]

        q = dot(q, generate_P(p))
        pp = sum([p[i] ** 2 for i in range(k, n)])
        for j in range(k, n):
            px = sum([p[l] * r[l][j] for l in range(0, n)])
            for i in range(k, n):
                r[i][j] -= 2 * p[i] / pp * px

    return [q, r]


# QR_END__________________________________




# HOUSEHOLDER_START_______________________

def hessel_rot(matrix):
    matrix = [r[:] for r in matrix]

    for j in range(len(matrix)):
        for i in range(j + 2, len(matrix)):
            if (j > len(matrix) - i + 1):
                break

            c = matrix[j + 1][j] / (matrix[j + 1][j] ** 2 + matrix[i][j] ** 2) ** 0.5
            s = matrix[i][j] / (matrix[j + 1][j] ** 2 + matrix[i][j] ** 2) ** 0.5

            T = ones(len(matrix))

            T[i][i] = c
            T[j + 1][j + 1] = c
            T[i][j + 1] = s
            T[j + 1][i] = -s

            matrix = dot(dot(transpose(T), matrix), T)
    return matrix


# HOUSEHOLDER_END_________________________


# QR----------------------------------------
def find_self_qr(A, eps=1e-6):
    qrA = [r[:] for r in hessel_rot(A)]
    counter = 0
    old_self_qr = [np.inf] * len(qrA)
    qr_self = [qrA[i][i] for i in range(len(qrA))]

    while (vector_norm_1(plus(old_self_qr, mul(qr_self, -1))) > eps):
        counter += 1
        old_self_qr = qr_self[:]
        Q, R = qr_razloj(qrA)
        qrA = dot(R, Q)
        qr_self = [qrA[i][i] for i in range(len(qrA))]

    qr_self.sort()
    qr_self.reverse()
    print("Iters", counter)

    return qr_self




# MAIN--------------------------------------
temp_arr = numpy.linalg.eig(A)[0].tolist()
temp_arr.sort()
temp_arr.reverse()
print(temp_arr)

print("QR")
qr_self = find_self_qr(A)
print("delta qr", [abs(temp_arr[i] - qr_self[i]) for i in range(len(qr_self))])


