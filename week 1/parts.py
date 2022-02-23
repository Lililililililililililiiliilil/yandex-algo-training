n, k, m = map(int, input().split())

if k > n or m > k:
    print(0)
else:
    q = k // m
    m *= q

    print(((n - k + 1) // m + bool((n - k + 1) % m)) * q)
