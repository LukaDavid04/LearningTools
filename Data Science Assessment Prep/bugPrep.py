def remove_k_elems(A, k):
    n = len(A)
    result = lambda arr, idx: arr[0:(idx)] + arr[(idx+k):n]
    return [result(A, i) for i in range(n-k+1)]

A = [2,4,6,8,10]
print(remove_k_elems(A,3))
