def commonElements(A, B, C):
    i, j, k = 0, 0, 0
    common = []

    while i < len(A) and j < len(B) and k < len(C):
        if A[i] == B[j] and B[j] == C[k]:
            common.append(A[i])
            i += 1
            j += 1
            k += 1
            while i < len(A) and A[i] == A[i - 1]:
                i += 1
            while j < len(B) and B[j] == B[j - 1]:
                j += 1
            while k < len(C) and C[k] == C[k - 1]:
                k += 1
        elif A[i] < B[j]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else:
            k += 1

    return common


# Sample Input
A = [1, 5, 10, 20, 30]
B = [5, 13, 15, 20]
C = [5, 20]

common = commonElements(A, B, C)

print("Common Elements:", end=" ")
print(common)