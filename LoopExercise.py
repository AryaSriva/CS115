def f(L):
    A = [L[0]]
    for i in range(1, len(L) - 1):
        avg = (L[i] + L[i-1] + L[i+1])/3
        A.append(avg)
    A.append(L[len(L)-1])
    return A

print(f([1,2,2,2,5]))

