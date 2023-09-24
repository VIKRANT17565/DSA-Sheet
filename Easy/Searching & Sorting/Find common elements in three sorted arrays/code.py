def commonElements(A, B, C, n1, n2, n3):
    arr = []
    i, j, k = 0, 0, 0
    while(i < n1 and j < n2 and k < n3):
        if i >= n1 or j >= n2 or k >= n3:
            break
        if A[i] == B[j] and B[j] == C[k]:
            if A[i] not in arr:
                arr.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] < B[j] or A[i] < C[k]:
            i += 1

        elif A[i] > B[j] or B[j] < C[k]:
            j += 1

        elif C[k] < B[j] or A[i] > C[k]:
            k += 1
        
    return arr

print(commonElements([1, 5, 10, 20, 40, 100], 
                     [6, 7, 20, 80, 100], 
                     [3, 4, 15, 20, 30, 70, 80, 100],
                     6, 5, 8))